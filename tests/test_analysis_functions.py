#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Youcheng Zhang
CS 5001, Spring 2024
Final Project - Tests: test analysis functions
"""
import unittest
from analysis_functions import find_park_by_park_name, \
    find_park_by_park_id, find_parks_by_neighbourhood, filter_parks, \
    find_parks_by_park_facility_type, count_facilities_with_specific_type, \
    extract_facility_distribution_data, map_parks_to_neighbourhoods, \
    create_facility_count_in_neighbourhood_dict, calculate_center, \
    calculate_distance
from models.park import Park
from models.park_facility import ParkFacility


class TestParkAnalysisFunctions(unittest.TestCase):
    """
    Unit test for the analysis functions dealing with Park.
    """

    def setUp(self):
        park1 = Park("1", "A", "Y", "Y", "Y", "S1", "N1", 45.1, 123.1)
        park2 = Park("2", "B", "Y", "N", "Y", "S2", "N2", 46.2, 123.5)
        park3 = Park("3", "C", "N", "Y", "N", "S3", "N3", 47.3, 124.0)
        self.parks = [park1, park2, park3]

    def test_find_park_by_park_name(self):
        result = find_park_by_park_name(self.parks, "A")
        self.assertEqual(result, self.parks[0])

    def test_find_park_by_invalid_park_name(self):
        with self.assertRaises(ValueError):
            find_park_by_park_name(self.parks, "No such park")

    def test_find_park_by_park_id(self):
        result = find_park_by_park_id(self.parks, "2")
        self.assertEqual(result, self.parks[1])

    def test_find_park_by_invalid_park_id(self):
        with self.assertRaises(ValueError):
            find_park_by_park_id(self.parks, "1000")

    def test_find_parks_by_neighbourhood(self):
        park = find_parks_by_neighbourhood(self.parks, "N1")
        self.assertEqual(park, [self.parks[0]])

    def test_find_parks_by_neighbourhood_no_parks_found(self):
        with self.assertRaises(ValueError):
            find_parks_by_neighbourhood(self.parks, "No such neighbourhood")

    def test_find_parks_by_neighbourhood_wrong_type_parks(self):
        with self.assertRaises(TypeError):
            find_parks_by_neighbourhood("Not a list", "N1")

    def test_find_parks_by_neighbourhood_wrong_type_neighbourhood(self):
        with self.assertRaises(TypeError):
            find_parks_by_neighbourhood(self.parks, 123)

    def test_filter_parks(self):
        filtered_park = filter_parks(self.parks, "Y", "Y", "Y")
        self.assertEqual(filtered_park, [self.parks[0]])

    def test_filter_parks_no_parks_found(self):
        with self.assertRaises(ValueError):
            filter_parks(self.parks, "N", "N", "N")

    def test_filter_parks_invalid_parks_type(self):
        with self.assertRaises(TypeError):
            filter_parks("Not a list", "Y", "Y", "Y")

    def test_filter_parks_invalid_special_features_input(self):
        with self.assertRaises(ValueError):
            filter_parks(self.parks, "O", "Y", "Y")

    def test_filter_parks_invalid_facilities_input(self):
        with self.assertRaises(ValueError):
            filter_parks(self.parks, "Y", "O", "Y")

    def test_filter_parks_invalid_washrooms_input(self):
        with self.assertRaises(ValueError):
            filter_parks(self.parks, "Y", "Y", "O")


class TestParkFacilityAnalysisFunction(unittest.TestCase):
    """
    Unit test for the analysis functions dealing with ParkFacility.
    """

    def setUp(self):
        facility1 = ParkFacility("A", ["P1", "P2"], 4)
        facility2 = ParkFacility("B", ["P1", "P3"], 5)
        facility3 = ParkFacility("C", ["P4", "P5"], 6)
        self.facilities = [facility1, facility2, facility3]

    def test_find_parks_by_facility_type(self):
        parks = find_parks_by_park_facility_type(self.facilities, "A")
        self.assertEqual(parks, ["P1", "P2"])

    def test_find_parks_by_facility_type_no_parks_found(self):
        with self.assertRaises(ValueError):
            find_parks_by_park_facility_type(self.facilities, "D")

    def test_find_parks_by_facility_type_invalid_park_facilities_type(self):
        with self.assertRaises(TypeError):
            find_parks_by_park_facility_type("Not a list", "A")

    def test_find_parks_by_facility_type_invalid_facility_type(self):
        with self.assertRaises(TypeError):
            find_parks_by_park_facility_type(self.facilities, 123)

    def test_count_facilities(self):
        count = count_facilities_with_specific_type(self.facilities, "B")
        self.assertEqual(count, 5)

    def test_count_facilities_no_facilities_found(self):
        with self.assertRaises(ValueError):
            count_facilities_with_specific_type(self.facilities, "D")

    def test_count_facilities_invalid_park_facilities_type(self):
        with self.assertRaises(TypeError):
            count_facilities_with_specific_type("Not a list", "A")

    def test_count_facilities_invalid_facility_type(self):
        with self.assertRaises(TypeError):
            count_facilities_with_specific_type(self.facilities, 123)


class TestAnalysisFunctionsForTwoClasses(unittest.TestCase):
    """
    Unit test for the functions analysing data for visualization and dealing
    with both Park and ParkFacility classes.
    """

    def setUp(self):
        park1 = Park("1", "A", "Y", "Y", "Y", "S1", "N1", 45.1, 123.1)
        park2 = Park("2", "B", "Y", "N", "Y", "S2", "N2", 46.2, 123.5)
        park3 = Park("3", "C", "N", "Y", "N", "S3", "N3", 47.3, 124.0)
        self.parks = [park1, park2, park3]

        facility1 = ParkFacility("A", ["A", "B"], 4)
        facility2 = ParkFacility("B", ["A", "C"], 4)
        facility3 = ParkFacility("C", ["B", "C"], 4)
        self.facilities = [facility1, facility2, facility3]

    def test_extract_facility_distribution_valid(self):
        facility_types, number_of_parks, facility_to_park_ratios = \
            extract_facility_distribution_data(self.facilities)
        self.assertEqual(facility_types, ["A", "B", "C"])
        self.assertEqual(number_of_parks, [2, 2, 2])
        self.assertEqual(facility_to_park_ratios, [2.0, 2.0, 2.0])

    def test_extract_facility_distribution_invalid_park_facilities_type(self):
        with self.assertRaises(TypeError):
            extract_facility_distribution_data("Not a list")

    def test_map_parks_to_neighbourhoods_valid(self):
        park_to_neighbourhood = map_parks_to_neighbourhoods(self.parks)
        expected_dict = {"A": "N1", "B": "N2", "C": "N3"}
        self.assertEqual(park_to_neighbourhood, expected_dict)

    def test_map_parks_to_neighbourhoods_invalid_type(self):
        with self.assertRaises(TypeError):
            map_parks_to_neighbourhoods("Not a list")

    def test_neighourhood_facility_count(self):
        count_dict = create_facility_count_in_neighbourhood_dict(
            self.parks, self.facilities)
        expected_dict = {"N1": 2, "N2": 2, "N3": 2}
        self.assertEqual(count_dict, expected_dict)

    def test_neighourhood_facility_count_invalid_park_list_type(self):
        with self.assertRaises(TypeError):
            create_facility_count_in_neighbourhood_dict("Not a list",
                                                        self.facilities)

    def test_neighourhood_facility_count_invalid_facility_list_type(self):
        with self.assertRaises(TypeError):
            create_facility_count_in_neighbourhood_dict(self.parks,
                                                        "Not a list")

    def test_calculate_center_valid(self):
        center = calculate_center(self.parks)
        expected = ((45.1 + 46.2 + 47.3) / 3, (123.1 + 123.5 + 124.0) / 3)
        self.assertAlmostEqual(center[0], expected[0])
        self.assertAlmostEqual(center[1], expected[1])

    def test_calculate_center_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_center([])

    def test_calculate_center_invalid_parameter_type(self):
        with self.assertRaises(TypeError):
            calculate_center("Not a list")

    def test_calculate_distance_invalid_park_type(self):
        with self.assertRaises(TypeError):
            calculate_distance("Not a park", 40.1, -70.1)

    def test_calculate_distance_invalid_lat_lon_types(self):
        park = Park('1', 'A Park', 'Y', 'Y', 'N', '123 W Ave', 'DT', 45.123,
                    90.123)
        with self.assertRaises(TypeError):
            calculate_distance(park, "40", -70.1)

        with self.assertRaises(TypeError):
            calculate_distance(park, 40.1, "70")
