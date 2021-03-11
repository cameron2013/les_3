print("Введите числа или q чтобы выйти: \nДля обнуления нажмите '0'")
b = []
flag_1 = False
flag_2 = False
while True:
    a = input().split()
    try:
        for i in range(len(a)):
            if a[i] == 'q' or a[i] == 'Q':
                flag_1 = True
            if a[i] == '0':
                flag_2 = True
            a[i] = float(a[i])
            b.append(a[i])
    except (ValueError, TypeError):
        print("Введено не число")
    print(f"Результат {sum(b)}")
    if flag_1 is True:
        print("Выплнение закончено")
        break
    if flag_2 is True:
        flag_2 = False
        print("Обнуление результата")
        b = []
        print(f"Результат {sum(b)}")
