number = int(input("Введите целое число: "))

if number % 2 == 0:
    parity = "четное"
else:
    parity = "нечетное"

if number > 0:
    sign = "положительное"
elif number < 0:
    sign = "отрицательное"
else:
    sign = "ноль"

if number % 5 == 0:
    multiple_of_5 = "да"
else:
    multiple_of_5 = "нет"

print(f"{parity}, {sign}, кратно 5: {multiple_of_5}")
