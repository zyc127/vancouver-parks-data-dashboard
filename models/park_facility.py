#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Youcheng Zhang
CS 5001, Spring 2024
Final Project - Models: park facility class file
"""

MIN_COUNT = 0
NO_PARKS = 0


class ParkFacility:
    """
    Represents a park facility in Vancouver with specific attributes

    Attributes:
        type(str): The type of the park facility
        parks(list): The list of parks which have the facility
        count(int): The number of park facility in Vancouver

    Methods:
      __init__(self, facility_type, parks_with_facility, facility_count):
          Initializes a new instance of the class
      __str(self): Creates a string representation of the ParkFacility
      count_parks_with_facility(self): Gets the number of parks with the
                                       facility
      calculate_facility_to_park_ratio(self): Calculates the facility to park
                                              ratio
    """

    def __init__(self, facility_type, parks_with_facility, facility_count):
        """
        Purpose: initialize a new instance of the ParkFacility class with the
                 specified details

        Parameters:
            facility_type(str): The type of the park facility
            parks_with_facility(list): The list of parks which have the
                                       facility
            facility_count(int): The number of park facility in Vancouver

        Returns:
            Nothing

        Raises:
            TypeError: If any of the parameters are not of their expected type
            ValueError: If the facility_count is negative
        """
        if not isinstance(facility_type, str):
            raise TypeError("facility_type must be a string")
        if not isinstance(parks_with_facility, list):
            raise TypeError("parks_with_facility must be a list")
        if not isinstance(facility_count, int):
            raise TypeError("facility_count must be an integer")
        if facility_count < MIN_COUNT:
            raise ValueError("facility_count must be a positive integer")

        self.type = facility_type
        self.parks = parks_with_facility
        self.count = facility_count

    def __str__(self):
        """
        Purpose: create a string representation of the ParkFacility

        Parameters:
            Nothing

        Returns:
            A string, representation of the park

        Raises:
            Nothing
        """
        parks_str = ', '.join(self.parks)

        park_facility_info = (f"\nFacility Type: {self.type}\n"
                              f"Number of Facilities: {self.count}\n"
                              f"Parks with this Facility: {parks_str}")

        return park_facility_info

    def count_parks_with_facility(self):
        """
        Purpose: get the number of parks with the facility

        Parameters:
            Nothing

        Returns:
            An int, number of parks with the facility

        Raises:
            Nothing
        """
        count_parks = len(self.parks)
        return count_parks

    def calculate_facility_to_park_ratio(self):
        """
        Purpose: calculate and return the facility to park ratio which
                 represents the accessibility of facilities across parks

        Parameters:
            Nothing

        Returns:
            A float, facility to park ratio

        Raises:
            ZeroDivisionError: If there are no parks to calculate the ratio,
                               preventing division by zero
        """
        count_parks = self.count_parks_with_facility()
        if count_parks == NO_PARKS:
            raise ZeroDivisionError("Cannot calculate ratio with zero parks")
        facility_to_park_ratio = self.count / count_parks
        return facility_to_park_ratio
