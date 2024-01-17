'''
CS 5001 Fall 2022 Lu YAN
Final project
Milestone 2
This is the file for class School
'''

class School:
    def __init__(self,name,school_type,neighbourhood):
        '''
        Function: __init__
        constructor function to initialize an instance
        Parameters: 3 strings,school name, school type, and neighbourhood the school belongs to
        Returns nothing
        
        Possible Errors: ValueError
        '''
        if not isinstance(name,str) or not isinstance(school_type,str) or not isinstance(neighbourhood,str):
            raise ValueError("Parameters 'name','type','neighbourhood' must be string.")
        if len(name.strip()) == 0 or len(school_type.strip()) == 0 or len(neighbourhood.strip()) == 0:
            raise ValueError("Parameters 'name','type','neighbourhood' cannot be empty.")
        self.name = name
        self.type = school_type
        self.neighbourhood = neighbourhood
    
    def __eq__(self,other):
        '''
        Function: __eq__
        Determine the 2 instances are equal by their values
        Parameters: other instance of School
        Returns a boolean
        '''
        if not isinstance(other,School):
            raise ValueError("Parameter must be an object of School.")
        if self.name == other.name:
            return True
        else:
            return False

    def __str__(self):
        '''
        Function: __str__
        Returns a string which is the string representation of the school name
        Parameters: nothing
        Returns a string
        '''
        message = self.name
        return message
    
        
