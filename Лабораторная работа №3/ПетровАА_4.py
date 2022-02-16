txt = open("Phonebook.txt", 'w')

n = 8
print("Напишите", n, "записей в телефонный справочник")
for i in range(n):
    record = str(input(f"{i+1} запись: "))
    txt.write(record + "\n")

txt.close()

print("Данные внутри телефонного справочника:")
txt = open("Phonebook.txt", 'r')
print(txt.read())
txt.close()
