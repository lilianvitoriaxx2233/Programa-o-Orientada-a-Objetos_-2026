print("Remover palavra inicial")
frase = input()
palavras = frase.split()

for i in range(len(palavras)):
    print(" ".join(palavras[i:]))