class Viagem:
    def __init__(self, distancia, horas, minutos):
        self.distancia = distancia
        self.horas = horas
        self.minutos = minutos

    def calcular_velocidade_media(self):
        tempo_total = self.horas + (self.minutos / 60)
        velocidade = self.distancia / tempo_total
        return velocidade



distancia = float(input("Digite a distância (km): "))
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))

v = Viagem(distancia, horas, minutos)

print("Velocidade média:", v.calcular_velocidade_media(), "km/h")