'''
CS 5001 Fall 2022 Lu YAN
Final project
Milestone 2
analysis: this file contains all the functions for data analysis
'''

def get_school_number(obj):
    '''
    Function: get_school_number
    Parameters: a neighbourhood object --> object
    Return the number of schools in the neighbourhood --> int
    '''
    return obj.calculate_school_number()

def sort_neighbourhood_by_schools(neighbourhood_list):
    '''
    Function: sort_neighbourhood_by_schools --> sort the neighbourhoods by their numbers of schools in decreasing order
    Parameters: a list of neighbourhood objects--> list
    Return:
    a list of objects --> list
    Possible errors: ValueError
    '''
    if not isinstance(neighbourhood_list,list):
        raise ValueError("Parameter 'neighbourhood_list' must be list.")
    if not neighbourhood_list:
        raise ValueError("Parameters 'neighbourhood_list' cannot be empty list.")
    
    sorted_list = sorted(neighbourhood_list,reverse=True,key=get_school_number)
    return sorted_list

def analyze_school(sorted_list):
    '''
    Function: analyze_school --> Calculate the number of schools in each neighbourhood
    Parameters: a list of neighbourhood objects
    Return:
    neighbourhood_name_list --> a list of strings
    school_number_list ---> a list of integers
    Possible errors: ValueError
    '''
    if not isinstance(sorted_list,list):
        raise ValueError("Parameter 'sorted_list' must be list.")
    if not sorted_list:
        raise ValueError("Parameters 'sorted_list' cannot be empty list.")
    
    neighbourhood_name_list = [obj.name for obj in sorted_list]
    school_number_list = [obj.calculate_school_number() for obj in sorted_list]
    return neighbourhood_name_list,school_number_list

def analyze_student(sorted_list):
    '''
    Function: analyze_student --> Calculate the number of students in each neighbourhood
    Parameters: a list of neighbourhood objects
    Return:
    neighbourhood_name_list --> a list of strings
    student_number_list ---> a list of integers
    Possible errors: ValueError
    '''
    if not isinstance(sorted_list,list):
        raise ValueError("Parameter 'sorted_list' must be list.")
    if not sorted_list:
        raise ValueError("Parameters 'sorted_list' cannot be empty list.")
  
    neighbourhood_name_list = [obj.name for obj in sorted_list]
    student_number_list = [obj.calculate_student_number() for obj in sorted_list]
    return neighbourhood_name_list,student_number_list

def analyze_ratio(sorted_list):
    '''
    Function: analyze_ratio --> Calculate the average number of students per school in each neighbourhood
    Parameters: a list of neighbourhood objects
    Return:
    neighbourhood_name_list --> a list of strings
    ratio_list ---> a list of integers
    Possible errors: ValueError
    '''
    if not isinstance(sorted_list,list):
        raise ValueError("Parameter 'sorted_list' must be list.")
    if not sorted_list:
        raise ValueError("Parameters 'sorted_list' cannot be empty list.")
    
    neighbourhood_name_list = [obj.name for obj in sorted_list]
    ratio_list = [obj.calculate_students_per_school() for obj in sorted_list]
    return neighbourhood_name_list,ratio_list

def calculate_school_average_and_store_in_list(neighbourhood_list):
    '''
    Function: calculate_school_average_and_store_in_list
    calculate the average number of schools in all neighbourhoods, and return a list to be used in visualization
    Parameters: a list of neighbourhood objects --> list
    Return a list of integers, all the integers are the same average value
    Possible errors: ValueError
    '''
    if not isinstance(neighbourhood_list,list):
        raise ValueError("Parameter 'neighbourhood_list' must be list.")
    if not neighbourhood_list:
        raise ValueError("Parameters 'neighbourhood_list' cannot be empty list.")
    
    school_list = []
    for neighbourhood in neighbourhood_list:
        school_list.append(neighbourhood.calculate_school_number())
    school_average = round(sum(school_list) / len(neighbourhood_list))
    result = []
    for i in range(0,len(neighbourhood_list)):
        result.append(school_average)
    return result

def calculate_student_average_and_store_in_list(neighbourhood_list):
    '''
    Function: calculate_student_average_and_store_in_list
    calculate the average number of students in all neighbourhoods, and return a list to be used in visualization
    Parameters: a list of neighbourhood objects --> list
    Return a list of integers, all the integers are the same average value
    Possible errors: ValueError
    '''
    if not isinstance(neighbourhood_list,list):
        raise ValueError("Parameter 'neighbourhood_list' must be list.")
    if not neighbourhood_list:
        raise ValueError("Parameters 'neighbourhood_list' cannot be empty list.")

    student_list = []
    for neighbourhood in neighbourhood_list:
        student_list.append(neighbourhood.calculate_student_number())
    student_average = round(sum(student_list) / len(neighbourhood_list))
    result = []
    for i in range(0,len(neighbourhood_list)):
        result.append(student_average)
    return result

def calculate_ratio_average_and_store_in_list(neighbourhood_list):
    '''
    Function: calculate_ratio_average_and_store_in_list
    calculate the average value of a ratio students per school in all neighbourhoods, and return a list to be used in visualization
    Parameters: a list of neighbourhood objects --> list
    Return a list of integers, all the integers are the same average value
    Possible errors: ValueError
    '''
    if not isinstance(neighbourhood_list,list):
        raise ValueError("Parameter 'neighbourhood_list' must be list.")
    if not neighbourhood_list:
        raise ValueError("Parameters 'neighbourhood_list' cannot be empty list.")

    ratio_list = []
    for neighbourhood in neighbourhood_list:
        ratio_list.append(neighbourhood.calculate_students_per_school())
    ratio_average = round(sum(ratio_list) / len(neighbourhood_list))
    result = []
    for i in range(0,len(neighbourhood_list)):
        result.append(ratio_average)
    return result

    
def find_neighbourhood(neighbourhood_name,neighbourhood_list):
    '''
    Function: find_neighbourhood --> given a neighbourhood name, search and find it in a list of neighbourhood objects
    Parameters: 
    neighbourhood name --> string
    a list of neighbourhood objects--> list
    Return the neighbourhood object --> object
    Possible errors: ValueError
    '''
    if not isinstance(neighbourhood_name,str):
        raise ValueError("Parameter 'neighbourhood_name' must be string.")
    if not isinstance(neighbourhood_list,list):
        raise ValueError("Parameter 'neighbourhood_list' must be list.")
    if not neighbourhood_list:
        raise ValueError("Parameters 'neighbourhood_list' and 'sorted_dict' cannot be empty list.")

    for neighbourhood in neighbourhood_list:
        if neighbourhood.name == neighbourhood_name:
            return neighbourhood

def find_school(school_name,school_list):
    '''
    Function: find_school --> given a school name, search and find it in a list of school objects
    Parameters: 
    school name --> string
    a list of school objects--> list
    Return the school object --> object
    Possible errors: ValueError
    '''
    if not isinstance(school_name,str):
        raise ValueError("Parameter 'school_name' must be string.")
    if not isinstance(school_list,list):
        raise ValueError("Parameter 'school_list' must be list.")
    if not school_list:
        raise ValueError("Parameters 'school_list' cannot be empty list")
    
    for school in school_list:
        if school.name == school_name:
            return school
