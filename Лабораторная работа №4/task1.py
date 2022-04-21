file = "Organization.txt"
txt = open(file, 'w')

n = int(input("Сколько записей хотите ввести: "))

print("Напишите", n, "записей в телефонный справочник")
for i in range(n):
    # record = str(input(f"{i+1} запись: "))
    # txt.write(record + "\n")
    print(f"{i+1} запись:")
    organization = str(input("Введите организацию: "))
    address = str(input("Введите адрес организации: "))
    number = str(input("Введите контактный телефон организации: "))
    txt.write(f"{organization} {address} {number}\n")


txt.close()

print("Данные внутри телефонного справочника:")
txt = open(file, 'r')
print(txt.read())
txt.close()
