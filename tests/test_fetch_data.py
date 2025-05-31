#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Youcheng Zhang
CS 5001, Spring 2024
Final Project - Tests: test fetch data file
"""
import unittest
import requests
import requests_mock
from models.fetch_data import fetch_url, clean_parks_from_url_response, \
    construct_park_facility_dictionary, \
    clean_parks_facilities_from_url_response


class TestFetchData(unittest.TestCase):
    """
    Unit test for the fetch data file.
    """

    def test_fetch_url_with_invalid_url_type(self):
        with self.assertRaises(TypeError):
            fetch_url(123)

    def test_fetch_url_success(self):
        with requests_mock.Mocker() as mock:
            mock.get("http://abc.com", text="abc")
            response = fetch_url("http://abc.com")
            self.assertEqual(response.text, "abc")

    def test_fetch_url_http_error(self):
        with requests_mock.Mocker() as mock:
            mock.get("http://abc.com", text="abc", status_code=500)
            response = fetch_url("http://abc.com")
            self.assertIsNone(response)

    def test_fetch_url_connection_error(self):
        with requests_mock.Mocker() as mock:
            mock.get("http://abc.com",
                     exc=requests.exceptions.ConnectionError)
            response = fetch_url("http://abc.com")
            self.assertIsNone(response)

    def test_clean_parks_from_url_response_invalid_format(self):
        with requests_mock.Mocker() as mock:
            mock.get('http://abc.com', text="a;b\nc;d")
            with self.assertRaises(ValueError):
                response = requests.get('http://abc.com')
                clean_parks_from_url_response(response)

    def test_construct_park_facility_dictionary(self):
        facilities_types = ['A', 'B', 'A']
        facilities_count = [1, 2, 3]
        parks_names = ['aa', 'bb', 'cc']
        expected_dict = {'A': [['aa', 'cc'], 4], 'B': [['bb'], 2]}
        result = construct_park_facility_dictionary(facilities_types,
                                                    facilities_count,
                                                    parks_names)
        self.assertEqual(result, expected_dict)

    def test_construct_park_facility_dictionary_parameters_mismatched_lengths(
            self):
        with self.assertRaises(ValueError):
            construct_park_facility_dictionary([1, 2, 3], [1, 2], [1])

    def test_clean_parks_facilities_from_url_response_invalid_format(self):
        with requests_mock.Mocker() as mock:
            mock.get('http://abc.com', text="a;b\nc;d")
            with self.assertRaises(ValueError):
                response = requests.get('http://abc.com')
                clean_parks_facilities_from_url_response(response)
