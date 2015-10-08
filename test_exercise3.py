#!/usr/bin/env python

""" Module to test exercise3.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

import pytest
import mock
from exercise3_solution import diagnose_car


def test_accepted_inputs(capsys):

    with mock.patch("__builtin__.raw_input", side_effect=["Y", "Y"]):
        diagnose_car()
        out, err = capsys.readouterr()
        assert out == "Clean terminals and try starting again.\n"

    with mock.patch("__builtin__.raw_input", side_effect=["Y", "N"]):
        diagnose_car()
        out, err = capsys.readouterr()
        assert out == "Replace cables and try again.\n"

    with mock.patch("__builtin__.raw_input", side_effect=["N", "Y"]):
        diagnose_car()
        out, err = capsys.readouterr()
        assert out == "Replace the battery.\n"

    with mock.patch("__builtin__.raw_input", side_effect=["N", "N", "Y"]):
        diagnose_car()
        out, err = capsys.readouterr()
        assert out == "Check spark plug connections.\n"

    with mock.patch("__builtin__.raw_input", side_effect=["N", "N", "N", "N"]):
        diagnose_car()
        out, err = capsys.readouterr()
        assert out == "Engine is not getting enough fuel. Clean fuel pump.\n"

    with mock.patch("__builtin__.raw_input", side_effect=["N", "N", "N", "Y", "N"]):
        diagnose_car()
        out, err = capsys.readouterr()
        assert out == "Check to ensure the choke is opening and closing.\n"

    with mock.patch("__builtin__.raw_input", side_effect=["N", "N", "N", "Y", "Y"]):
        diagnose_car()
        out, err = capsys.readouterr()
        assert out == "Get it in for service.\n"