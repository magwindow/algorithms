def binary_search(list, item):
    # В переменных low и high хранятся границы то части списка,
    # в которой выполняется поиск
    low = 0
    high = len(list) - 1
    
    # Пока часть не сократиться до 1 элемента
    while low <= high:
        # Проверяем средний элемент
        mid = low + high
        guess = list[mid]
        # Значение найдено
        if guess == item:
            return mid
        # Много
        if guess > item:
            high = mid - 1
        # Мало
        else:
            low = mid + 1

    # Значение не существует
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))  # => 1
print(binary_search(my_list, -1))  # => None
        
        