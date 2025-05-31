#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Youcheng Zhang
CS 5001, Spring 2024
Final Project - Tests: test Park class
"""
import unittest
from models.park import Park


class TestPark(unittest.TestCase):
    """
    Unit test for the Park class.
    """

    def test_init(self):
        park1 = Park('1', 'A Park', 'Y', 'Y', 'N', '123 W Ave', 'DT', 45.123,
                     90.123)
        self.assertEqual(park1.id, '1')
        self.assertEqual(park1.name, 'A Park')
        self.assertEqual(park1.special_features, 'Y')
        self.assertEqual(park1.facilities, 'Y')
        self.assertEqual(park1.washrooms, 'N')
        self.assertEqual(park1.street_location, '123 W Ave')
        self.assertEqual(park1.neighbourhood, 'DT')
        self.assertEqual(park1.latitude, 45.123)
        self.assertEqual(park1.longitude, 90.123)

    def test_park_id_type_error(self):
        with self.assertRaises(TypeError):
            Park(123, 'A Park', 'Y', 'Y', 'N', '123 W Ave', 'DT', 45.123,
                 90.123)

    def test_park_name_type_error(self):
        with self.assertRaises(TypeError):
            Park('1', 123, 'Y', 'Y', 'N', '123 W Ave', 'DT', 45.123, 90.123)

    def test_special_features_type_error(self):
        with self.assertRaises(TypeError):
            Park('1', 'A Park', 123, 'Y', 'N', '123 W Ave', 'DT', 45.123,
                 90.123)

    def test_facilities_type_error(self):
        with self.assertRaises(TypeError):
            Park('1', 'A Park', 'Y', 123, 'N', '123 W Ave', 'DT', 45.123,
                 90.123)

    def test_washrooms_type_error(self):
        with self.assertRaises(TypeError):
            Park('1', 'A Park', 'Y', 'Y', 123, '123 W Ave', 'DT', 45.123,
                 90.123)

    def test_street_location_type_error(self):
        with self.assertRaises(TypeError):
            Park('1', 'A Park', 'Y', 'Y', 'N', 123, 'DT', 45.123, 90.123)

    def test_neighbourhood_type_error(self):
        with self.assertRaises(TypeError):
            Park('1', 'A Park', 'Y', 'Y', 'N', '123 W Ave', 123, 45.123,
                 90.123)

    def test_latitude_type_error(self):
        with self.assertRaises(TypeError):
            Park('1', 'A Park', 'Y', 'Y', 'N', '123 W Ave', 'DT', 'A', 90.123)

    def test_longitude_type_error(self):
        with self.assertRaises(TypeError):
            Park('1', 'A Park', 'Y', 'Y', 'N', '123 W Ave', 'DT', 45.123, 'A')

    def test_init_invalide_lantitude(self):
        with self.assertRaises(ValueError) as ve:
            Park('1', 'A Park', 'Y', 'Y', 'N', '123 W Ave', 'DT', 100.1, 90.1)
        self.assertEqual(str(ve.exception),
                         "Latitude must be between -90 and 90 degrees")

        with self.assertRaises(ValueError) as ve:
            Park('1', 'A Park', 'Y', 'Y', 'N', '123 W Ave', 'DT', -100.1,
                 90.1)
        self.assertEqual(str(ve.exception),
                         "Latitude must be between -90 and 90 degrees")

    def test_init_invalid_longitude(self):
        with self.assertRaises(ValueError) as ve:
            Park('1', 'A Park', 'Y', 'Y', 'N', '123 W Ave', 'DT', 45.1, 200.1)
        self.assertEqual(str(ve.exception),
                         "Longitude must be between -180 and 180 degrees")

        with self.assertRaises(ValueError):
            Park('1', 'A Park', 'Y', 'Y', 'N', '123 W Ave', 'DT', 45.1,
                 -200.1)
        self.assertEqual(str(ve.exception),
                         "Longitude must be between -180 and 180 degrees")

    def test_str(self):
        park2 = Park('1', 'A Park', 'Y', 'Y', 'N', '123 W Ave', 'DT', 45.123,
                     90.123)
        expected_str = ('\nA Park\n(ID: 1, Special Features: Y, Facilities: Y'
                        ', Washrooms: N, Street Location: 123 W Ave, '
                        'Neighbourhood: DT)')
        self.assertEqual(park2.__str__(), expected_str)

    def test_matches_special_features(self):
        park3 = Park('1', 'A Park', 'Y', 'Y', 'N', '123 W Ave', 'DT', 45.123,
                     90.123)
        self.assertTrue(park3.matches_special_features('Y'))
        self.assertFalse(park3.matches_special_features('N'))

    def test_matches_special_features_invalid_input(self):
        park4 = Park('1', 'A Park', 'Y', 'Y', 'N', '123 W Ave', 'DT', 45.123,
                     90.123)
        with self.assertRaises(ValueError) as ve:
            park4.matches_special_features('A')
        self.assertEqual(str(ve.exception),
                         "special_features must be 'Y' or 'N'")

    def test_matches_facilities(self):
        park5 = Park('1', 'A Park', 'Y', 'Y', 'N', '123 W Ave', 'DT', 45.123,
                     90.123)
        self.assertTrue(park5.matches_facilities('Y'))
        self.assertFalse(park5.matches_facilities('N'))

    def test_matches_facilities_invalid_input(self):
        park6 = Park('1', 'A Park', 'Y', 'Y', 'N', '123 W Ave', 'DT', 45.123,
                     90.123)
        with self.assertRaises(ValueError) as ve:
            park6.matches_facilities('A')
        self.assertEqual(str(ve.exception),
                         "facilities must be 'Y' or 'N'")

    def test_matches_washrooms(self):
        park7 = Park('1', 'A Park', 'Y', 'Y', 'N', '123 W Ave', 'DT', 45.123,
                     90.123)
        self.assertFalse(park7.matches_washrooms('Y'))
        self.assertTrue(park7.matches_washrooms('N'))

    def test_matches_washrooms_invalid_input(self):
        park8 = Park('1', 'A Park', 'Y', 'Y', 'N', '123 W Ave', 'DT', 45.123,
                     90.123)
        with self.assertRaises(ValueError) as ve:
            park8.matches_washrooms('A')
        self.assertEqual(str(ve.exception),
                         "washrooms must be 'Y' or 'N'")
