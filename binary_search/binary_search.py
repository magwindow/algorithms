import math

def binarysearch(sorted_cabinet,looking_for):
    """Бинарный поиск"""
    guess = math.floor(len(sorted_cabinet)/2)
    upperbound = len(sorted_cabinet)
    lowerbound = 0
    
    while abs(sorted_cabinet[guess] - looking_for) > 0.0001:
        if sorted_cabinet[guess] > looking_for:
            upperbound = guess
            guess = math.floor((guess + lowerbound)/2)
        if sorted_cabinet[guess] < looking_for:
            lowerbound = guess
            guess = math.floor((guess + upperbound)/2)
    
    return guess


sortedcabinet = [1,2,3,4,5,6,7,8,9,10]

print(binarysearch(sortedcabinet,8))



def inverse_sin(number):
    """
    Находит позиции числа, синус которого равен заданному числу, 
    и возвращает значение предметной области с заданным индексом
   """
    domain = [x * math.pi/10000 - math.pi/2 for x in list(range(0,10000))]
    the_range = [math.sin(x) for x in domain]
    result = domain[binarysearch(the_range,number)]
    return result

print(inverse_sin(0.9))