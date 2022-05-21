
a = int(input("Введіть значення A: "))
b = int(input("Введіть значення B: "))
c = int(input("Введіть значення C: "))

if a > b:
    print("Дуже погано")
elif b > a:
    if b > c:
        print("Просто супер!")
    else:
        print("Не дуже супер")
elif a == b:
    print("Значення одинакові")



