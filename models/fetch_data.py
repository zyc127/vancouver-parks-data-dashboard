#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Youcheng Zhang
CS 5001, Spring 2024
Final Project - Models: data fetching file
"""
import requests
from .park import Park
from .park_facility import ParkFacility

EXPECTED_NUMBER_OF_PARTS_IN_PARKS = 15
EXPECTED_NUMBER_OF_PARTS_IN_PARKS_FACILITIES = 5
PARK_ID_INDEX = 0
PARK_NAME_INDEX_IN_PARKS = 1
SPECIAL_FEATURES_INDEX = 4
FACILITIES_INDEX = 5
WASHROOMS_INDEX = 6
STREET_NUMBER_INDEX = 7
SPACE = " "
STREET_NAME_INDEX = 8
NEIGHBOURHOOD_INDEX = 11
COORDINATES_INDEX = 14
LATITUDE_INDEX = 0
LONGITUDE_INDEX = 1
FACILITY_TYPE_INDEX = 2
FACILITY_COUNT_INDEX = 3
PARK_NAME_INDEX_IN_PARKS_FACILITIES = 1
HEADER_LINE_INDEX = 1
PARKS_LIST_INDEX = 0
FACILITIES_COUNT_INDEX = 1
SEMICOLON = ';'
COMMA = ','


def fetch_url(url):
    """
    Purpose: open and fetch the contents of a URL

    Parameters:
        url(str): A string representing a URL pointing to a web resource

    Returns:
        A csv file, file fetched from the URL

    Raises:
        HTTPError: If HTTP request to the URL fails due to an error response
                   status code
        ConnectionError: If HTTP request to the URL fails due to network
                         problems
        TypeError: If url is not a string
    """
    if not isinstance(url, str):
        raise TypeError("url must be a string")

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")

    except requests.exceptions.ConnectionError as e:
        print(f"Connection error occurred: {e}")

    else:
        return response


def clean_parks_from_url_response(response):
    """
    Purpose: read parks data from an HTTP response and create a list of Park
             objects

    Parameters:
        response(csv): A csv file containing the text with parks data

    Returns:
        A list, the list of Park objects

    Raises:
        ValueError: If a line in the file does not contain exactly the
                    expected number of parts
    """
    parks = []

    content = response.text.splitlines()

    for line in content[HEADER_LINE_INDEX:]:
        parts = line.strip().split(SEMICOLON)

        if len(parts) != EXPECTED_NUMBER_OF_PARTS_IN_PARKS:
            raise ValueError("The content does not match the "
                             "expected format")

        park_id = parts[PARK_ID_INDEX]
        park_name = parts[PARK_NAME_INDEX_IN_PARKS]
        special_features = parts[SPECIAL_FEATURES_INDEX]
        facilities = parts[FACILITIES_INDEX]
        washrooms = parts[WASHROOMS_INDEX]
        street_location = parts[STREET_NUMBER_INDEX] + SPACE + \
            parts[STREET_NAME_INDEX]
        neighbourhood = parts[NEIGHBOURHOOD_INDEX]
        corordinates_str = parts[COORDINATES_INDEX]
        corordinates = corordinates_str.split(COMMA)
        latitude = float(corordinates[LATITUDE_INDEX])
        longitude = float(corordinates[LONGITUDE_INDEX])

        parks.append(Park(park_id, park_name, special_features, facilities,
                          washrooms, street_location, neighbourhood,
                          latitude, longitude))
    return parks


def construct_park_facility_dictionary(facilities_types, facilities_count,
                                       parks_names):
    """
    Purpose: create a dictionary where the facilities' types is key and
             lists containing two elements is the value, the first element is
             a sublist containing the parks' names associated with the parks'
             facilities and the second element is the count of the facilities

    Parameters:
        facilities_types(list): A list reperesenting types of the
                                facilities
        facilities_count(list): A list representing count if the
                                facilities
        parks_names(list): A list representing names if the parks

    Returns:
        A dictionary, where the facilities' types is key and lists containing
        two elements is the value, the first element is a sublist containing
        the parks' names associated with the parks' facilities and the second
        element is the count of the facilities

    Raises:
        TypeError: If the parameters are not of type list as expected
        ValueError: If the lengths of the input lists do not match
    """
    if not isinstance(facilities_types, list):
        raise TypeError("facilities_types must be a list")
    if not isinstance(facilities_count, list):
        raise TypeError("facilities_count must be a list")
    if not isinstance(parks_names, list):
        raise TypeError("parks_names must be a list")
    if not len(facilities_types) == len(facilities_count) == \
            len(parks_names):
        raise ValueError("Input lists must have the same length")

    park_facility_dictionary = {}

    for index, facility in enumerate(facilities_types):
        if facility in park_facility_dictionary:
            park_facility_dictionary[facility][PARKS_LIST_INDEX].append(
                parks_names[index])
            park_facility_dictionary[facility][FACILITIES_COUNT_INDEX] += \
                facilities_count[index]

        else:
            park_facility_dictionary[facility] = [[parks_names[index]],
                                                  facilities_count[index]]
    return park_facility_dictionary


def clean_parks_facilities_from_url_response(response):
    """
    Purpose: read parks facilities data from an HTTP response and create a
             list of ParkFacility objects

    Parameters:
        response(csv): A csv file containing the text with parks facilities
                       data

    Returns:
        A list, the list of ParkFacility objects

    Raises:
        ValueError: If a line in the file does not contain exactly the
                    expected number of parts
    """
    parks_facilities = []
    facilities_types = []
    parks_names = []
    facilities_count = []

    content = response.text.splitlines()

    for line in content[HEADER_LINE_INDEX:]:
        parts = line.strip().split(SEMICOLON)

        if len(parts) != EXPECTED_NUMBER_OF_PARTS_IN_PARKS_FACILITIES:
            raise ValueError("The content does not match the "
                             "expected format")

        facility_type = parts[FACILITY_TYPE_INDEX]
        facility_count = int(parts[FACILITY_COUNT_INDEX])
        park_name = parts[PARK_NAME_INDEX_IN_PARKS_FACILITIES]

        facilities_types.append(facility_type)
        parks_names.append(park_name)
        facilities_count.append(facility_count)

    park_facility_dictionary = construct_park_facility_dictionary(
            facilities_types, facilities_count, parks_names)

    for facility_type, value in park_facility_dictionary.items():
        parks_with_facility = value[PARKS_LIST_INDEX]
        facility_count = value[FACILITIES_COUNT_INDEX]

        parks_facilities.append(ParkFacility(facility_type,
                                             parks_with_facility,
                                             facility_count))
    return parks_facilities
