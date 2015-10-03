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
    error_msg = 'Invalid input, please input Y / N only'

    diag_1 = raw_input('Is the car silent when you turn the key? (Y/N)')

    while not ((diag_1 == 'Y') or (diag_1 == 'N')):
        print(error_msg)
        diag_1 = raw_input('Is the car silent when you turn the key? (Y/N)')
    if diag_1 == 'Y':

        diag_2 = raw_input('Are the battery terminals corroded? (Y/N)')

        while not ((diag_2 == 'Y') or (diag_2 == 'N')):
            print(error_msg)
            diag_2 = raw_input('Are the battery terminals corroded? (Y/N)')
        if diag_2 == 'Y':
            print('Clean terminals and try starting again')
        if diag_2 == 'N':
            print('The battery cables may be damaged.Replace cables and try again')

    if diag_1 == 'N':

        diag_3 = raw_input('Does the car make a clicking noise? (Y/N)')

        while not ((diag_3 == 'Y') or (diag_3 == 'N')):
            print(error_msg)
            diag_3 = raw_input('Does the car make a clicking noise? (Y/N)')
        if diag_3 == 'Y':
            print('Replace the battery')
        if diag_3 == 'N':

            diag_4 = raw_input('Does the car crank up but fail to start? (Y/N)')

            while not ((diag_4 == 'Y') or (diag_4 == 'N')):
                print(error_msg)
                diag_4 = raw_input('Does the car crank up but fail to start? (Y/N)')
            if diag_4 == 'Y':
                print('Check spark plug connections.')
            if diag_4 == 'N':

                diag_5 = raw_input('Does the engine start and then die? (Y/N)')

                while not ((diag_5 == 'Y') or (diag_5 == 'N')):
                    print(error_msg)
                    diag_5 = raw_input('Does the engine start and then die? (Y/N)')
                if diag_5 == 'N':
                    print('Engine is not getting enough fuel. Clean fuel pump')
                if diag_5 == 'Y':

                    diag_6 = raw_input('Does your car have fuel injection? (Y/N)')

                    while not ((diag_6 == 'Y') or (diag_6 == 'N')):
                        print(error_msg)
                        diag_6 = raw_input('Does your car have fuel injection? (Y/N)')
                    if diag_6 == 'Y':
                        print('Get it in for service')
                    if diag_6 == 'N':
                        print('Check to ensure the choke is opening and closing.')



diagnose_car()