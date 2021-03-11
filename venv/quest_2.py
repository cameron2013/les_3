def info_person():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    year = input("Введите год рождения: ")
    city = input("Введите город проживания: ")
    email = input("email: ")
    phone = input("тел.: ")
    return f"{name} {surname} {year}-го года рождения проживает в городе {city}/-е. Email: {email}, тел.: {phone}"


print(info_person())