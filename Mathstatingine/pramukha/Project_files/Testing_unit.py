# Validating units
import random as rd
from stats_Engine import *
import matplotlib.pyplot as plt
import csv
import math

#TODO Making higher dimensional data structure for testing
def Data_generation(size=200, randomisation_scale=2):
    """
    Making  random set of different mathematical equation with noisy dataset randomisation
    Procedure 
    +. Making structured set of mathematical equations to generate points 
    +. randomisations of points based on randomised batch set and size range 
    
    """
    # Mathematical equation based base-dataset
    mathematical_equations = {
        'linear_equation' : 'm*x + c',
        'quadratic_equation' : 'a*(x**2) + b*x + c',
        'cubic_equation' : 'a*(x**3) + b*(x**2) + c*(x) + d'
        # More equations for testing 
    }
    # Random sellection of base math expression
    random_pic = rd.randint(0,len(mathematical_equations.values())-1)
    keys_eq = []
    for x in mathematical_equations.keys():
        keys_eq.append(x)
    Generating_equation = mathematical_equations[keys_eq[random_pic]]  # Generating equation

    # Expression logic
    eval_expression = ''  # eval expression for generation 
    for i in Generating_equation:
        if (i.isalpha()) and (not(i in 'x,y,z'.split(','))):
            var = rd.randint(-20, 20)  # making equation variable||Makig permutating combinations of the numbers 
            eval_expression += str(var)
        else:
            eval_expression += i
    print(f'Evaluation Expression : {eval_expression}')
    output_dataset = []  # appending random_processed points | (x_cord, evaluated_point)
    for point in range(0,size):
        x_eval_expression = ''
        # Potential function : Making changes in expressions for evaluations 
        for i in eval_expression:
            if i == 'x':
                x_eval_expression += str(point)
            else:
                x_eval_expression += i
        equation_based_point = eval(x_eval_expression)  # Base equation points check //
        #output_dataset.append(equation_based_point)

        # Making noise in the dataset 
        operations = '+,-,*'.split(',') # // division is making extream variations 
        random_operation = operations[rd.randint(0,len(operations)-1)]
        random_number = rd.randint(-10,10)  # more randomisations possible
        expression = str(equation_based_point) + str(random_operation) + str(random_number)  # Variations in the datapoint required
        randomised_point = abs(eval(expression))
        

        point_element = (point,randomised_point)
        output_dataset.append(point_element)

    # Making output dataset a file 
    data_set_file = open('/home/madhavr/Desktop/Mathstatingine/Data_set.csv','w')
    writer = csv.writer(data_set_file)
    writer.writerow(["x_coordinate","Randomised_point"])
    for i in output_dataset:
        writer.writerow(i) # making string flow 
    data_set_file.close()
    return '/home/madhavr/Desktop/Mathstatingine/Data_set.csv' # Data containning file name 
