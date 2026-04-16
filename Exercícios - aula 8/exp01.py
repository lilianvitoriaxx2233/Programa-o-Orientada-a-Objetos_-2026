print("Ler dois valores inteiros e imprimir o maior deles:")
print()

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

if a > b:
    print("Maior =", a)
elif b > a:
    print("Maior =", b)
else:
    print("Números iguais")
