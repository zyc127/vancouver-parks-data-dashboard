#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Youcheng Zhang
CS 5001, Spring 2024
Final Project - Controller: helper functions file
"""
from models.fetch_data import fetch_url, clean_parks_from_url_response, \
    clean_parks_facilities_from_url_response
import analysis_functions as analysis
from views import user_interface as view
from views import data_visualization as visualization

PARKS_URL = (
    "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/parks"
    "/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&"
    "delimiter=%3B"
)

PARKS_FACILITIES_URL = (
    "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/"
    "parks-facilities/exports/csv?lang=en&timezone=America%2FLos_Angeles&"
    "use_labels=true&delimiter=%3B"
)
VIEW_PARKS_OPTION = "1"
SEARCH_PARK_OPTION = "2"
BASED_ON_ID_OPTION = "1"
BASED_ON_NAME_OPTION = "2"
BASED_ON_NEIGHBOURHOOD_OPTION = "3"
EXIT_MENU_OPTION = "4"
FILTER_PARKS_OPTION = "3"
PARK_FACILITIES_OPTION = "4"
VIEW_PARK_FACILITIES_OPTION = "1"
SEARCH_PARKS_BY_FACILITY_TYPE = "2"
COUNT_FACILITIES_BY_TYPE = "3"
VIEW_PARK_MAP_OPTION = "5"
VIEW_DISTANCE_MAP_OPTION = "6"
VIEW_FACILITY_DISTRIBUTION = "7"
VIEW_NEIGHBOURHOOD_FACILITY_DISTRIBUTION = "8"
VIEW_FACILITY_DIVERSITY_REPORT = "8"
EXIT_OPTION = "9"
RUN_PROGRAM = True
RUN_MENU = True
BACK_TO_PREVIOUS_MENU = False
END_PROGRAM = False


def get_parks():
    """
    Purpose: retrieve the list of all stored Park objects from URL

    Parameters:
        Nothing

    Returns:
        A list, list of Park objects

    Raises:
        Nothing
    """
    parks = clean_parks_from_url_response(fetch_url(PARKS_URL))
    return parks


def get_park_facilities():
    """
    Purpose: retrieve the list of all stored ParkFacility objects from URL

    Parameters:
        Nothing

    Returns:
        A list, list of ParkFacility objects

    Raises:
        Nothing
    """
    park_facilities = clean_parks_facilities_from_url_response(
        fetch_url(PARKS_FACILITIES_URL))
    return park_facilities


def output_parks():
    """
    Purpose: call the model to retrieve all parks and display them using the
             view

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    parks = get_parks()
    view.view_parks(parks)


def output_park_by_park_id():
    """
    Purpose: prompt the user to input the ID of a park and display information
             of the park with corresponding ID

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    parks = get_parks()
    park_id = view.get_park_id()
    park = analysis.find_park_by_park_id(parks, park_id)
    view.display_park_information(park)


def output_park_by_park_name():
    """
    Purpose: prompt the user to input the name of a park and display
             information of the park with corresponding name

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    parks = get_parks()
    park_name = view.get_park_name()
    park = analysis.find_park_by_park_name(parks, park_name)
    view.display_park_information(park)


def output_parks_by_neighbourhood():
    """
    Purpose: prompt the user to input a neighbourhood and display
             information of the parks located within the  neighbourhood

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    parks = get_parks()
    neighbourhood = view.get_neighbourhood()
    parks_in_neighbourhood = analysis.find_parks_by_neighbourhood(
        parks,
        neighbourhood)
    view.view_parks(parks_in_neighbourhood)


def filter_parks():
    """
    Purpose: collect filter criteria from the user, calls the model to filter
             parks, and displays the filtered parks using the view.

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    parks = get_parks()
    special_features = view.ask_for_special_features_preference()
    facilities = view.ask_for_facilities_preference()
    washrooms = view.ask_for_washrooms_preference()

    filtered_parks = analysis.filter_parks(parks, special_features,
                                           facilities, washrooms)
    view.view_parks(filtered_parks)


def output_park_facilities():
    """
    Purpose: call the model to retrieve all park facilities and display them
             using the view

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    park_facilities = get_park_facilities()
    view.view_park_facilities(park_facilities)


def output_parks_by_facility_type():
    """
    Purpose: prompt the user to input a facility type and display
             information of the parks have the specific facility

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    park_facilities = get_park_facilities()
    facility_type = view.get_facility_type()
    park_names = analysis.find_parks_by_park_facility_type(park_facilities,
                                                           facility_type)
    if not park_names:
        print("No parks has been found.")
    else:
        view.display_park_names_with_specified_facility_type(park_names,
                                                             facility_type)


def output_facility_count_by_facility_type():
    """
    Purpose: prompt the user to input a facility type and display
             number of the facility in Vancouver

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    park_facilities = get_park_facilities()
    facility_type = view.get_facility_type()
    facility_count = analysis.count_facilities_with_specific_type(
        park_facilities, facility_type)
    view.display_facility_count(facility_count, facility_type)


def output_facility_to_park_ratio_distribution():
    """
    Purpose: fetch park facility data and display a bar chart visualizing
             the facility-to-park ratio for different facility types

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    park_facilities = get_park_facilities()
    facility_types, number_of_parks, facility_to_park_ratios = \
        analysis.extract_facility_distribution_data(park_facilities)
    visualization.display_facility_to_park_ratio_distribution(
        facility_types, facility_to_park_ratios)


