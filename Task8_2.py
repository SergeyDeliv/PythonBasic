"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyOwnError(Exception):
    def __init__(self, text):
        self.text = text


try:
    a = int(input("Введите число которое будем делить "))
    b = int(input("Введите число на которое будем делить "))
    if b == 0:
        raise MyOwnError("Делить на ноль нельзя!")
except MyOwnError as my:
    print(my)
except ValueError:
    print("Введите чило")
else:
    print(a / b)

# ---------------------------------------------------------------------------

class MyOwnError:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return ("А-та-та... Делить на ноль нельзя!")


rez = MyOwnError(10, 100)
print(MyOwnError.divide_by_null(10, 0))
print(MyOwnError.divide_by_null(10, 0.1))
print(rez.divide_by_null(100, 0))