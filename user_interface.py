'''
CS 5001 Fall 2022 Lu YAN
Final project
Milestone 2
interface: this file contains the function of loading GUI
'''

import tkinter
from tkinter import ttk
from visualization import *

def load_interface(sorted_neighbourhood_list,school_list):
    '''
    Function: laod_interface --> load tkinter interface
    Parameters:
    sorted_neighbourhood_list: a list of neighbourhood objects
    school_list: a list of school objects
    return nothing
    Possible errors: ValueError
    '''  
    if not isinstance(sorted_neighbourhood_list,list) or not isinstance(school_list,list):
        raise ValueError("Parameters 'sorted_neighbourhood_list' and 'school_list' must be list.")
    if not sorted_neighbourhood_list or not school_list:
        raise ValueError("Parameters 'sorted_neighbourhood_list' and 'school_list' cannot be empty list.")
        
    root = tkinter.Tk()
    root.title("Check Vancouver schools, students and neighbourhoods information")
    
    # create labels and buttons
    input_school = ttk.Label(root,text = "Enter school name to check its location and type\nExample: Fraser Academy / Little Flower Academy")
    entry_school = ttk.Entry(root,width=50)
    button_school = ttk.Button(root,text = "Search")
    label_school = ttk.Label(root,text="")

    input_neighbourhood = ttk.Label(text = "Enter neighbourhood name to check its information\nExample: Downtown / Sunset")
    entry_neighbourhood = ttk.Entry(root,width = 50)
    button_neighbourhood = ttk.Button(root,text = "Search")
    label_neighbourhood = ttk.Label(root,text="")

    button_school_graph = ttk.Button(root,text = "Show schools in all neighbourhoods")
    button_student_graph = ttk.Button(root,text = "Show students in all neighbourhoods")
    button_ratio_graph = ttk.Button(root,text = "Show average number of students per school")
    
    # label and button layout
    input_school.grid(row=0, column=0)
    entry_school.grid(row=0,column=1)
    button_school.grid(row=0,column=2)
    label_school.grid(row=1,column=0,columnspan=3)

    input_neighbourhood.grid(row=2, column=0)
    entry_neighbourhood.grid(row=2, column=1)
    button_neighbourhood.grid(row=2, column=2)
    label_neighbourhood.grid(row=3, column=0,columnspan=3)

    button_school_graph.grid(row=4, column=0)
    button_student_graph.grid(row=4, column=1)
    button_ratio_graph.grid(row=4, column=2)

    # set button event handling
    button_school.config(command = lambda: display_single_school_info(school_list,label_school,entry_school))
    button_neighbourhood.config(command = lambda: display_single_neighbourhood_info(sorted_neighbourhood_list,label_neighbourhood,entry_neighbourhood))
    button_school_graph.config(command = lambda: make_bar_graph_school(sorted_neighbourhood_list))
    button_student_graph.config(command = lambda: make_bar_graph_student(sorted_neighbourhood_list))
    button_ratio_graph.config(command = lambda: make_bar_graph_ratio(sorted_neighbourhood_list))
    
    # execute the root window
    root.mainloop()


