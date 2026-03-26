class Viagem:
    def __init__(self, distancia_km, horas, minutos):
        self.distancia_km = distancia_km
        self.horas = horas
        self.minutos = minutos

    def calcular_tempo_em_horas(self):
        return self.horas + (self.minutos / 60)

    def calcular_velocidade_media(self):
        tempo_total = self.calcular_tempo_em_horas()
        
        if tempo_total == 0:
            return 0
        
        return self.distancia_km / tempo_total


# Programa para testar a classe
def main():
    distancia = float(input("Digite a distância (km): "))
    horas = int(input("Digite as horas: "))
    minutos = int(input("Digite os minutos: "))

    viagem = Viagem(distancia, horas, minutos)

    velocidade = viagem.calcular_velocidade_media()

    print(f"Velocidade média: {velocidade:.2f} km/h")


if __name__ == "__main__":
    main()