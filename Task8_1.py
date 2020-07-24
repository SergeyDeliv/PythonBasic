"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        i = 0
        if 1 <= day <= 31:
            i += 1
        else:
            print(f'Неправильный день')
        if 1 <= month <= 12:
            i += 1
        else:
            print(f'Неправильный месяц')
        if 2020 >= year >= 0:
            i += 1
        else:
            print(f'Неправильный год')
        if i == 3:
            print(f'Всё верно!')

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('23 - 07 - 2020')
print(today)
Data.valid(11, 11, 2020)
today.valid(40, 13, 2025)
print(Data.extract('11 - 11 - 2011'))
Data.valid(1, 11, 2000)
