a_user = int(input("Введіть значення A: "))
b_user = int(input("Введіть значення B: "))
c_user = int(input("Введіть значення C: "))


def my_function(a, b, c):

    # lesson 1
    if a > b:
        print("Дуже погано")
    elif b > a:
        if b > c:
            print("Просто супер!")
        else:
            print("Не дуже супер")
    elif a == b:
        print("Значення одинакові")

    # lesson 2
    history = []
    while True:

        if a < b:
            print("Дуже сумно!!!!!!!!!!!")
            a += c
            history.append(a)
        else:
            print("Нарешті вгадав!")
            print("Історія інкрементів: ", history)
            break


my_function(a_user, b_user, c_user)
