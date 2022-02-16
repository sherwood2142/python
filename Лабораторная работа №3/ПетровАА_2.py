from random import randrange

n = 10
array = [randrange(1, 10) for i in range(n)]

print("Сгенерированный массив:", array)

lengthOfArray = len(array)
maxElement = max(array)
minElement = min(array)

i = 0
while i < lengthOfArray - 1:
    temp = array[i]
    array[i] = array[i+1]
    array[i+1] = temp
    i += 2

print("Переставленный массив:", array)
