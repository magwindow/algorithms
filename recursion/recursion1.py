def countdown(n):
    """Считает от n до 0"""
    print(n)
    if n <= 0:
        return
    else:
        countdown(n-1)
        
# countdown(10)

def fact(n):
    """Вычисляет факториал"""
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
# print(fact(5))

def sum(arr):
    """Сумма всех элементов списка"""
    total = 0
    for i in arr:
        total += i
    return total

def sum2(arr):
    """Рекурсивная сумма всех элементов списка"""
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum2(arr[1:])
    
# print(sum2([1,2,3,4,5]))
# print(sum([1,2,3,4,5]))

def count_array(arr):
    """Посчитывает количество элементов в списке"""
    if len(arr) == 0:
        return 0
    else:
        return 1 + count_array(arr[1:])
    
# print(count_array([1, 2, 3, 4, 5, 'a']))
    
