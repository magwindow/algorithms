import math 

def continued_fraction(x,y,length_tolerance):
    """Алгоритм выражения дробей в виде непрерывных дробей"""
    output = []
    big = max(x,y)
    small = min(x,y)
    while small > 0 and len(output) < length_tolerance:
        quotient = math.floor(big/small)
        output.append(quotient)
        new_small = big % small
        big = small
        small = new_small
    return output


# print(continued_fraction(105,33,10))


def get_number(continued_fraction):
    """Преобразование непрерывной дроби в представление числа"""
    index = -1
    number = continued_fraction[index]
    while abs(index) < len(continued_fraction):
        next = continued_fraction[index - 1]
        number = 1/number + next
        index -= 1
    return number

# print(get_number([3,5,2]))


def continued_fraction_decimal(x,error_tolerance,length_tolerance):
    """Вычисление непрерывных дробей для дробных чисел"""
    output = []
    first_term = int(x)
    leftover = x - int(x)
    output.append(first_term)
    error = leftover
    while error > error_tolerance and len(output) <length_tolerance:
        next_term = math.floor(1/leftover)
        leftover = 1/leftover - next_term
        output.append(next_term)
        error = abs(get_number(output) - x)
    return output

# print(continued_fraction_decimal(1.4142135623730951,0.00001,100))


def square_root(x,y,error_tolerance):
    """Функция для вычисления квадратных корней по вавилонскому алгоритму"""
    our_error = error_tolerance * 2
    while our_error > error_tolerance:
        z = x/y
        y = (y + z)/2
        our_error = y**2 - x
    return y

# print(square_root(5,1,.000000000000001))  # sqrt(5)


def next_random(previous,n1,n2,n3):
    """Линейный конгруэнтный генератор"""
    the_next = (previous * n1 + n2) % n3
    return the_next

def list_random(n1,n2,n3):
    output = [1]
    while len(output) <= n3:
        output.append(next_random(output[len(output) - 1],n1,n2,n3))
    return output

print(list_random(29,23,32))