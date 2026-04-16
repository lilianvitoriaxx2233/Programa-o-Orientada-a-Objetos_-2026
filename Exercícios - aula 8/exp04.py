print("Sequência de números inteiros separados por vírgula:")
print()
numeros = input("Digite números separados por vírgula: ")

lista = numeros.split(",")
soma = 0

for n in lista:
    soma += int(n)

print("Soma =", soma)
