'''
CS 5001 Fall 2022 Lu YAN
Final project
Milestone 2
This is the file for testing class Neighbourhood
'''

import unittest
from Neighbourhood import Neighbourhood
from School import School

class TestNeighbourhood(unittest.TestCase):

    def setUp(self):
        '''
        Function: setUp
        create the objects that will be repeatedly used in TestNeighbourhood class
        '''
        self.neighbourhood = Neighbourhood("Downtown",1,2,3)
        self.school = School("Fraser Academy","Independant School","Kitsilano")

    def test_init(self):
        '''
        Function: test_init
        test whether the __init__() function of class Neighbourhood works properly
        test whether value errors are properly raised
        '''
        self.assertEqual(self.neighbourhood.name,"Downtown")
        self.assertEqual(self.neighbourhood.students_five_to_nine,1)
        self.assertEqual(self.neighbourhood.students_ten_to_fourteen,2)
        self.assertEqual(self.neighbourhood.students_fifteen_to_nineteen,3)

        with self.assertRaises(ValueError):
            neighbourhood_2 = Neighbourhood(0,1,2,3)
        with self.assertRaises(ValueError):
            neighbourhood_3 = Neighbourhood("Downtown","1",2,3)
        with self.assertRaises(ValueError):    
            neighbourhood_4 = Neighbourhood("Downtown",1,"2",3)
        with self.assertRaises(ValueError):
            neighbourhood_5 = Neighbourhood("Downtown",1,2,"3")
        with self.assertRaises(ValueError):    
            neighbourhood_6 = Neighbourhood("",1,2,3)
        with self.assertRaises(ValueError):
            neighbourhood_7 = Neighbourhood("Downtown"," ",2,3)
        with self.assertRaises(ValueError):    
            neighbourhood_8 = Neighbourhood("Downtown",1,"  ",3)
        with self.assertRaises(ValueError):
            neighbourhood_9 = Neighbourhood("Downtown",1,2,"   ")
    
    def test_add_school(self):
        '''
        Function: test_add_school
        test whether the add_school function of class Neighbourhood works properly
        test whether value errors are properly raised
        '''
        self.neighbourhood.add_school(self.school)
        self.assertEqual(self.neighbourhood.schools,[self.school])

        neighbourhood_2 = Neighbourhood("Sunset",1,2,3)
        with self.assertRaises(ValueError):
            self.neighbourhood.add_school(neighbourhood_2)
    
    def test_calulate_school_number(self):
        '''
        Function: test_calulate_school_number
        test whether the calulate_school_number function of class Neighbourhood works properly
        '''
        self.neighbourhood.add_school(self.school)
        self.assertEqual(self.neighbourhood.calculate_school_number(),1)
    
    def test_calculate_student_number(self):
        '''
        Function: test_calulate_student_number
        test whether the calulate_student_number function of class Neighbourhood works properly
        '''
        self.assertEqual(self.neighbourhood.calculate_student_number(),6)
    
    def test_calculate_students_per_school(self):
        '''
        Function: test_calculate_students_per_school
        test whether the calculate_students_per_school( function of class Neighbourhood works properly
        test whether zero division errors are properly raised
        '''
        with self.assertRaises(ZeroDivisionError):
            self.neighbourhood.calculate_students_per_school()
        
        self.neighbourhood.add_school(self.school)
        self.assertEqual(self.neighbourhood.calculate_students_per_school(),6)

    def test_eq(self):
        '''
        Function: test_eq
        test whether the __eq__() function of class School works properly
        test whether value errors are properly raised
        '''
        neighbourhood_2 = Neighbourhood("Downtown",4,5,6)
        neighbourhood_3 = Neighbourhood("Sunset",1,2,3)

        self.assertEqual(self.neighbourhood,neighbourhood_2)
        self.assertNotEqual(self.neighbourhood,neighbourhood_3)

        neighbourhood_4 = "Downtown"
        with self.assertRaises(ValueError):
            self.neighbourhood == neighbourhood_4

    def test_str(self):
        '''
        Function: test_str
        test whether the __str__() function of class School works properly
        '''
        self.assertEqual(str(self.neighbourhood),"Downtown")

unittest.main()