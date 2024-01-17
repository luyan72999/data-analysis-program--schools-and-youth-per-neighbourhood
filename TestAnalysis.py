'''
CS 5001 Fall 2022 Lu YAN
Final project
Milestone 2
This file contains the test suite for analysis.py
'''
import unittest
from analysis import *
from data_processing import *
from School import School
from Neighbourhood import Neighbourhood
from constants import *

class TestAnalysis(unittest.TestCase):
    
    def setUp(self):
        '''
        Function: setUp
        prepare the data that will be repeatedly used in TestNeighbourhood class
        '''
        self.neighbourhood_list = clean_and_parse_people_into_objects(download_csv(URL_PEOPLE))
        self.school_list = clean_and_parse_schools_into_objects(download_csv(URL_SCHOOL))
        add_school_to_neighbourhood(self.school_list,self.neighbourhood_list)
    
    def test_get_school_number(self):
        '''
        Function: test_get_school_number
        test whether the get_school_number() function works properly
        '''
        self.assertEqual(get_school_number(self.neighbourhood_list[0]),len(self.neighbourhood_list[0].schools))

    def test_sort_neighbourhood_by_schools(self):
        '''
        Function: test_sort_neighbourhood_by_schools
        test whether the sort_neighbourhood_by_schools() function works properly
        test whether value errors are properly raised
        '''
        with self.assertRaises(ValueError):
            sort_neighbourhood_by_schools("schools")
        with self.assertRaises(ValueError):
            sort_neighbourhood_by_schools([])
            
        sorted_list = sort_neighbourhood_by_schools(self.neighbourhood_list)
        i = 1
        while i < len(sorted_list):
            j = i - 1
            self.assertTrue(sorted_list[j].calculate_school_number() >= sorted_list[i].calculate_school_number())
            i += 1

    def test_analyze_school(self):
        '''
        Function: test_analyze_school
        test whether the analyze_school() function works properly
        test whether value errors are properly raised
        '''
        with self.assertRaises(ValueError):
            analyze_school("1")
        with self.assertRaises(ValueError):
            analyze_school([])

        sorted_list = sort_neighbourhood_by_schools(self.neighbourhood_list)
        name_list, school_number_list = analyze_school(sorted_list)
        self.assertTrue(isinstance(name_list,list))
        for item in name_list:
            self.assertTrue(isinstance(item,str))
        
        self.assertTrue(isinstance(school_number_list,list))
        for item in school_number_list:
            self.assertTrue(isinstance(item,int))
        
    def test_analyze_student(self):
        '''
        Function: test_analyze_student
        test whether the analyze_student() function works properly
        test whether value errors are properly raised
        '''
        with self.assertRaises(ValueError):
            analyze_student("1")
        with self.assertRaises(ValueError):
            analyze_student([])
        
        sorted_list = sort_neighbourhood_by_schools(self.neighbourhood_list)
        name_list, student_number_list = analyze_school(sorted_list)
        self.assertTrue(isinstance(name_list,list))
        for item in name_list:
            self.assertTrue(isinstance(item,str))
        
        self.assertTrue(isinstance(student_number_list,list))
        for item in student_number_list:
            self.assertTrue(isinstance(item,int))
    
    def test_analyze_ratio(self):
        '''
        Function: test_analyze_ratio
        test whether the analyze_ratio() function works properly
        test whether value errors are properly raised
        '''
        with self.assertRaises(ValueError):
            analyze_ratio("1")
        with self.assertRaises(ValueError):
            analyze_ratio([])

        sorted_list = sort_neighbourhood_by_schools(self.neighbourhood_list)
        name_list, ratio_number_list = analyze_school(sorted_list)
        self.assertTrue(isinstance(name_list,list))
        for item in name_list:
            self.assertTrue(isinstance(item,str))
        
        self.assertTrue(isinstance(ratio_number_list,list))
        for item in ratio_number_list:
            self.assertTrue(isinstance(item,int))

    def test_calculate_school_average_and_store_in_list(self):
        '''
        Function: test_calculate_school_average_and_store_in_list
        test whether the calculate_school_average_and_store_in_list() function works properly
        test whether value errors are properly raised
        '''
        with self.assertRaises(ValueError):
            calculate_school_average_and_store_in_list("1")
        with self.assertRaises(ValueError):
            calculate_school_average_and_store_in_list([])
        
        self.assertEqual(calculate_school_average_and_store_in_list(self.neighbourhood_list),[9]*22)

    def test_calculate_student_average_and_store_in_list(self):
        '''
        Function: test_calculate_student_average_and_store_in_list
        test whether the calculate_student_average_and_store_in_list() function works properly
        test whether value errors are properly raised
        '''
        with self.assertRaises(ValueError):
            calculate_school_average_and_store_in_list("1")
        with self.assertRaises(ValueError):
            calculate_school_average_and_store_in_list([])

        self.assertEqual(calculate_student_average_and_store_in_list(self.neighbourhood_list),[3453]*22)
    
    def test_calculate_ratio_average_and_store_in_list(self):
        '''
        Function: test_ratio_average_and_store_in_list
        test whether the ratio_average_and_store_in_list() function works properly
        test whether value errors are properly raised
        '''
        with self.assertRaises(ValueError):
            calculate_school_average_and_store_in_list("1")
        with self.assertRaises(ValueError):
            calculate_school_average_and_store_in_list([])
        
        self.assertEqual(calculate_ratio_average_and_store_in_list(self.neighbourhood_list),[416]*22)
        
    def test_find_neighbourhood(self):
        '''
        Function: test_find_neighbourhood
        test whether the find_neighbourhood() function works properly
        test whether value errors are properly raised
        '''
        with self.assertRaises(ValueError):
            find_neighbourhood(1,[1])
        with self.assertRaises(ValueError):
            find_neighbourhood("1",1)
        with self.assertRaises(ValueError):
            find_neighbourhood("1",[])
        
        self.assertEqual(find_neighbourhood("Downtown",self.neighbourhood_list),self.neighbourhood_list[1])

    def test_find_school(self):
        '''
        Function: test_find_school
        test whether the find_school() function works properly
        test whether value errors are properly raised
        '''
        with self.assertRaises(ValueError):
            find_school(1,[1])
        with self.assertRaises(ValueError):
            find_school("1",1)
        with self.assertRaises(ValueError):
            find_school("1",[])
        
        self.assertEqual(find_school("Alexander Academy",self.school_list),self.school_list[0])
        
unittest.main()