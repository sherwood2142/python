def factorial(num):
    factorialNumber = 1
    for i in range(1, num + 1):
        factorialNumber *= i

    return factorialNumber


factNum = int(input("Введите факториал = "))
print("Факториал от", factNum, "равен:", factorial(factNum))
