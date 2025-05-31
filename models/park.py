#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Youcheng Zhang
CS 5001, Spring 2024
Final Project - Models: park class file
"""

MIN_LATITUDE_DEGREE = -90
MAX_LATITUDE_DEGREE = 90
MIN_LONGITUDE_DEGREE = -180
MAX_LONGITUDE_DEGREE = 180


class Park:
    """
    Represents a park in Vancouver with specific attributes

    Attributes:
        id(str)): The ID of the park
        name(str): The name of the park
        special_features(str): Indicates whether the park has special features.
                               'Y' means the park has special features, and
                               'N' means it does not
        facilities(str): Indicates whether the park has facilities. 'Y' means
                         the park has facilities, and 'N' means it does not
        washrooms(str): Indicates whether the park has washrooms. 'Y' means
                        the park has washrooms, and 'N' means it does not
        street_location(str): The street location of the park
        neighbourhood(str): The neighbourhood where the park is located
        latitude(float): The latitude of the park
        longitude(float): The longitude of the park

    Methods:
        __init__(self, park_id, park_name, special_features, facilities,
                 washrooms, street_location, neighbourhood): Initializes a new
                                                             instance of the
                                                             class
        __str(self): Creates a string representation of the Park
        matches_special_features(self, special_features): Determines whether
                                                          the park has special
                                                          features as
                                                          specified
        matches_facilities(self, facilities): Determines whether the park has
                                              facilities as specified
        matches_washrooms(self, washrooms): Determines whether the park has
                                            washrooms as specified
    """

    def __init__(self, park_id, park_name, special_features, facilities,
                 washrooms, street_location, neighbourhood, latitude,
                 longitude):
        """
        Purpose: initialize a new instance of the Park class with the
                 specified details

        Parameters:
            park_id(str)): The ID of the park
            park_name(str): The name of the park
            special_features(str): Indicates whether the park has special
                                   features. 'Y' means the park has special
                                   features, and 'N' means it does not
            facilities(str): Indicates whether the park has facilities. 'Y'
                             means the park has facilities, and 'N' means it
                             does not
            washrooms(str): Indicates whether the park has washrooms. 'Y'
                            means the park has washrooms, and 'N' means it
                            does not
            street_location(str): The street location of the park
            neighbourhood(str): The neighbourhood where the park is located
            latitude(float): The latitude of the park
            longitude(float): The longitude of the park

        Returns:
            Nothing

        Raises:
            TypeError: If any of the parameters are not of their expected type
            ValueError:  If latitude and longitude are not within valid
                        ranges
        """
        for argument in [park_id, park_name, special_features, facilities,
                         washrooms, street_location, neighbourhood]:
            if not isinstance(argument, str):
                raise TypeError("String arguments must be of type string")
        for argument in [latitude, longitude]:
            if not isinstance(argument, float):
                raise TypeError("Latitude and longitude must be of type float")
        for argument in [special_features, facilities, washrooms]:
            if argument not in ['Y', 'N']:
                raise TypeError(f"{argument} must be string 'Y' or 'N'")
        if not MIN_LATITUDE_DEGREE <= latitude <= MAX_LATITUDE_DEGREE:
            raise ValueError("Latitude must be between -90 and 90 degrees")
        if not MIN_LONGITUDE_DEGREE <= longitude <= MAX_LONGITUDE_DEGREE:
            raise ValueError("Longitude must be between -180 and 180 degrees")

        self.id = park_id
        self.name = park_name
        self.special_features = special_features
        self.facilities = facilities
        self.washrooms = washrooms
        self.street_location = street_location
        self.neighbourhood = neighbourhood
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        """
        Purpose: create a string representation of the Park

        Parameters:
            Nothing

        Returns:
            A string, representation of the park

        Raises:
            Nothing
        """
        park_info = (
            f"\n{self.name}\n(ID: {self.id}, Special Features: "
            f"{self.special_features}, Facilities: {self. facilities}, "
            f"Washrooms: {self.washrooms}, Street Location: "
            f"{self.street_location}, Neighbourhood: {self.neighbourhood})")
        return park_info

    def matches_special_features(self, special_features):
        """
        Purpose: determine whether the park has special features as specified

        Parameters:
            special_features(str): A 'Y' or 'N' string indicating whether to
                                  check for the presence ('Y') or absence
                                  ('N') of special features in the park

        Returns:
            A boolean, True if the park's special features match the specified
            criteria, False otherwise

        Raises:
            ValueError: If special_features is not 'Y' or 'N'
        """
        if special_features not in ['Y', 'N']:
            raise ValueError("special_features must be 'Y' or 'N'")

        if self.special_features == special_features:
            return True
        else:
            return False

    def matches_facilities(self, facilities):
        """
        Purpose: determine whether the park has facilities as specified

        Parameters:
            facilities(str): A 'Y' or 'N' string indicating whether to check
                           for the presence ('Y') or absence（'N') of
                           facilities in the park

        Returns:
            A boolean, True if the park's facilities match the specified
            criteria, False otherwise

        Raises:
            ValueError: If facilities is not 'Y' or 'N'
        """
        if facilities not in ['Y', 'N']:
            raise ValueError("facilities must be 'Y' or 'N'")

        if self.facilities == facilities:
            return True
        else:
            return False

    def matches_washrooms(self, washrooms):
        """
        Purpose: determine whether the park has washrooms as specified

        Parameters:
            facilities(str): A 'Y' or 'N' string indicating whether to check
                           for the presence ('Y') or absence（'N') of
                           washrooms in the park

        Returns:
            A boolean, True if the park's washrooms match the specified
            criteria, False otherwise

        Raises:
            ValueError: If washrooms is not 'Y' or 'N'
        """
        if washrooms not in ['Y', 'N']:
            raise ValueError("washrooms must be 'Y' or 'N'")

        if self.washrooms == washrooms:
            return True
        else:
            return False
