"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def div():
    try:
        res = int(input("Введите делимое число ")) / int(input("Введите делитель "))
    except ValueError:
        return 'Ошибочное значение'
    except ZeroDivisionError:
        return "На ноль делить нельзя"

    return res


print(f'Результат:  {div()}')
