A = int(input("Введите число A = "))
B = int(input("Введите число B = "))
C = int(input("Введите число C = "))

if A > B and A > C:
    print("Число A", A, "максимальное")
elif B > A and B > C:
    print("Число B", B, "максимальное")
elif C > A and C > B:
    print("Число C", C, "максимальное")
else:
    print("Есть несколько максимальных чисел")