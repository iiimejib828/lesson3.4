print('Конфликтные буквы')
print('Новые буквы')

v = 34, 12, 84  # создание кортежа
b = 34

# создание цикла
for a in v:
    if a < b:
        print('a меньше b')
    elif a > b:
        print('a больше b')
    else:
        print('a равно b')
