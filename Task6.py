a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
days = 1
print(f"{days}-й день: {a}")
while a < b:
    days += 1
    a = a + 0.1 * a
    print(f"{days}-й день: {a:.2f}")

print(f"Вы достигнете требуемых показателей на %.d день" % days)