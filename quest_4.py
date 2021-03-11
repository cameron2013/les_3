# Четвертая задача
def return_power(a, b):
    if b == int(b):
        b = int(b)
        if b < 0:
            a1 = a
            for i in range(abs(b)-1):
                a1 = a1 * a
            return 1/a1
        else:
            return "Функция должна принимать отрицательное второе число"
    else:
        return "Второе число не целочисленное"


a = input("Введите первое число: ")
b = input("Введите второе целове отрицательное число: ")
try:
    a = float(a)
    b = float(b)
    print(f"Результат: {return_power(a, b)}")
except ValueError:
    print("Введены не числа")
