from random import randrange

n = 10
array = [randrange(1, 10) for i in range(n)]

print("Сгенерированный массив:", array)

print("Чётные элементы массива:")
for i in range(len(array)):
    if array[i] % 2 == 0:
        print(array[i])
