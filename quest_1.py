def devide(a,b):
    if b != 0:
        return a/b


a = float(input("Введите a: "))
b = float(input("Введите b: "))
if devide(a,b) == None:
    print("Нельзя делить на ноль!")
else:
    print(f"a/b = {devide(a,b):.3f}")
