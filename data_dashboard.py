'''
CS 5001 Fall 2022 Lu YAN
Final project
Milestone 2
data_dashboard: the driver file to execute the program
'''

from requests.exceptions import HTTPError
from requests.exceptions import ConnectionError
from data_processing import *
from analysis import sort_neighbourhood_by_schools
from user_interface import *

def main():
    try:
        content_people = download_csv(URL_PEOPLE)
        content_school = download_csv(URL_SCHOOL)
        school_list = clean_and_parse_schools_into_objects(content_school)
        neighbourhood_list = clean_and_parse_people_into_objects(content_people)
        add_school_to_neighbourhood(school_list,neighbourhood_list)
        sorted_neighbourhood_list = sort_neighbourhood_by_schools(neighbourhood_list)
        load_interface(sorted_neighbourhood_list,school_list)
    
    except HTTPError as e:
        print(e)
    except ConnectionError as e:
        print(e)
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except NameError as e:
        print(e)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()