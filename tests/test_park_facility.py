#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Youcheng Zhang
CS 5001, Spring 2024
Final Project - Tests: test ParkFacility class
"""
import unittest
from models.park_facility import ParkFacility


class TestParkFacility(unittest.TestCase):
    """
    Unit test for the ParkFacility class.
    """

    def test_init(self):
        park_facility1 = ParkFacility('Facility A', ['Park A', 'Park B'], 4)
        self.assertEqual(park_facility1.type, 'Facility A')
        self.assertListEqual(park_facility1.parks, ['Park A', 'Park B'])
        self.assertEqual(park_facility1.count, 4)

    def test_init_facility_parameters_type_error(self):
        with self.assertRaises(TypeError):
            ParkFacility(123, ['Park A', 'Park B'], 4)

        with self.assertRaises(TypeError):
            ParkFacility('A', 'Park A', 4)

        with self.assertRaises(TypeError):
            ParkFacility('A', ['Park A', 'Park B'], 'A')

    def test_init_negative_count(self):
        with self.assertRaises(ValueError):
            ParkFacility('Playground', ['Park A', 'Park B'], -1)

    def test_str(self):
        park_facility2 = ParkFacility('Facility A', ['Park A', 'Park B'], 4)
        expected_str = ('\nFacility Type: Facility A\n'
                        'Number of Facilities: 4\n'
                        'Parks with this Facility: Park A, Park B')
        self.assertEqual(park_facility2.__str__(), expected_str)

    def test_count_parks_with_facility(self):
        park_facility3 = ParkFacility('Facility A', ['Park A', 'Park B'], 2)
        self.assertEqual(park_facility3.count_parks_with_facility(), 2)

    def test_calculate_facility_to_park_ratio(self):
        park_facility4 = ParkFacility('Facility A', ['Park A', 'Park B'], 4)
        self.assertEqual(park_facility4.calculate_facility_to_park_ratio(), 2)

    def test_calculate_facility_to_park_ratio_with_no_parks(self):
        park_facility5 = ParkFacility('Facility A', [], 4)
        with self.assertRaises(ZeroDivisionError):
            park_facility5.calculate_facility_to_park_ratio()
