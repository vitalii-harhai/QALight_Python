import random


def list_function(len_list, range_list):
    ls = []
    for i in range(len_list):
        ls.append(random.randrange(range_list))
    print(ls)


a = int(input("Введіть кількість елементів: "))
b = int(input("Введіть граничне значення діапазону: "))

list_function(a, b)
