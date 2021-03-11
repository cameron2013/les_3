# Шестая задача
# Вариант через title
def int_func(a):
    flag_low = False
    for i in a:
        if not((ord(i)>=65 and ord(i)<=90) or ((ord(i)>=97 and ord(i)<=122)) or ord(i)==32):
            print("Слово не из латинских букв")
            return None
        if ord(i)>=65 and ord(i)<=90:
            flag_low = True
    if flag_low is True:
        print("В слове есть заглавные буквы. \nПеробразование слова к маленьким буквам.")
        a.lower
    return a.title()


print(f'Результат: {int_func(input("Введите слово: "))}')
# Ввод строки
a = input("Введите строку: ")
print(f"Результат: {int_func(a)}")


# Вариант без title
def int_func_without_title(a):
    flag_low = False
    for i in a:
        if not((ord(i)>=65 and ord(i)<=90) or ((ord(i)>=97 and ord(i)<=122)) or ord(i)==32):
            print("Слово не из латинских букв")
            return None
        if ord(i)>=65 and ord(i)<=90:
            flag_low = True
    if flag_low is True:
        print("В слове есть заглавные буквы. \nПеробразование слова к маленьким буквам.")
        a.lower
    for i in range(len(a)):
        if i == 0:
            b = chr(ord(a[i]) - 32)
        else:
            b = b + a[i]
    return b


print(f'Результат: {int_func_without_title(input("Введите слово: "))}')
# Ввод строки
a = input("Введите строку: ").split()
b = ''
for i in range(len(a)):
    a[i] = int_func_without_title(a[i])
    b = b + a[i] + ' '
print(f"Результат: {b}")
