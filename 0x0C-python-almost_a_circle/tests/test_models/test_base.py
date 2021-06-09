#!/usr/bin/python3
"""
    Creating Class Testing
"""
from models.base import Base
import unittest
import os


class testing(unittest.TestCase):
    """
    Creating Edge Cases for test
    """

    def testing_pep8(self):
        """Testing pep8"""
        os.popen("pep8 base.py").read()
