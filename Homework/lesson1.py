# задание 1

name = "Anna"
age = 28
number = 3.4
print(name)
print(age)
print(number)

name = input("What is your name?")
print("Nice to meet you," + name)
age = input ("How old are you?")
print("Great! You are" + age + "years old")

# задание 2

number = int(input("Введите число в секундах:"))
hours = str(number // 3600)
minutes = str((number % 3600) // 60)
sec = str((number % 3600) % 60)
print(hours + ":" + minutes + ":" + sec)


# Задание 3
number = input("Введите число:")
number2 = (number) + (number)
number3 = (number) + (number) + (number)
print(int(number) + int(number2) + int(number3))

# Задание 5

revenue = int(input("Введите выручку компании:"))
costs = int(input("Введите издержки компании:"))

if revenue > costs:
    print("Ваша выручка больше издержек")
    profitability = (revenue - costs) / revenue * 100
    print("Ваша рентабельность составляет:" + str(profitability) + "%")
    number = int(input("Сколько у вас в компании сотрудников?"))
    number2 = revenue // number
    print("Прибыль фирмы в расчете на одного сотрудника составляет" + str(number2))
else:
    print("Ваши издержки больше выручки")
