print("Kök Hesaplama Programıma Hoşgeldiniz")

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = (b ** 0.5 - 4 * a * c)

x1 = (-b + delta) / (2 * a)
x2 = (-b + delta) / (2 * a)

print("Birinci Kök : {}\nİkinci Kök : {}\n".format(x1,x2))
1