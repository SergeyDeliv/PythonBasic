"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def my_func():
    try:
        name = input('Введите имя ')
        surname = input('Введите фамилию ')
        year = int(input('Введите год '))
        city = input('Введите город ')
        email = input('Введите email ')
        telephone = input('Введите телефон ')
        print(name, surname, year, city, email, telephone)
    except ValueError:
        return


my_func()