def output_facility_distribution_by_parks():
    """
    Purpose: fetch park facility data and display a bar chart showing the
             number of parks that contain each type of facility

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    park_facilities = get_park_facilities()
    facility_types, number_of_parks, facility_to_park_ratios = \
        analysis.extract_facility_distribution_data(park_facilities)
    visualization.display_facility_distribution_by_parks(
        facility_types, number_of_parks)


def output_neighbourhood_facility_distribution():
    """
    Purpose: fetche data on parks and their facilities, calculates the
             distribution of facilities across neighbourhoods, and displays
             this distribution as a pie chart

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    parks = get_parks()
    park_facilities = get_park_facilities()
    facility_count_in_neighbourhood = \
        analysis.create_facility_count_in_neighbourhood_dict(parks,
                                                             park_facilities)
    visualization.display_neighbourhood_facility_distribution(
        facility_count_in_neighbourhood)


def output_parks_in_neighbourhood_map():
    """
    Purpose: prompt the user to input a neighbourhood name, and generate and
             display an interactive map of all parks in the neighbourhood

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    parks = get_parks()
    neighbourhood = view.get_neighbourhood()
    parks_in_neighbourhood = analysis.find_parks_by_neighbourhood(
        parks, neighbourhood)
    center_latitude, center_longitude = analysis.calculate_center(
        parks_in_neighbourhood)
    visualization.display_parks_in_neighbourhood_map(parks_in_neighbourhood,
                                                     center_latitude,
                                                     center_longitude)


def output_distance_map():
    """
    Purpose: prompt the user to input a park name, and generate an
             interactive map visualizing the distance between the park and the
             neighbourhood center in which the park is located

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    parks = get_parks()
    park_name = view.get_park_name()
    park = analysis.find_park_by_park_name(parks, park_name)
    park_to_neighbourhood = analysis.map_parks_to_neighbourhoods(parks)
    neighbourhood = park_to_neighbourhood[park_name]
    parks_in_neighbourhood = analysis.find_parks_by_neighbourhood(
        parks, neighbourhood)
    center_latitude, center_longitude = analysis.calculate_center(
        parks_in_neighbourhood)
    distance = analysis.calculate_distance(park, center_latitude,
                                           center_longitude)
    visualization.visualize_distance_between_park_and_center(park,
                                                             center_latitude,
                                                             center_longitude,
                                                             distance)


def run_search_for_parks_menu():
    """
    Purpose: run an interactive menu for searching parks based on various
             criteria such as ID, name, or neighbourhood

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    run_menu = RUN_MENU

    while run_menu == RUN_MENU:
        view.display_search_park_menu()
        search_park_choice = view.get_user_choice()
        if search_park_choice == BASED_ON_ID_OPTION:
            output_park_by_park_id()
        elif search_park_choice == BASED_ON_NAME_OPTION:
            output_park_by_park_name()
        elif search_park_choice == BASED_ON_NEIGHBOURHOOD_OPTION:
            output_parks_by_neighbourhood()
        elif search_park_choice == EXIT_MENU_OPTION:
            run_menu = BACK_TO_PREVIOUS_MENU
        else:
            print("Invalid Input!")


def run_park_facilities_menu():
    """
    Purpose: run an interactive menu which allows users to view, search,
             and count park facilities by type

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    run_menu = RUN_MENU

    while run_menu == RUN_MENU:
        view.display_park_facilities_menu()
        park_facilities_choice = view.get_user_choice()
        if park_facilities_choice == VIEW_PARK_FACILITIES_OPTION:
            output_park_facilities()
        elif park_facilities_choice == SEARCH_PARKS_BY_FACILITY_TYPE:
            output_parks_by_facility_type()
        elif park_facilities_choice == COUNT_FACILITIES_BY_TYPE:
            output_facility_count_by_facility_type()
        elif park_facilities_choice == EXIT_MENU_OPTION:
            run_menu = BACK_TO_PREVIOUS_MENU
        else:
            print("Invalid Input!")


def run_program():
    """
    Purpose: runs the main loop of the application, managing user interactions
             through the main menu

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    run_program = RUN_PROGRAM

    while run_program == RUN_PROGRAM:
        view.display_main_menu()
        main_menu_choice = view.get_user_choice()

        if main_menu_choice == VIEW_PARKS_OPTION:
            output_parks()
        elif main_menu_choice == SEARCH_PARK_OPTION:
            run_search_for_parks_menu()
        elif main_menu_choice == FILTER_PARKS_OPTION:
            filter_parks()
        elif main_menu_choice == PARK_FACILITIES_OPTION:
            run_park_facilities_menu()
        elif main_menu_choice == VIEW_PARK_MAP_OPTION:
            output_parks_in_neighbourhood_map()
        elif main_menu_choice == VIEW_DISTANCE_MAP_OPTION:
            output_distance_map()
        elif main_menu_choice == VIEW_FACILITY_DISTRIBUTION:
            output_facility_distribution_by_parks()
            output_facility_to_park_ratio_distribution()
        elif main_menu_choice == VIEW_NEIGHBOURHOOD_FACILITY_DISTRIBUTION:
            output_neighbourhood_facility_distribution()
        elif main_menu_choice == EXIT_OPTION:
            run_program = END_PROGRAM
            print("Goodbye!")
        else:
            print("Invalid Input!")
