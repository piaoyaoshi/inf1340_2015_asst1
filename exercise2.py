#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

def name_that_shape():

    """
        This function accepts a number as input (between 3 and 10). Outputs the name of a shape that has that number of sides.

        A few test cases
        ----------------
        Input:Please enter the number of sides (only valid from 3 to 10):3
        Expected Output: Triangle

        Input:Please enter the number of sides (only valid from 3 to 10):10
        Expected Output: Decagon

        Input:Please enter the number of sides (only valid from 3 to 10):20
        Expected Output: Error

        Input:Please enter the number of sides (only valid from 3 to 10):1
        Expected Output: Error

        Input:Please enter the number of sides (only valid from 3 to 10):3.0
        Expected Output: Error

        Input:Please enter the number of sides (only valid from 3 to 10):
        Expected Output: Error

        Input:Please enter the number of sides (only valid from 3 to 10):three
        Expected Output: Error

        Input:Please enter the number of sides (only valid from 3 to 10):*&%
        Expected Output: Error

        Input:Please enter the number of sides (only valid from 3 to 10):3 ok
        Expected Output: Error

        This is the dictionary containing key value pairs
    """
    dictionary = {
        '3': 'triangle',
        '4': 'quadrilateral',
        '5': 'pentagon',
        '6': 'hexagon',
        '7': 'heptagon',
        '8': 'octagon',
        '9': 'nonagon',
        '10': 'decagon'
    }

    # This code asks for user input of number of sides

    number_of_sides = raw_input("Please enter the number of sides (only valid from 3 to 10):")

    # This code assess if the entered number is a key in the dictionary and if so prints the value

    if number_of_sides in dict.keys():
        print(dictionary[number_of_sides])
    else:
        print("Error")


    #name_that_shape()