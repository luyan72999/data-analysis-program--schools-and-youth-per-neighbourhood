'''
CS 5001 Fall 2022 Lu YAN
Final project
Milestone 2
This is the file for testing class School
'''

import unittest
from School import School

class TestSchool(unittest.TestCase):
    
    def test_init(self):
        '''
        Function: test_init
        test whether the __init__() function of class School works properly
        test whether value errors are properly raised
        '''
        school = School("Fraser Academy","Independant School","Kitsilano")
        self.assertEqual(school.name,"Fraser Academy","School name attribute not properly assigned.")
        self.assertEqual(school.type,"Independant School","School type attribute not properly assigned.")
        self.assertEqual(school.neighbourhood,"Kitsilano","School neighbourhood attribute not properly assigned.")

        with self.assertRaises(ValueError):
            school_2 = School(5,"Independant School","Kitsilano")
        with self.assertRaises(ValueError):
            school_3 = School("Fraser Academy",True,"Kitsilano")
        with self.assertRaises(ValueError):
            school_4 = School("Fraser Academy","Independant School",5.25)
        with self.assertRaises(ValueError):
            school_5 = School("","Independant School","Kitsilano")
        with self.assertRaises(ValueError):
            school_6 = School("Fraser Academy"," ","Kitsilano")
        with self.assertRaises(ValueError):
            school_7 = School("Fraser Academy","Independant School","  ")

    def test_eq(self):
        '''
        Function: test_eq
        test whether the __eq__() function of class School works properly
        test whether value errors are properly raised
        '''
        school = School("Fraser Academy","Independant School","Kitsilano")
        school_2 = School("Fraser Academy","Independant","Kit")
        school_3 = School("Vancouver Learning Network","Independant School","Kitsilano")
        self.assertEqual(school,school_2,"Two school objects are not equal.")
        self.assertNotEqual(school,school_3,"Two inequal school objects are equal.")

        school_4 = "Fraser Academey"
        with self.assertRaises(ValueError):
            school == school_4
    
    def test_str(self):
        '''
        Function: test_str
        test whether the __str__() function of class School works properly
        '''
        school = School("Fraser Academy","Independant School","Kitsilano")
        self.assertEqual(str(school),"Fraser Academy")

unittest.main()
    