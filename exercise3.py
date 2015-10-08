#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:y,n,yes,no

    Expected Outputs:

    Errors:

    """
    error = 'I don\'t understand'
    # This function is the first box in the flow chart

    def check_silence():
        silent = raw_input("Is the car silent when you turn the key?")
        if silent == "y":
            check_battery()
        elif silent == "n":
            check_noise()
        else:
            print (error)
            check_silence()

    # This is the left side of the flowchart
    def check_battery():
        corroded = raw_input("Are the battery terminals corroded?")
        if corroded == "y":
            print ("Clean terminals and try starting again.")
            exit()
        elif corroded == "n":
            print ("Replace cables and try again")
            exit()
        else:
            print (error)
            check_battery()

    # Everything below is the right side of the flow chart
    def check_noise():
        click = raw_input("Does the car make a clicking noise?")
        if click == "y":
            print ("Replace the battery")
            exit()
        elif click == "n":
            check_crank()
        else:
            print (error)
            check_noise()

    def check_crank():
        crank = raw_input("Does the car crank up but fail to start?")
        if crank == "y":
            print ("Check spark plug connections.")
            exit()
        elif crank == "n":
            check_engine()
        else:
            print (error)
            check_crank()

    def check_engine():
        engine = raw_input("Does engine start and then die?")
        if engine == "y":
            check_fuel()
        elif engine == "n":
            print ("Engine is not getting enough fuel. Clean fuel pump")
            exit()
        else:
            print (error)
            check_engine()

    def check_fuel():
        fuel = raw_input("Does your car have fuel injection?")
        if fuel == "n":
            print ("Check to ensure the choke is opening and closing")
            exit()
        elif fuel == "y":
            print ("Get it in for service")
            exit()
        else:
            print (error)
            check_fuel()

    check_silence()

diagnose_car()


