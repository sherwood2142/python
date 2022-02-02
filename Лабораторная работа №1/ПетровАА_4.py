import math

hypotenuse = float(input("Введите длину гипотенузы = "))
secondCathetus = float(input("Введите длину катета = "))

firstCathetus = math.sqrt(math.pow(hypotenuse, 2) - math.pow(secondCathetus, 2))


def trunc(num, digit):
    digit = 10 ** digit
    return (int(num * digit) / digit)


print("Длина первого катета = ", trunc(firstCathetus, 3))
