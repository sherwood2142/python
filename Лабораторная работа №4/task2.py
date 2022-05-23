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

arr1 = set()
arr2 = set()
for i in range(len(arr1Str)):
    arr1.add(int(arr1Str[i]))
for i in range(len(arr2Str)):
    arr2.add(int(arr2Str[i]))

# print(arr1, arr2)

print(sorted(arr1.intersection(arr2)))
