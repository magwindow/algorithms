def gcd(x,y):
    """Рекурсивная реализация алгоритма Евклида"""
    larger = max(x,y)
    smaller = min(x,y)
    remainder = larger % smaller

    if remainder == 0:
        return(smaller)
    
    if remainder != 0:
        return gcd(smaller,remainder)
    

# print(gcd(12,8))

luoshu = [[4,9,2],[3,5,7],[8,1,6]]

def verifysquare(square: list) -> bool:
    """
    Функция проверяет является ли квадрат магическим.
    Для этого вычисляет суммы по всем строкам,
    столбцам и диагоналям, а затем проверяет, что все они одинаковы.
    """
    sums = []
    rowsums = [sum(square[i]) for i in range(0,len(square))]
    sums.append(rowsums)
    colsums = [sum([row[i] for row in square]) for i in range(0,len(square))]
    sums.append(colsums)
    maindiag = sum([square[i][i] for i in range(0,len(square))])
    sums.append([maindiag])
    antidiag = sum([square[i][len(square) - 1 - i] for i in range(0,len(square))])
    sums.append([antidiag])
    flattened = [j for i in sums for j in i]
    return(len(list(set(flattened))) == 1)

print(verifysquare(luoshu))