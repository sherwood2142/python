username = str(input("Введите имя пользователя: "))
age = int(input("Введите возраст: "))


def printUser():
    print("Имя пользователя:", username)
    print("Возраст:", age)


if age < 14:
    birthCertificate = int(input("Введите номер свидетельства о рождении: "))
    printUser()
    print("Номер свидетельства о рождении:", birthCertificate)
elif 14 <= age < 27:
    passport = int(input("Введите номер паспорта: "))
    militaryID = int(input("Введите номер военного билета: "))
    printUser()
    print("Номер паспорта:", passport)
    print("Номер военного билета:", militaryID)
elif age >= 27:
    passport = int(input("Введите номер паспорта: "))
    printUser()
    print("Номер паспорта:", passport)
    print("Не военнообоязанный.")
