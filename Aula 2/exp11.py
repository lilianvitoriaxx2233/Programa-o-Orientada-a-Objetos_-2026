import math
b = int(input("Informe o valor da base:"))
h = int(input("Informe o valor da altura:"))

def Diagonal(b, h):
    diagonal = math.sqrt(b**2+h**2)
    return diagonal

diagonal = Diagonal(b, h)
print(diagonal)