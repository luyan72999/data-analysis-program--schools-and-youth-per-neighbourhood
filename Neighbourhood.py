'''
CS 5001 Fall 2022 Lu YAN
Final project
Milestone 1
This is the file for class Neighbourhood
'''
from School import School

class Neighbourhood:
    def __init__(self,name,five_to_nine,ten_to_fourteen,fifteen_to_nineteen):
        '''
        Function: __init__
        constructor function to initialize an instance
        Parameters: 
        1 string: name of the neighbourhood
        3 integers: number of students between five to nine, ten to fourteen and fifteen to nineteen
        Returns nothing
            
        Possible Errors: ValueError
        '''
        if not isinstance(name,str):
            raise ValueError("Parameter 'name' must be string.")
        if not isinstance(five_to_nine,int) or not isinstance(ten_to_fourteen,int) or not isinstance(fifteen_to_nineteen,int):
            raise ValueError("Parameter 'five_to_nine','ten_to_fifteen' and 'fifteen_to_nineteen' must be integers.")
        if len(name.strip()) == 0 or len(str(five_to_nine).strip()) == 0 or len(str(ten_to_fourteen).strip()) == 0 or len(str(fifteen_to_nineteen).strip()) == 0:
            raise ValueError("Parameter 'name', 'five_to_nine','ten_to_fifteen' and 'fifteen_to_nineteen' cannot be empty.")

        self.name = name
        self.schools = []
        self.students_five_to_nine = five_to_nine
        self.students_ten_to_fourteen = ten_to_fourteen
        self.students_fifteen_to_nineteen = fifteen_to_nineteen

    def add_school(self,school):
        '''
        Function: add_school
        add a school object into the attribute 'schools' 
        Parameters: a object of School
        Return nothing
        Possible errors: ValueError
        '''
        if not isinstance(school,School):
            raise ValueError("Parameter must be an instance of Schoool.")
        self.schools.append(school)

    def calculate_school_number(self):
        '''
        Function: calculate_school_number
        calculate the number of schools by the length of schools list
        Parameters: nothing
        Returns an integer: number of schools
        '''
        school_number = len(self.schools)
        return school_number
    
    def calculate_student_number(self):
        '''
        Function: calculate_student_number
        calculate the number of students by adding three attributes together
        Parameters: nothing
        Returns an integer: number of students
        '''
        student_number = self.students_five_to_nine + self.students_ten_to_fourteen + self.students_fifteen_to_nineteen
        return student_number

    def calculate_students_per_school(self):
        '''
        Function: calculate_students_per_school
        calculate the ratio of students per school
        Parameters: nothing
        Returns an integer, the rounded quotient of number of students divided by number of schools

        Possible errors: ZeroDivisionError
        '''
        number_of_schools = self.calculate_school_number()
        number_of_students = self.calculate_student_number()
        if number_of_schools != 0:
            ratio_students_per_school = round(number_of_students / number_of_schools)
            return ratio_students_per_school
        else:
            raise ZeroDivisionError("Denominator 'number of schools' cannot be zero.")
    
    def __eq__(self,other):
        '''
        Function: __eq__
        Determine the 2 instances are equal by their values
        Parameters: other instance of Neighbourhood
        Returns a boolean
        '''
        if not isinstance(other,Neighbourhood):
            raise ValueError("Parameter must be an object of Neighbourhood.")
        if self.name == other.name:
            return True
        else:
            return False
    
    def __str__(self):
        '''
        Function: __str__
        Returns a string which is the string representation of the neighbourhood name
        Parameters: nothing
        Returns a string
        '''
        message = self.name
        return message
    
    

        