"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1, arg2, arg3):
    if arg1 > arg3 < arg2:
        return print(f"Сумма наибольших двух аргументов {arg1 + arg2}")
    elif arg1 > arg2 < arg3:
        return print(f"Сумма наибольших двух аргументов {arg1 + arg3}")
    else:
        return print(f"Сумма наибольших двух аргументов {arg2 + arg3}")


my_func(int(input("Введите первый позиционный аргумент: ")),
        int(input("Введите второй позиционный аргумент: ")),
        int(input("Введите третий позиционный аргумент: ")))
