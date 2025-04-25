"""
Making mathematical insights of the complex and high dimensional dataset 

> Handelling data-set based on vectors space units
    ~ Linear Algebra unit development for handeling transfromations and orthogonal computations 
> Mathematical insights unit 
    ~ for geting info regards the mathematical relations of the data units 

Output_structure 
        > Mathematical relations modeling unit
        > Robust Linear Algebra unit for dimensionality reduction outputs 
        > Final plot mathematical usefull observations unit 

"""

def expression_generator(generator_expression, size=100):
    """
    Generating points of the expressions | 
    making iterator from zero to the range for the expression based points
    Potential upgrade : Handle plane expressions 
    Procedure:
        iterate for variable > replace with the iterator then eval it 
    """
    points_generated = []
    # Generator expressions loop 
    for _ in range(size):
        expressiion = ''
        for x in generator_expression:
            if x == 'x':
                expressiion += _  #TODO Optimisations for faster computations potent point 
        point = eval(expressiion)  # evaluating final point 
        points_generated.append(point)
    print(f'Points generated :{points_generated[:20]}')
