# Первая задача
def devide(a,b):
    if b != 0:
        return a/b


a = input("Введите a: ")
b = input("Введите b: ")
try:
    a = float(a)
    b = float(b)
    if devide(a, b) == None:
        print("Нельзя делить на ноль!")
    else:
        print(f"a/b = {devide(a, b):.3f}")
except ValueError:
    print("Переменные не числа!")
