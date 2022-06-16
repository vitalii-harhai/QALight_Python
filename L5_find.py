import random

# Створюємо список з 10 випадкових чисел
ls = []
for i in range(10):
    ls.append(random.randrange(10))


# Функція формує список з індексами числа, яке шукає користувач
def find(number):
    list_position = []
    s = 0
    for el in ls:
        if el == number:
            list_position.append(s)
        s += 1
    return list_position


# Отримуємо число для пошуку від користувача
user_find = int(input("Введіть число, яке будемо шукати: "))

# Отримуємо список з індексами знайденого числа
list_index = find(user_find)

# Формування строки для виводу в термінал, на випадок якщо число повторюється
str_terminal = "Число, яке ви шукаєте, знаходиться у списку під номером "
s1 = 0
for i in list_index:
    if s1 == 0:
        str_terminal = str_terminal + str(list_index[s1])
    else:
        str_terminal = str_terminal + " та під номером " + str(list_index[s1])
    s1 += 1
print(str_terminal)
