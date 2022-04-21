filePath = "text.txt"
txt = open(filePath, 'r')
txtString = txt.read()
txt.close()

uniqueSymbols = []
equalMemory = []

for i in range(len(txtString)):
    if txtString[i] != " ":
        if txtString[i] not in equalMemory:
            uniqueSymbols.append(txtString[i])
            equalMemory.append(txtString[i])
        else:
            if len(uniqueSymbols) > 0:
                uniqueSymbols.remove(txtString[i])

print(f"Количество уникальных символов: {len(uniqueSymbols)}")
print(uniqueSymbols)
