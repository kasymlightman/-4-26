data = input("Введите a и b: ").replace(",", " ").split()
a = float(data[0])
b = float(data[1])

def f(x):
    return int(x) if x == int(x) else x

print(f"сумма={f(a + b)}, разность={f(a - b)}, произведение={f(a * b)}", end=", ")

if b == 0:
    print("деление на ноль")
else:
    print(f"частное={a / b:.2f}, остаток={f(a % b)}")
