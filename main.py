#1
try:
    x = int(input())
except ValueError:
    print("Iltimos, son kiriting!")
#2
try:
    a = float(input())
    b = float(input())
    print(a / b)
except ZeroDivisionError:
    print("Nolga bo'lib bo'lmaydi!")
#3
lst = [1, 2, 3, 4]
try:
    i = int(input())
    print(lst[i])
except IndexError:
    print("Bunday indeks mavjud emas!")

#4
d = {"a": 1, "b": 2}
try:
    k = input()
    print(d[k])
except KeyError:
    print("Kalit topilmadi!")

#5
try:
    s = input()
    print(int(s))
except ValueError:
    print("Bu matnni songa aylantirib bo'lmaydi!")
