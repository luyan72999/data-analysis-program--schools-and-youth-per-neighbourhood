'''
CS 5001 Fall 2022 Lu YAN
Milestone 2
this file contains the test suite of all the funstions in data_processing.py
'''

import unittest
from data_processing import *
import requests
from requests.exceptions import HTTPError
from requests.exceptions import ConnectionError
from School import School
from Neighbourhood import Neighbourhood
from constants import *

class TestDataProcessing(unittest.TestCase):

    def test_download_csv(self):
        '''
        Function: test_download_csv
        Test whether the download_csv() function works properly
        Test whether the value errors are properly raised
        '''
        with self.assertRaises(ValueError):
            download_csv(1)
        
        self.assertTrue(isinstance(download_csv(URL_SCHOOL),str))

    def test_clean_and_parse_schools_into_objects(self):
        '''
        Function: test_clean_and_parse_schools_into_objects
        Test whether the clean_and_parse_schools_into_objects() function works properly
        Test whether the value errors are properly raised
        '''
        with self.assertRaises(ValueError):
            clean_and_parse_schools_into_objects(1)
        
        content = download_csv(URL_SCHOOL)
        school_list = clean_and_parse_schools_into_objects(content)
        self.assertEqual(len(school_list),194)
        for object in school_list:
            self.assertTrue(isinstance(object,School))
    
    def test_clean_and_parse_people_into_objects(self):
        '''
        Function: test_clean_and_parse_people_into_objects
        Test whether the clean_and_parse_people_into_objects() function works properly
        Test whether the value errors are properly raised
        '''
        with self.assertRaises(ValueError):
            clean_and_parse_people_into_objects(1)
        
        content = download_csv(URL_PEOPLE)
        neighbourhood_list = clean_and_parse_people_into_objects(content)
        self.assertEqual(len(neighbourhood_list),22)
        for object in neighbourhood_list:
            self.assertTrue(isinstance(object,Neighbourhood))
    
    def test_add_school_to_neighbourhood(self):
        '''
        Function: test_add_school_to_neighbourhood
        Test whether the add_school_to_neighbourhood() function works properly
        Test whether the value errors are properly raised
        '''
        with self.assertRaises(ValueError):
            add_school_to_neighbourhood(1,[1])
        with self.assertRaises(ValueError):
            add_school_to_neighbourhood([1],1)
        with self.assertRaises(ValueError):
            add_school_to_neighbourhood([],[1])
        with self.assertRaises(ValueError):
            add_school_to_neighbourhood([1],[])
        
        school_list = clean_and_parse_schools_into_objects(download_csv(URL_SCHOOL))
        neighbourhood_list = clean_and_parse_people_into_objects(download_csv(URL_PEOPLE))
        add_school_to_neighbourhood(school_list,neighbourhood_list)
        for object in neighbourhood_list:
            self.assertNotEqual(len(object.schools),0)

unittest.main()