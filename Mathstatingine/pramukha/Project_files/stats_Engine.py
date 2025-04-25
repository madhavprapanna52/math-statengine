'''
Statistical units for data processing 
> Models fiting unit 
    - Using generalisation fit techniques for geting fit of dataset
    -Making fitting algorithms for geting info about the parameters to extract from datset for future predictions 

> Data statistical observation unit 
    + tests for classification of data from statistical perspective
    + Exploring and revealing complexity

> Making flow of Execution of program 
Developing robust output set for good communications to units 
output structure : 
        > Statistical insights of dataset 
        > Unit and granular statistical modeling insights  // Math modeling 
        > In demand | decission output for program functioning 

'''
import math
from Data_handeling_unit import *

#TODO Making discriptive statistical unit working for the big dataset and handeling file based data 
def discriptive_statistical_analysis(data_set):
    '''
    #TODO More discriptive statistical units to add
    '''
    # Average Data
    total = 0
    mode = -10000000
    for i in data_set[1:]:  # i = [(x_cor, pnt)]
        print(f'The data being iterated for total : {i}')
        total += int(i)
        if mode < i[1]:
            mode = i[1]  # taking maximum out of 

    average = (total/len(data_set))
    # variance and standard deviation 
    variance = []
    standard_deviation = []
    for i in data_set:
        variance.append(i[1] - average)
        standard_deviation.append(math.sqrt((i[1] - average)**2)) # formula surity //
    
    report_dictionary = {'mean':average,'variance':variance,'standard_deviation':standard_deviation}
    return report_dictionary


#TODO Model fitting algorithms for making statistical modeling of given dataset for inferentials and math engine process 

def permutation(expression):  # checked | tested OK
    '''
    Just solving in an range of numbers to reduce computational resources efforts to compute every point
    Have many computations restrictions to compute big numbers thus it constrains to some only 
    procedure   
        Making factorials as list then taking account of equivalency and then reducing computations 
    '''
    def factolist_exp(number):
        exp = []
        for i in range(1,number+1):
            exp.append(i)
        return exp

    def multiplicating_list(l):
        f = 1
        for _ in l:
            f = f * int(_)
        return f
    elems = expression.split('_') # choosing set of numbers 
    for i in range(2):
        elems[i] = int(elems[i])
    # Making permutation computation decissions 
    if elems[1] > elems[0]:
        print('Error while making calculations')
    elif (elems[1] > elems[0] - 8):
        # factorial simplification based on sets 
        N = multiplicating_list(list(set(factolist_exp(elems[0])) - set(factolist_exp(elems[1]))))
        D = (elems[0] - elems[1])
        if D == 0:  # handle expception 
            print(f"permutation result : {N}")
            return int(N)
        else:
            print(f'permutation_result : {N/D}')
            return int(N/D)
        
    else:
        print('computational limits ..')

class Discreet_statistics:
    """
    Function making Basic discreet statistical analysis of the given dataset
    Modeling distributions 
        1. Binomial  - How many time success happen
        2. Hypergeometric - Whats total possibility of happening a event in the dataset perspective 
        3. Geometric - whats first time we got success
        4. Poisson - Loading ..

        Intellegence 
         + Analysing the dataset and ploting best fit distribution for the situation 
    """
    def __init__(data_set):  # file path required 
        self.data_set = data_set
        # Inspecting dataset for potent bionomial automations 
        self.test_1 = file_inspection(data_set)

    def report_making(self):
        '''
        Procedure :
            ~ Making Distribution report 
            Binomial : Graph plot through |expression point generator|
            geometric distribution : Success in given trials 
            hyper_geometric distribution for both p and (1-p) 
            poission distribution plot of the events number for both events 
        '''
        if self.test_1:
            print("Making report for the dataset ...")
            # Binomial Distribution based 
            binomial_expression = '(t_x)*(p**x)*((1-p)**(t-x))' # binomial expression
    

print(permutation('10_1')) # 10_3 => 86400 ? 