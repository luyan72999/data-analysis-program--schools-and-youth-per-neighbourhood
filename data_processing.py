'''
CS 5001 Fall 2022 Lu YAN
Milestone 2
data_processing: this file contains all the functions for data downloading, cleaning, and parsing into objects
'''
import requests
from requests.exceptions import HTTPError
from requests.exceptions import ConnectionError
from constants import *
from School import School
from Neighbourhood import Neighbourhood


def download_csv(url):
    '''
    Function: download_csv --> download a csv from an url and exact its content as a string
    Parameters: the url of a csv file --> string
    Return: the content of the csv file --> string
    Possible errors: 
    HTTP and Connection errors
    Value errors
    '''
    if not isinstance(url,str):
        raise ValueError("Parameter 'url' must be string.")
    response = requests.get(url)
    response.raise_for_status()
    text = response.text
    return text

def clean_and_parse_schools_into_objects(school_content): 
    '''
    Function: clean_and_parse_schools_into_objects --> Delete the undesired rows and columns of school.csv content, and parse data into school objects
    Parameters: the whole content of the school csv file --> string
    Return: a list of schools --> a list of objects
    Possible errors: ValueError
    '''
    if not isinstance(school_content,str):
        raise ValueError("Parameter 'school_content' must be a string.")

    temp_list_1 = school_content.split("\n")[SCHOOL_FIRST_CONTENT_LINE:LAST_ELEMENT]

    temp_list_2 = []
    for line in temp_list_1:
        temp_list_2.append(line.split(";"))

    school_list = []
    for line in temp_list_2:
        school = School(line[SCHOOL_NAME_COLUMN],line[SCHOOL_TYPE_COLUMN],line[SCHOOL_NEIGHBOURHOOD_COLUMN][:LAST_ELEMENT])
        school_list.append(school)

    return school_list

def clean_and_parse_people_into_objects(people_content):
    '''
    Function: clean_and_parse_people_into_objects --> Delete the undesired rows and columns of CensusLocalAreaProfiles.csv content, and parse data into neighbourhood objects
    Parameters: the whole content of the Census.csv file --> string
    Return: a list of neighbourhoods --> a list of objects
    Possible errors: ValueError
    '''
    if not isinstance(people_content,str):
        raise ValueError("Parameter 'people_content' must be a string.")
    
    content = people_content[FIRST_ELEMENT:PEOPLE_CONTENT_CUT]

    # create the neighbourhoods list
    temp_list_1 = content.split("\n")[NEIGHBOURHOOD_LINE].split(",")[NEIGHBOURHOOD_START_COLUMN:LAST_TWO_ELEMENTS]
    
    # create the number of people list
    redundant_symbol = ',"'
    content_without_symbol = content.translate(str.maketrans("","",redundant_symbol))
    temp_list_2 = content_without_symbol.split("\n")[FIVE_TO_NINE_YEARS_LINE:FIFTEEN_TO_NINETEEN_YEARS_LINE]
    temp_list_3 = []
    for item in temp_list_2:
        temp_list_3.append(item.split("  ")[2:LAST_TWO_ELEMENTS])

    # parse the data in 2 lists into objects
    neighbourhood_list = []
    for i in range(len(temp_list_1)):
        neighbourhood = Neighbourhood(temp_list_1[i],int(temp_list_3[FIVE_TO_NINE_YEARS_LIST][i]),int(temp_list_3[TEN_TO_FOURTEEN_YEARS_LIST][i]),int(temp_list_3[FIFTEEN_TO_NINETEEN_YEARS_LIST][i]))
        neighbourhood_list.append(neighbourhood)
    return neighbourhood_list

def add_school_to_neighbourhood(school_list,neighbourhood_list):
    '''
    Function: add_school_to_neighbourhood  --> add school objects into the attributes of corresponding neighbourhood objects
    Parameters: 
    a list of school objects --> list
    a list of neighbourhood objects --> list
    Return nothing
    Possible errors: ValueError
    '''
    if not isinstance(school_list,list) or not isinstance(neighbourhood_list,list):
        raise ValueError("Parameters 'school_list' and 'neighbourhood_list' must be list.")
    if not school_list or not neighbourhood_list:
        raise ValueError("Parameters 'school_list' and 'neighbourhood_list' cannot be empty list.")
    
    for neighbourhood in neighbourhood_list:
        for school in school_list:
            if school.neighbourhood == neighbourhood.name:
                neighbourhood.add_school(school)
