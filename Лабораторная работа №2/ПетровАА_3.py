def deposit(x, p, y):
    year = 0
    while x < y:
        x += int(p / 100 * x)
        year += 1

    return year


x = int(input("Введите вклад в банке = "))
p = int(input("Введите проценты годового вклада = "))
y = int(input("Введите ожидаемое кол-во денег в накопительном счету = "))

print("Вам надо ждать", deposit(x, p, y), "лет")