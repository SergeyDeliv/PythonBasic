"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open("task5_1.txt", 'w', encoding="utf-8") as f:
    content = input("Input anything: ")
    while content:
        f.writelines(content + "\n")
        content = input("Input anything: ")
        if not content:
            break

with open("task5_1.txt", 'r', encoding="utf-8") as f:
    print(f.read())
