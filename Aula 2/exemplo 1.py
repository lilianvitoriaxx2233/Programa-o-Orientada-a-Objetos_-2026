print("Quatro Valores Inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

somar_par = 0
somar_impar = 0

for x in [a, b, c, d]:
    if x % 2 == 0:
        somar_par += x
    else:
        somar_impar += x
print("Resultado dos pares =", somar_par)
print("Resultado dos ímpares =", somar_impar)