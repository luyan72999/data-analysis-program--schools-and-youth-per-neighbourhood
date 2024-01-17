'''
CS 5001 Fall 2022 Lu YAN
Milestone 2
Visualization: this file contains all the functions for data visualization
'''
import matplotlib.pyplot as plt
from analysis import *

def make_bar_graph_school(sorted_neighbourhood_list):
    '''
    Function: make_bar_graph_school --> generate a matplot bar graph of schools and neighbourhoods
    Parameters: sorted_neighbourhood_list: a list of neighbourhood objects
    return nothing
    Possible errors: ValueError
    '''
    if not isinstance(sorted_neighbourhood_list,list):
        raise ValueError("Parameter 'sorted_neighbourhood_list' must be list.")
    if not sorted_neighbourhood_list:
        raise ValueError("Parameter 'sorted_neighbourhood_list' cannot be empty")

    xlabels, ylabels = analyze_school(sorted_neighbourhood_list)
    average_list = calculate_school_average_and_store_in_list(sorted_neighbourhood_list)
   
    figure, ax = plt.subplots(figsize = (12,6))
    ax.bar(xlabels, ylabels, color = "g")
    ax.plot(xlabels, average_list, color = 'r')
  
    ax.set_title("Number of schools in each neighbourhood")
    ax.legend(title="Red line: Average value")
    figure.autofmt_xdate()
    plt.show()

def make_bar_graph_student(sorted_neighbourhood_list):
    '''
    Function: make_bar_graph_student --> generate a matplot bar graph of students and neighbourhoods
    Parameters:sorted_neighbourhood_list: a list of neighbourhood objects
    return nothing
    Possible errors: ValueError
    '''
    if not isinstance(sorted_neighbourhood_list,list):
        raise ValueError("Parameter 'sorted_neighbourhood_list' must be list.")
    if not sorted_neighbourhood_list:
        raise ValueError("Parameter 'sorted_neighbourhood_list' cannot be empty")

    xlabels, ylabels = analyze_student(sorted_neighbourhood_list)
    average_list = calculate_student_average_and_store_in_list(sorted_neighbourhood_list)
   
    figure, ax = plt.subplots(figsize = (12,6))
    ax.bar(xlabels, ylabels, color = "y")
    ax.plot(xlabels, average_list, color = 'r')
  
    ax.set_title("Number of students in each neighbourhood")
    ax.legend(title="Red line: Average value")
    figure.autofmt_xdate()
    plt.show()

def make_bar_graph_ratio(sorted_neighbourhood_list):
    '''
    Function: make_bar_graph_ratio --> generate a matplot bar graph of average number of students per school, and neighbourhoods
    Parameters: sorted_neighbourhood_list: a list of neighbourhood objects
    return nothing
    Possible errors: ValueError
    '''
    if not isinstance(sorted_neighbourhood_list,list):
        raise ValueError("Parameter 'sorted_neighbourhood_list' must be list.")
    if not sorted_neighbourhood_list:
        raise ValueError("Parameter 'sorted_neighbourhood_list' cannot be empty")

    xlabels, ylabels = analyze_ratio(sorted_neighbourhood_list)
    average_list = calculate_ratio_average_and_store_in_list(sorted_neighbourhood_list)
   
    figure, ax = plt.subplots(figsize = (12,6))
    ax.bar(xlabels, ylabels, color = "#87CEFA")
    ax.plot(xlabels, average_list, color = 'r')
  
    ax.set_title("Average number of students per school in each neighbourhood")
    ax.legend(title="Red line: Average value")
    figure.autofmt_xdate()
    plt.show()

def display_single_neighbourhood_info(neighbourhood_list,label,entry):
    '''
    Function: display_single_neighbourhood_info --> given a neighbourhood object, display its info: schools,young people, and students per school in this neighbourhood
    Parameters: 
    neighbourhood list --> a list of neighbourhood objects
    label --> a tkinter label object to show the message
    entry --> a tkinter entry object to get user input
    Return nothing
    Possible errors: ValueError
    '''
    if not isinstance(neighbourhood_list,list):
        raise ValueError("Parameter 'neighbourhood_list' must be list.")
    if not neighbourhood_list:
        raise ValueError("Parameter 'neighbourhood_list' cannot be empty")

    neighbourhood_object = find_neighbourhood(entry.get(),neighbourhood_list)
    if neighbourhood_object:
        total_schools = neighbourhood_object.calculate_school_number()
        total_young_people = neighbourhood_object.calculate_student_number()
        ratio_students_schools = neighbourhood_object.calculate_students_per_school()
        text = f"Total number of schools: {total_schools}\nNumber of young people in {neighbourhood_object.name}:\nFive to nine years old: {neighbourhood_object.students_five_to_nine}\nTen to fourteen years old: {neighbourhood_object.students_ten_to_fourteen}\nFifteen to nineteen years old: {neighbourhood_object.students_fifteen_to_nineteen}\nTotal: {total_young_people}\nIn average, {ratio_students_schools} young people share one school in this neighbourhood."
        label["text"] = text
    else:
        label["text"] = "The neighbourhood you entered does not exist."


def display_single_school_info(school_list,label,entry):
    '''
    Function: display_single_school_info --> given a school object, display its info: school type and school neighhourhood
    Parameters: 
    school_list --> a list of school objects
    label --> a tkinter label object to show the message
    entry --> a tkinter entry object to get user input
    Return nothing
    Possible errors: ValueError
    '''
    if not isinstance(school_list,list):
        raise ValueError("Parameter 'school_list' must be list.")
    if not school_list:
        raise ValueError("Parameter 'school_list' cannot be empty")

    school_object = find_school(entry.get(),school_list)
    if school_object:
        text = f"{school_object.name}:\nSchool Type: {school_object.type}\nSchool Neighbourhood: {school_object.neighbourhood}"
        label["text"] = text
    else:
        label["text"] = "The school you entered does not exist."