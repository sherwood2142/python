filePath = "Numbers.txt"
with open(filePath, "r") as file:
    str1 = file.readline()
    # print(str1, end="")
    str2 = file.readline()
    # print(str2)

str1 = str1.replace("\n", "")
arr1Str = str1.split(" ")
str2 = str2.replace("\n", "")
arr2Str = str2.split(" ")

arr1 = []
arr2 = []
for i in range(len(arr1Str)):
    arr1.append(int(arr1Str[i]))
for i in range(len(arr2Str)):
    arr2.append(int(arr2Str[i]))

print(arr1)
print(arr2)

arrContain = []
equalMemory = []

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            if arr1[i] not in equalMemory:
                arrContain.append(arr1[i])
            else:
                equalMemory.append(arr1[i])

arrContain.sort()
print(arrContain)
