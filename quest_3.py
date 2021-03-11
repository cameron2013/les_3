# Третья задача
def max_sum(a, b, c):
    return a + b + c - min(a, b, c)

a = input("Введите а: ")
b = input("Введите b: ")
c = input("Введите c: ")
try:
    a = float(a)
    b = float(b)
    c = float(c)
    print(f"Максимальная сумма двух элементов: {max_sum(a, b, c)}")
except ValueError:
    print("Переменные не числа!")
