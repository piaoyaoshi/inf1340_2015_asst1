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

    Inputs:

    Expected Outputs:

    Errors:

    """
    def silent_fun():
        silent = raw_input("Is the car silent when you turn the key?")
        if silent == "y" or silent.lower() == "yes":
            corroded_fun()
        if silent == "n"or silent.lower() == "no":
            click_fun()
        if silent != "y" or "yes" or "n" or "no":
            print ("I don't understand")
            silent_fun()

    # This is the left side of the flowchart
    def corroded_fun():
        corroded = raw_input("Are the battery terminals corroded?")
        if corroded == "y" or corroded.lower() == "yes":
            print ("Clean terminals and try starting again.")
            exit()
        if corroded == "n" or corroded.lower() == "no":
            print ("Replace cables and try again")
            exit()
        if corroded != "y" or "yes" or "n" or "no":
            print ("I don't understand")
            corroded_fun()

    # Everything below is the right side of the flow chart
    def click_fun():
        click = raw_input("Does the car make a clicking noise?")
        if click == "y" or click.lower() == "yes":
            print ("Replace the battery")
            exit()
        if click == "n" or click.lower() == "no":
            crank_fun()
        if click != "y" or "yes" or "n" or "no":
            print ("I don't understand")
            click_fun()

    def crank_fun():
        crank = raw_input("Does the car crank up but fail to start?")
        if crank == "y" or crank.lower() == "yes":
            print ("Check spark plug connections.")
            exit()
        if crank == "n" or crank.lower() == "no":
            engine_fun()
        if crank != "y" or "yes" or "n" or "no":
            print ("I don't understand")
            crank_fun()

    def engine_fun():
        engine = raw_input("Does engine start and then die?")
        if engine == "y" or engine.lower() == "yes":
            fuel_fun()
        if engine == "n" or engine.lower() == "no":
            print ("The battery cables may be damaged. Replace cables and try again.")
            exit()
        if engine != "y" or "yes" or "n" or "no":
            print ("I don't understand")
            engine_fun()

    def fuel_fun():
        fuel = raw_input("Does your car have fuel injection?")
        if fuel == "n" or fuel.lower() == "no":
            print ("Check to ensure the choke is opening and closing")
            exit()
        if fuel == "y" or fuel.lower() == "yes":
            print ("Get it in for service")
            exit()
        if fuel != "y" or "yes" or "n" or "no":
            print ("I don't understand")
            fuel_fun()

    silent_fun()

diagnose_car()