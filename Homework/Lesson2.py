# задание 2

number = int(input("Введите число в секундах:"))
hours = str(number // 3600)
minutes = str((number % 3600) // 60)
sec = str((number % 3600) % 60)
print(hours + ":" + minutes + ":" + sec)