#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Youcheng Zhang
CS 5001, Spring 2024
Final Project - Views: user interface file
"""
from models.park import Park


# Interaction with Park
def get_park_id():
    """
    Purpose: prompt the user for the park ID and return the value

    Parameters:
        Nothing

    Returns:
        A str, park ID

    Raises:
        Nothing
    """
    park_id = input("Enter park ID: ")
    return park_id


def get_park_name():
    """
    Purpose: prompt the user for the park name and return the value

    Parameters:
        Nothing

    Returns:
        A str, park name

    Raises:
        Nothing
    """
    park_name = input("Enter park name: ")
    return park_name


def get_neighbourhood():
    """
    Purpose: prompt the user for the neighbourhood name and return the value

    Parameters:
        Nothing

    Returns:
        A str, neighbourhood name

    Raises:
        Nothing
    """
    neighbourhood = input("Enter neighbourhood: ")
    return neighbourhood


def get_street_location():
    """
    Purpose: prompt the user for the street location and return the value

    Parameters:
        Nothing

    Returns:
        A str, street location

    Raises:
        Nothing
    """
    street_location = input("Enter street location: ")
    return street_location


def ask_for_special_features_preference():
    """
    Purpose: ask the user whether they want to filter the parks to only
             include those with special features

    Parameters:
        Nothing

    Returns:
        A str, 'Y' represents yes, 'N' represents no

    Raises:
        Nothing
    """
    special_features_choice = input("Do you want to view parks with special "
                                    "features? (Y/N): ")
    return special_features_choice.upper()


def ask_for_facilities_preference():
    """
    Purpose: ask the user whether they want to filter the parks to only
             include those with facilities

    Parameters:
        Nothing

    Returns:
        A str, 'Y' represents yes, 'N' represents no

    Raises:
        Nothing
    """
    facilities_choice = input("Do you want to view parks with facilities? "
                              "(Y/N): ")
    return facilities_choice.upper()


def ask_for_washrooms_preference():
    """
    Purpose: ask the user whether they want to filter the parks to only
             include those with washrooms

    Parameters:
        Nothing

    Returns:
        A str, 'Y' represents yes, 'N' represents no

    Raises:
        Nothing
    """
    washrooms_choice = input("Do you want to view parks with washrooms? "
                             "(Y/N): ")
    return washrooms_choice.upper()


def display_park_information(park):
    """
    Purpose: display the information of the given park

    Parameters:
        park(Park): A Park object representing the park to display.

    Returns:
        Nothing

    Raises:
        TypeError: If park is not an instance of Park
    """
    if not isinstance(park, Park):
        raise TypeError("park must be an instance of Park")

    print(park)


def view_parks(parks):
    """
    Purpose: display the infomation of all parks in a given list of Park
             objects

    Parameters:
        parks(list): The list of Park objects

    Returns:
        Nothing

    Raises:
        ValueError: If the input list is empty
        TypeError: If parks is not a list
    """
    if not isinstance(parks, list):
        raise TypeError("parks must be a list")
    if not parks:
        raise ValueError("No parks has been found.")

    for park in parks:
        display_park_information(park)


# Interaction with ParkFacility
def get_facility_type():
    """
    Purpose: prompt the user for the facility type and return the value

    Parameters:
        Nothing

    Returns:
        A str, facility type

    Raises:
        Nothing
    """
    facility_type = input("Enter facility type: ")
    return facility_type


def view_park_facilities(park_facilities):
    """
    Purpose: display the infomation of all park facilities in a given list of
             ParkFacility objects

    Parameters:
        park_facilities(list): The list of ParkFacility objects

    Returns:
        Nothing

    Raises:
        ValueError: If the input list is empty
        TypeError: If park_facilities is not a list
    """
    if not isinstance(park_facilities, list):
        raise TypeError("park_facilities must be a list")
    if not park_facilities:
        raise ValueError("No park_facilities has been found.")

    for facility in park_facilities:
        print(facility)


def display_park_names_with_specified_facility_type(park_names,
                                                    facility_type):
    """
    Purpose: display names of the parks have a specific facility

    Parameters:
        park_names(list): The list of names of the parks have specific
                          facility
        facility_type(str): A string representing type of the facility

    Returns:
        Nothing

    Raises:
        TypeError: If park_names is not a list or facility_type is not a
                   string
    """
    if not isinstance(park_names, list):
        raise TypeError("park_names must be a list")
    if not isinstance(facility_type, str):
        raise TypeError("facility_type must be a str")

    parks = ', '.join(park_names)
    print(f"{facility_type} can be found in:\n{parks}")


def display_facility_count(facility_count, facility_type):
    """
    Purpose: display the number of a specific facility in Vancouver

    Parameters:
        facility_count(int): An integer representing the number of the
                             facility
        facility_type(str): A string representing type of the facility

    Returns:
        Nothing

    Raises:
        TypeError: If facility_count is not an integer or facility_type is not
                   a stirng
    """
    if not isinstance(facility_count, int):
        raise TypeError("facility_count must be an integer")
    if not isinstance(facility_type, str):
        raise TypeError("facility_type must be a string")

    print(f"There are a total of {facility_count} {facility_type} spread "
          "across various parks in Vancouver.")


# Display menus
def display_main_menu():
    """
    Purpose: display the main menu of the program

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    print("\nWelcome to the Vancouver Park Explorer! Please select an "
          "option:")
    print("\n1. View Parks")
    print("2. Search for Parks")
    print("3. Filter Parks")
    print("4. View and Search for Park Facilities")
    print("5. View Park Maps by Neighbourhood")
    print("6. View Distance Between Parks and Neighbourhood Centers")
    print("7. View Facility Distribution Accross Parks")
    print("8. View Neighbourhood Facility Distribution")
    print("9. Exit")


def display_search_park_menu():
    """
    Purpose: display the menu of the search park section

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    print("\nSearch for Parks:")
    print("1. Based on ID")
    print("2. Based on Park Name")
    print("3. Based on Neighbourhood")
    print("4. Back to Previous Menu")


def display_park_facilities_menu():
    """
    Purpose: display the menu of the park facilities section

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    print("\nView and Search for Park Facilities:")
    print("1. View Park Facilities")
    print("2. Search Parks Based on Park Facility Type")
    print("3. Count Vancouver Park Facilities by Type")
    print("4. Back to Previous Menu")


# Get user choice
def get_user_choice():
    """
    Purpose: prompt and return the user's choice from the displayed main menu

    Parameters:
        Nothing

    Returns:
        A str, the user's choice

    Raises:
        Nothing
    """
    choice = input("\nEnter your choice: ")
    return choice
