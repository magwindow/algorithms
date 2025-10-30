import random
import matplotlib.pyplot as plt

def insert_cabinet(cabinet,to_insert):
    check_location = len(cabinet) - 1
    insert_location = 0
    global stepcounter
    while check_location >= 0:
        stepcounter += 1
        if to_insert > cabinet[check_location]:
            insert_location = check_location + 1
            check_location = - 1
        check_location = check_location - 1
    stepcounter += 1
    cabinet.insert(insert_location,to_insert)
    return(cabinet)

def insertion_sort(cabinet):
    newcabinet = []
    global stepcounter
    while len(cabinet) > 0:
        stepcounter += 1
        to_insert = cabinet.pop(0)
        newcabinet = insert_cabinet(newcabinet,to_insert)
    return(newcabinet)


cabinet = [8,4,6,1,2,5,3,7]
stepcounter = 0
sortedcabinet = insertion_sort(cabinet)
# print("Кол-во шагов:", stepcounter)


def check_steps(size_of_cabinet):
    cabinet = [int(1000 * random.random()) for i in range(size_of_cabinet)]
    global stepcounter
    stepcounter = 0
    insertion_sort(cabinet)
    return stepcounter


random.seed(5040)
xs = list(range(1,100))
ys = [check_steps(x) for x in xs]
print(ys)

plt.plot(xs,ys)
plt.title('Количество шагов, необходимых для сортировки\nметодом вставки для случайных полок')
plt.xlabel('Количество папок на случайной полке')
plt.ylabel('Количество шагов, необходимых\nдля сортировки методом вставки')
plt.show()


