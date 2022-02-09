def factorial(num):
    factorialNumber = 1
    i = 1
    while i <= num:
        factorialNumber *= i
        i += 1

    return factorialNumber


factNum = int(input("Введите факториал = "))
print("Факториал от", factNum, "равен:", factorial(factNum))
