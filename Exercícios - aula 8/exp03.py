print("Ler uma string, calcular e mostrar a soma dos caracteres que são algarismos:")
print()

frase = input("Digite uma frase: ")

soma = 0
for c in frase:
    if c.isdigit():
        soma += int(c)

print(soma, end = " ")
