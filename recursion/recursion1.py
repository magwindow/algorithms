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