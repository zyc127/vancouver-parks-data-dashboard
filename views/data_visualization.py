#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Youcheng Zhang
CS 5001, Spring 2024
Final Project - Views: data visualization file
"""
import matplotlib.pyplot as plt
import folium
import os
import webbrowser
from models.park import Park

BAR_FIGURE_WIDTH = 25
BAR_FIGURE_HEIGHT = 10
BAR_XTICKS_ROTATION = 45
PIE_CHART_WIDTH = 20
PIE_CHART_HEIGHT = 18
PIE_CHART_START_ANGLE = 90
ZOOM_LEVEL = 13
BAR_CHART_COLOUR = 'skyblue'
HORIZONTAL_ALIGNMENT_RIGHT = 'right'
AUTOPCT_FORMAT = '%1.1f%%'
AXIS_EQUAL = 'equal'
NEIGHBOURHOOD_CENTER_ICON_COLOUR = 'red'
PAKR_ICON_COLOUR = 'green'
DISTANCE_LINE_COLOUR = 'blue'


def display_facility_to_park_ratio_distribution(facility_types,
                                                facility_to_park_ratios):
    """
    Purpose: display a bar chart of the facility-to-park ratio for different
            facility types

    Parameters:
        facility_types(list): A list containing the names of different
                              facility types
        facility_to_park_ratios(list): A list containing calculated
                                       facility-to-park ratios

    Returns:
        Nothing

    Raises:
        TypeError: If facility_types is not a list or if
                   facility_to_park_ratios is not a list
        ValueError: If facility_types and facility_to_park_ratios do not have
                    the same length
    """
    if not isinstance(facility_types, list):
        raise TypeError("facility_types must be a list")
    if not isinstance(facility_to_park_ratios, list):
        raise TypeError("facility_to_park_ratios must be a list")
    if len(facility_types) != len(facility_to_park_ratios):
        raise ValueError("The length of facility_types and facility_to_park_"
                         "ratios must match")

    plt.figure(figsize=(BAR_FIGURE_WIDTH, BAR_FIGURE_HEIGHT))
    plt.bar(facility_types, facility_to_park_ratios, color=BAR_CHART_COLOUR)
    plt.title('Facility to Park Ratio by Facility Type')
    plt.xlabel('Facility Type')
    plt.ylabel('Facility to Park Ratio')
    plt.xticks(rotation=BAR_XTICKS_ROTATION, ha=HORIZONTAL_ALIGNMENT_RIGHT)
    plt.tight_layout()
    plt.show()


def display_facility_distribution_by_parks(facility_types, number_of_parks):
    """
    Purpose: display a bar chart showing the number of parks that contain
             each type of facility

    Parameters:
        facility_types(list): A list containing the names of different
                              facility types
        number_of_parks(list): A list containing the number of parks that have
                               each corresponding facility type

    Returns:
        Nothing

    Raises:
        TypeError: If facility_types is not a or number_of_parks is not a list
        ValueError: If the lengths of facility_types and number_of_parks do
                    not match
    """
    if not isinstance(facility_types, list):
        raise TypeError("facility_types must be a list")
    if not isinstance(number_of_parks, list):
        raise TypeError("number_of_parks must be a list")
    if len(facility_types) != len(number_of_parks):
        raise ValueError("The length of facility_types and number_of_parks "
                         "must match")

    plt.figure(figsize=(BAR_FIGURE_WIDTH, BAR_FIGURE_HEIGHT))
    plt.bar(facility_types, number_of_parks, color=BAR_CHART_COLOUR)
    plt.title('Number of Parks Containing Each Type of Facility')
    plt.xlabel('Facility Type')
    plt.ylabel('Number of Parks')
    plt.xticks(rotation=BAR_XTICKS_ROTATION, ha=HORIZONTAL_ALIGNMENT_RIGHT)
    plt.tight_layout()
    plt.show()


def display_neighbourhood_facility_distribution(
        facility_count_in_neighbourhood):
    """
    Purpose: display a pie chart visualizing the distribution of facilities
             across neighbourhoods

    Parameters:
        facility_count_in_neighbourhood(dict): A dictionary with neighbourhood
                                               names as keys and the
                                               corresponding counts of
                                               facilities as values
    Returns:
        Nothing

    Raises:
        TypeError: If facility_count_in_neighbourhood is not a dictionary
    """
    if not isinstance(facility_count_in_neighbourhood, dict):
        raise TypeError("facility_count_in_neighbourhood must be a "
                        "dictionary")

    labels = facility_count_in_neighbourhood.keys()
    sizes = facility_count_in_neighbourhood.values()
    plt.figure(figsize=(PIE_CHART_WIDTH, PIE_CHART_HEIGHT))
    plt.pie(sizes, labels=labels, autopct=AUTOPCT_FORMAT,
            startangle=PIE_CHART_START_ANGLE)
    plt.axis(AXIS_EQUAL)
    plt.title('Neighbourhood Facility Distribution')
    plt.show()


def display_parks_in_neighbourhood_map(parks_in_neighbourhood,
                                       center_latitude,
                                       center_longitude):
    """
    Purpose: generate and save an interactive map showing parks in a
             neighbourhood

    Parameters:
        parks_in_neighbourhood(list): A list of Park objects located within a
                                      specific neighbourhood
        center_latitude(float): The latitude around which the map will be
                                centered.
        center_longitude(float): The longitude around which the map will be
                                 centered.

    Returns:
        Nothing

    Raises:
        TypeError: If parks_in_neighbourhood is not a list of Park objects, or
                   if center_latitude or center_longitude are not floats
    """
    if not isinstance(parks_in_neighbourhood, list):
        raise TypeError("parks_in_neighbourhood must be a list")
    if not isinstance(center_latitude, float):
        raise TypeError("center_latitude must be a float")
    if not isinstance(center_longitude, float):
        raise TypeError("center_longitude must be a float")

    parks_map = folium.Map(location=(center_latitude, center_longitude),
                           zoom_start=ZOOM_LEVEL)
    for park in parks_in_neighbourhood:
        folium.Marker(location=(park.latitude, park.longitude),
                      popup=f"{park.name}",
                      tooltip=park.name).add_to(parks_map)
    parks_map.save("parks_in_neighbourhood_map.html")
    parks_map_path = os.path.abspath("parks_in_neighbourhood_map.html")
    webbrowser.open(f"file:///{parks_map_path}")
    print("View the map at: ./parks_in_neighbourhood_map.html\n")


def visualize_distance_between_park_and_center(park, center_latitude,
                                               center_longitude, distance):
    """
    Purpose: visualize the distance between a specified park and a
             neighborhood center on an interactive map

    Parameters:
        park(Park): A Park object
        center_latitude(float): A float representing the latitude of the
                                neighborhood center
        center_longitude(float): A float representing the longitude of the
                                 neighborhood center
        distance(float): A float representing the distance in kilometers
                         between the park and the neighborhood center

    Returns:
        Nothing

    Raises:
        TypeError: If park is not a Park object, or if center_latitude
                   center_longitude, or distance are not floats
        AttributeError: If the park object does not have 'latitude' or
                        'longitude' attributes
    """
    if not isinstance(park, Park):
        raise TypeError("park must be an instance of Park")
    if not isinstance(center_latitude, float):
        raise TypeError("center_latitude must be a float")
    if not isinstance(center_longitude, float):
        raise TypeError("center_longitude must be a float")
    if not isinstance(distance, float):
        raise TypeError("distance must be a float")
    if not hasattr(park, 'latitude') or not hasattr(park, 'longitude'):
        raise AttributeError("park must have 'latitude' and 'longitude' "
                             "attributes")

    distance_map = folium.Map(location=(park.latitude, park.longitude),
                              zoom_start=ZOOM_LEVEL)

    folium.Marker((park.latitude, park.longitude), popup=f"{park.name}",
                  icon=folium.Icon(color=PAKR_ICON_COLOUR)).add_to(
                      distance_map)

    folium.Marker(location=(center_latitude, center_longitude),
                  popup="Neighbourhood Center", icon=folium.Icon(
                      color=NEIGHBOURHOOD_CENTER_ICON_COLOUR)
                  ).add_to(distance_map)

    folium.PolyLine(((park.latitude, park.longitude), (center_latitude,
                                                       center_longitude)),
                    color=DISTANCE_LINE_COLOUR,
                    popup=f"Distance: {distance: .2f} km"
                    ).add_to(distance_map)

    distance_map.save("distance_map.html")
    distance_map_path = os.path.abspath("distance_map.html")
    webbrowser.open(f"file:///{distance_map_path}")
    print(f"The distance between {park.name} and the neighbourhood center is "
          f"{distance: .2f} km.")
    print("View it on the map at: ./distance_map.html\n")
