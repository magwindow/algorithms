

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


cabinet = [8,4,6,1,2,5,3,7]
sortedcabinet = insertion_sort(cabinet)
print(insertion_sort(sortedcabinet))