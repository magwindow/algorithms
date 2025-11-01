def insert_cabinet(cabinet, to_insert):
    """Вставка папки с заданным номером на полку"""
    check_location = len(cabinet) - 1
    insert_location = 0
    while check_location >= 0:
        if to_insert > cabinet[check_location]:
            insert_location = check_location + 1
            check_location = - 1
        check_location = check_location - 1
    cabinet.insert(insert_location, to_insert)
    return cabinet

# cabinet = [1,2,3,3,4,6,8,12]
# newcabinet = insert_cabinet(cabinet,5)
# print(newcabinet)


def insertion_sort(cabinet):
    """Сортировка методом вставки"""
    newcabinet = []
    while len(cabinet) > 0:
        to_insert = cabinet.pop(0)
        newcabinet = insert_cabinet(newcabinet, to_insert)
    return newcabinet


# cabinet = [8,4,6,1,2,5,3,7]
# sortedcabinet = insertion_sort(cabinet)
# print(insertion_sort(sortedcabinet))


def find_smallest(arr):
    """Поиск наименьшего элемента в списке"""
    # Для хранения наименьшего значения
    smallest = arr[0]
    # Для хранения индекса наименьшего значения
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    """Сортировка выбором"""
    new_arr = []
    for i in range(len(arr)):
        # Находит наименьший элемент в списке
        # и добавляет его в новый список
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

print(selection_sort([5,3,6,2,10]))