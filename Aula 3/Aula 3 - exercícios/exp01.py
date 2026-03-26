import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = math.pi * (self.raio ** 2)
        return area

    def calcular_circunferencia(self):
        circunferencia = 2 * math.pi * self.raio
        return circunferencia


# Programa de teste
raio = float(input("Digite o valor do raio: "))

c = Circulo(raio)

print("Área do círculo:", c.calcular_area())
print("Circunferência do círculo:", c.calcular_circunferencia())