array = [1, 2, 4, 5, 8, 2, 3, 8, 4, 10]

equalMemory = []
count = 0
for i in range(len(array) - 1):
    if array.count(array[i]) > 1:
        if array[i] not in equalMemory:
            count += 1
            equalMemory.append(array[i])

print("Количество одинаковых пар элементов:", count)
