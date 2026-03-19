print("Palavras de t´ras pra frente")
print("Digite uma frase: ")
frase = input()
palavras = frase.split()

for p in palavras:
    print(p[::-1])