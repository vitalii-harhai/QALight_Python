
a = int(input("Введіть значення A: "))
b = int(input("Введіть значення B: "))
c = int(input("Введіть значення C: "))

history = []

while True:

    if a < b:
        print("Дуже сумно!")
        a += c
        history.append(a)
    else:
        print("Нарешті вгадав!")
        print("Історія інкрементів: ", history)
        break
