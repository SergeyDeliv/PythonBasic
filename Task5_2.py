"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("task5_2.txt", 'a', encoding="utf-8") as f:
    content = input("Input anything: ")
    while content:
        f.writelines(content + "\n")
        content = input("Input anything: ")
        if not content:
            break

with open('task5_2.txt', 'r', encoding="utf-8") as f:
    content = f.read()
    print(f'Содержимое файла: \n{content}')
    content = content.split()
    print(f'Общее количество слов - {len(content)}')

with open('task5_2.txt', 'r', encoding="utf-8") as f:
    content = f.readlines()
    print(f'Количество строк в файле - {len(content)}')
    for i in range(len(content)):
        print(f'Количество символов {i + 1} - ой строки {len(content[i])}')






