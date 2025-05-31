#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Youcheng Zhang
CS 5001, Spring 2024
Final Project - Controller: analysis fuctions file
"""
from geopy.distance import geodesic
from models.park import Park

FACILITY_COUNT_INCREMENT = 1
COUNT_INCREMENT = 1


# analysis functions dealing with Park
def find_park_by_park_name(parks, park_name):
    """
    Purpose: find the park based on a given park name

    Parameters:
        park_name(str): A string representing the name of a park
        parks(list): The list of Park objects

    Returns:
        A Park object

    Raises:
        TypeError: If parks is not a list or park_name is not a string.
        ValueError: If no park matches the given name
    """
    if not isinstance(parks, list):
        raise TypeError("parks must be a list")
    if not isinstance(park_name, str):
        raise TypeError("park_name must be a string")

    for park in parks:
        if park.name == park_name:
            return park

    raise ValueError(f"No park found with the name: {park_name}")


def find_park_by_park_id(parks, park_id):
    """
    Purpose: find the park based on a given park id

    Parameters:
        park_id(str): A string representing the id of a park
        parks(list): The list of Park objects

    Returns:
        A park object

    Raises:
        TypeError: If parks is not a list or park_id is not a string
        ValueError: If no park matches the given id
    """
    if not isinstance(parks, list):
        raise TypeError("parks must be a list")
    if not isinstance(park_id, str):
        raise TypeError("park_id must be a string")

    for park in parks:
        if park.id == park_id:
            return park

    raise ValueError(f"No park found with the id: {park_id}")


def find_parks_by_neighbourhood(parks, neighbourhood):
    """
    Purpose: get a list of park objects located within a specific
             neighbourhood

    Parameters:
        neighbourhood(str): A string representing the name of a neighbourhood
        parks(list): The list of Park objects

    Returns:
        A list, list of Park objects located within a specific neighbourhood

    Raises:
       TypeError: If parks is not a list or neighbourhood is not a string
       ValueError: If no parks are found in the specified neighbourhood
    """
    if not isinstance(parks, list):
        raise TypeError("parks must be a list")
    if not isinstance(neighbourhood, str):
        raise TypeError("neighbourhood must be a string")

    parks_in_neighbourhood = []

    for park in parks:
        if park.neighbourhood == neighbourhood:
            parks_in_neighbourhood.append(park)

    if not parks_in_neighbourhood:
        raise ValueError("No parks found in the neighbourhood: "
                         f"{neighbourhood}")

    return parks_in_neighbourhood


def filter_parks(parks, special_features=None,
                 facilities=None, washrooms=None):
    """
    Purpose: filter the parks based on the given criteria.

    Parameters:
        parks (list): The list of Park objects to be filtered.
        neighbourhood (str): The neighbourhood name to filter parks by
        special_features (str): Filters parks based on the presence ('Y') or
                                absence ('N') of special features
        facilities (str): Filters parks based on the presence ('Y') or absence
                          ('N') of facilities
        washrooms (str): Filters parks based on the presence ('Y') or absence
                         ('N') of washrooms

    Returns:
        A list, list of Park objects that match all specified criteria

    Raises:
        TypeError: If parks is not a list, or if special_features, facilities,
                   or washrooms are neither None nor a string
        ValueError: If special_features, facilities, or washrooms are provided
                    but are not 'Y' or 'N', or if no parks are found after
                    filtering
    """
    if not isinstance(parks, list):
        raise TypeError("parks must be a list")
    if special_features is not None and not isinstance(special_features, str):
        raise TypeError("special_features must be None or a string")
    if special_features not in ['Y', 'N']:
        raise ValueError("special_features must be 'Y' or 'N")
    if facilities is not None and not isinstance(facilities, str):
        raise TypeError("facilities must be None or a string")
    if facilities not in ['Y', 'N']:
        raise ValueError("facilities must be 'Y' or 'N")
    if washrooms is not None and not isinstance(washrooms, str):
        raise TypeError("washrooms must be None or a string")
    if washrooms not in ['Y', 'N']:
        raise ValueError("washrooms must be 'Y' or 'N")

    filtered_parks = []

    for park in parks:
        if park.matches_special_features(special_features) and \
           park.matches_facilities(facilities) and \
           park.matches_washrooms(washrooms):

            filtered_parks.append(park)

    if not filtered_parks:
        raise ValueError("No parks found after filtering")

    return filtered_parks


# analysis functions dealing with ParkFacility
def find_parks_by_park_facility_type(park_facilities, facility_type):
    """
    Purpose: get a list of the names of all parks that have the specified type
             of facility

    Parameters:
        park_facilities(list): The list of ParkFacility objects
        facility_type(str): A string representing the type of a facility

    Returns:
        A list, the names of all parks that have the specified type of
        facility

    Raises:
       TypeError: If park_facilities is not a list or if facility_type is not
                  a string
       ValueError: If no parks are found with the specified facility type
    """
    if not isinstance(park_facilities, list):
        raise TypeError("park_facilities must be a list")
    if not isinstance(facility_type, str):
        raise TypeError("facility_type must be a string")

    for park_facility in park_facilities:
        if park_facility.type == facility_type:
            return park_facility.parks

    raise ValueError("No parks found with the facility type: "
                     f"{facility_type}")


def count_facilities_with_specific_type(park_facilities, facility_type):
    """
    Purpose: get the number of park facilities with a specific type

    Parameters:
        park_facilities(list): The list of ParkFacility objects
        facility_type(str): A string representing the type of a facility

    Returns:
        An integer, number of park facilities with a specific type

    Raises:
        TypeError: If park_facilities is not a list or facility_type is not
                   a string
        ValueError: If no facilities are found with the specified type
    """
    if not isinstance(park_facilities, list):
        raise TypeError("park_facilities must be a list")
    if not isinstance(facility_type, str):
        raise TypeError("facility_type must be a string")

    for park_facility in park_facilities:
        if park_facility.type == facility_type:
            return park_facility.count

    raise ValueError(f"No facilities found with the type: {facility_type}")


# analhysis function dealing with graph and map construction
def extract_facility_distribution_data(park_facilities):
    """
    Purpose: extract data necessary for constructing and analyzing the
             distribution of facilities across parks

    Parameters:
        park_facilities(list): A list of ParkFacility objects

    Returns:
        A tuple, where the first element is the list of facility types, the
        second element is the list containing the number of parks that have
        the facility, and the third element is the list of facility to park
        ratios

    Raises:
        TypeError: If park_facilities is not a list
    """
    if not isinstance(park_facilities, list):
        raise TypeError("park_facilities must be a list")

    facility_types = []
    number_of_parks = []
    facility_to_park_ratios = []

    for facility in park_facilities:
        facility_types.append(facility.type)
        number_of_parks.append(facility.count_parks_with_facility())
        facility_to_park_ratios.append(
            facility.calculate_facility_to_park_ratio())
    return facility_types, number_of_parks, facility_to_park_ratios


def map_parks_to_neighbourhoods(parks):
    """
    Purpose: create a dictionary mapping from park names to their respective
             neighbourhoods

    Parameters:
        parks(list): The list of Park objects

    Returns:
        A dictionary, where each key is a park name and each value is the
        corresponding neighbourhood

    Raises:
        TypeError: If parks is not a list
    """
    if not isinstance(parks, list):
        raise TypeError("parks must be a list")

    park_to_neighbourhood = {}
    for park in parks:
        park_to_neighbourhood[park.name] = park.neighbourhood
    return park_to_neighbourhood


def create_facility_count_in_neighbourhood_dict(parks, park_facilities):
    """
    Purpose: create a dictionary where each key is a neighbourhood and each
             value is the count of facilities in that neighbourhood

    Parameters:
        parks(list): The list of Park objects
        park_facilities(list): The list of ParkFacility objects

    Returns:
        A dictionary, where each key is a neighbourhood and each value is the
        count of facilities in that neighbourhood

    Raises:
        TypeError: If parks or park_facilities are not lists
    """
    if not isinstance(parks, list):
        raise TypeError("parks must be a list")
    if not isinstance(park_facilities, list):
        raise TypeError("park_facilities must be a list")

    park_to_neighbourhood = map_parks_to_neighbourhoods(parks)

    facility_count_in_neighbourhood = {}

    for facility in park_facilities:
        for park_name in facility.parks:
            neighbourhood = park_to_neighbourhood.get(park_name)
            if neighbourhood in facility_count_in_neighbourhood:
                facility_count_in_neighbourhood[neighbourhood] += \
                    FACILITY_COUNT_INCREMENT
            else:
                facility_count_in_neighbourhood[neighbourhood] = \
                    FACILITY_COUNT_INCREMENT

    return facility_count_in_neighbourhood


def calculate_center(parks_in_neighbourhood):
    """
    Purpose: calculate the geographic center of a collection of parks in a
             specific neighbourhood

    Parameters:
        parks_in_neighbourhood(list): A list of Park objects located within a
                                      specific neighbourhood

    Returns:
        A tuple, the first element is the average latitude and the second
        element is the average longitude of the provided parks

    Raises:
        ValueError: If the input list is empty
        TypeError: If parks_in_neighbourhood is not a list
    """
    if not isinstance(parks_in_neighbourhood, list):
        raise TypeError("parks_in_neighbourhood must be a list")
    if not parks_in_neighbourhood:
        raise ValueError("parks_in_neighbourhood cannot be empty")

    total_latitude = 0
    total_latitude = 0
    total_longitude = 0
    count = 0

    for park in parks_in_neighbourhood:
        total_latitude += park.latitude
        total_longitude += park.longitude
        count += COUNT_INCREMENT

    center_latitude = total_latitude / count
    center_longitude = total_longitude / count
    return center_latitude, center_longitude


def calculate_distance(park, center_latitude, center_longitude):
    """
    Purpose: calculate the geodesic distance between a park and a neighborhood
             center

    Parameters:
        park(Park): A Park object
        center_latitude(float): A float representing the latitude of the
                                neighborhood center
        center_longitude(float): A float representing the longitude of the
                                 neighborhood center

    Returns:
        A float, The distance in kilometers between the park and the
        neighborhood center

    Raises:
        TypeError: If park is not an instance of Park, or center_latitude and
        center_longitude are not floats.
    """
    if not isinstance(park, Park):
        raise TypeError("park must be an instance of Park")
    if not isinstance(center_latitude, float) or not isinstance(
            center_longitude, float):
        raise TypeError("center_latitude and center_longitude must be floats")

    park_location = (park.latitude, park.longitude)
    park_location = (park.latitude, park.longitude)
    neighborhood_center = (center_latitude, center_longitude)
    distance = geodesic(park_location, neighborhood_center).kilometers
    return distance
