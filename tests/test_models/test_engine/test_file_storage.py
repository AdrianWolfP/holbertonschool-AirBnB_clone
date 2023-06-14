#!/usr/bin/python3
""" Test file_storage module """

import unittest
from models import BaseModel
from Models import storage
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """ Class to test file storage engine an the method """

    def setUp(self):
        """ Method is called before setting up
        each case is run """
        # Create a new FileStorage object before each test
        self.test_object = BaseModel()
<<<<<<< HEAD
=======
        
>>>>>>> f316a631296f42a2d78156d9c26119fa1cae2e76
