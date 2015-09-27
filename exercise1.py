#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

money = 0

def stock_ticker(money):
    #Variables needed for the program
    share_cost = 900.00
    shares = 2000
    commission_rate = 3.00 / 100.00

    #This will calculate the amount paid for the stocks
    total_holdings = shares * share_cost
    commission = total_holdings * commission_rate
    money = money - (total_holdings - commission)

    #This will calculate how much the stocks were sold for and they money made
    share_cost = 942.75
    total_holdings = shares * share_cost
    commission = total_holdings * commission_rate
    money = money + (total_holdings - commission)
    print money

stock_ticker(money)