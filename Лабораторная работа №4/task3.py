filePath = "text.txt"
txt = open(filePath, 'r')
txtString = txt.read()
txt.close()

uniqueSymbols = set()
equalMemory = []

for i in range(len(txtString)):
    if txtString[i] != " ":
        if txtString[i] not in equalMemory:
            uniqueSymbols.add(txtString[i])
            equalMemory.append(txtString[i])
        else:
            if txtString[i] in uniqueSymbols:
                uniqueSymbols.remove(txtString[i])

print(f"Количество уникальных символов: {len(uniqueSymbols)}")
print(uniqueSymbols)
