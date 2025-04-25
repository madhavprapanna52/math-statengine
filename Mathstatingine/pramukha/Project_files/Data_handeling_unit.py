"""
Data processing Unit 
Functions 
1. Making basic data operations | cleaning, outliers filtering 
        Removing irrelevent based compression techniques/ filtering algo
2. Surface level computation decissions for further processing units 
        declearing complexity , Nature and Size 
"""
import pandas as pd 
from Testing_unit import *
from stats_Engine import *
import os
import csv


def discreet(list_points):
    pass



def file_inspection(file_path):
    '''
    Function : Make decissions based on inspections check 
    Inspection checks 
        1. file size 
        2. Random row inspection and system information 

    file inspection procedure 
    file extension > size and row inspection > proceed with computation routes  
    output : Command driving other functioning of the program 
    #TODO Need inspections for text based 
    '''
    #TODO Making log file for the terminal output managements 
    file_size = os.path.getsize(file_path)
    print(f'File size : {file_size}')
    with open(file_path, 'r') as file_handle:
        reader = csv.reader(file_handle)
        # inspecting 10 sets

        chunk_set = []
        print(f'header : {next(reader)}')
        for _ in range(10):
            i = next(reader)
            chunk_set.append(i)
        print('Making inspection to the chunk of file would be great to proceed further')
        print(f'         {chunk_set}')
    # Discreet / Continuous | Points variability is low then its continuous 
    total = sum([int(x[1]) for x in chunk_set])  # using list comprehension
    decimal_dataset = (type(total) == float)
    avg = total/len(chunk_set)
    variance = []
    for _ in chunk_set:
        vari = (int(_[1]) - avg)**2
        variance.append(vari)
    variance_avg = sum(variance)/len(variance)
    # Making threshhold for discreet and continuous 
    if (variance_avg < 5) and decimal_dataset:
        print('Data_set is continuous - Under construction')
        return 'Continuous Dataset'  # exception case

    else:
        print(f'Data is Discreet : {variance_avg}')
        # Making discreet dataset inspection
        unique_set = set(chunk_set)
        if (len(unique_set)>2):
            print(f'Not ment for automated Distribution report')
            return False  # initiation of user interactive panel for informations

        else:
            print("Making automated Distribution report for dataset ..")
            return True # For making automated report
        

#TODO Making computational decissions logic - inspecting dataset for preprocessing : possible compressions algorithms 
