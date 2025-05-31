#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Youcheng Zhang
CS 5001, Spring 2024
Final Project - Controller: driver file
"""
import requests
from controller_helper import run_program


def main():

    try:
        run_program()

    except requests.exceptions.HTTPError as he:
        print(f"\nHTTPError see details below:\n {he}")

    except requests.exceptions.ConnectionError as ce:
        print(f"\nConnectionError see details below:\n{ce}")

    except ValueError as ve:
        print(f"\nValueError see details below:\n{ve}")

    except TypeError as te:
        print(f"\nTypeError see details below:\n{te}")

    except ZeroDivisionError as ze:
        print(f"\nZeroDivisionError see details below:\n{ze}")

    except AttributeError as ae:
        print(f"\nAttributeError see details below:\n{ae}")


if __name__ == "__main__":
    main()
