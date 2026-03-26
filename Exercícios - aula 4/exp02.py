print("Ler uma string com dois valores inteiros positivos entre um operador:")
print()
expressao = input("Digite a operação (ex: 20+100): ")

if "+" in expressao:
    x, y = expressao.split("+")
    resultado = int(x) + int(y)
elif "-" in expressao:
    x, y = expressao.split("-")
    resultado = int(x) - int(y)
elif "*" in expressao:
    x, y = expressao.split("*")
    resultado = int(x) * int(y)
elif "/" in expressao:
    x, y = expressao.split("/")
    resultado = int(x) / int(y)

print("O resultado da operação é", resultado)
