"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""
my_str = input("введите строку из нескольких слов, разделённых пробелами ")
my_word = []
number = 1
for i in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    print(f" {number} {my_word[i][0:10]}")
    number += 1
