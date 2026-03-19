print("Valores inteiros:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a==b or a==c or a==d or b==c or c==d:
    print("Erro")
else:
    maior = max(a, b, c, d)
    menor = min(a, b, c, d)

    lista = [a, b, c, d]
    lista.remove(maior)
    lista.remove(menor)

    somar_seg = lista[0] + lista[1]

print("Maior valor =", maior)
print("Menor valor =", menor)
print("Soma do seg maior com o seg menor =", somar_seg)
