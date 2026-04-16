# Entidade
class Triangulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2
    
# ----------- CIRCULO --------------
import math

class Circulo:
    def __init__(self):
        self.__raio = 0.0

    def set_raio(self, r):
        if r >= 0:
            self.__raio = r

    def get_raio(self):
        return self.__raio

    def calc_area(self):
        return math.pi * self.__raio ** 2

    def calc_circunferencia(self):
        return 2 * math.pi * self.__raio


# ------------------ VIAGEM ------------------
class Viagem:
    def __init__(self):
        self.__distancia = 0.0
        self.__tempo = 0.0

    def set_distancia(self, d):
        self.__distancia = d

    def set_tempo(self, t):
        self.__tempo = t

    def get_distancia(self):
        return self.__distancia

    def get_tempo(self):
        return self.__tempo

    def velocidade_media(self):
        if self.__tempo > 0:
            return self.__distancia / self.__tempo
        return 0


# ------------------ CONTA BANCÁRIA ------------------
class Conta:
    def __init__(self):
        self.__nome = ""
        self.__numero = ""
        self.__saldo = 0.0

    def set_nome(self, n):
        self.__nome = n

    def set_numero(self, num):
        self.__numero = num

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

    def get_saldo(self):
        return self.__saldo


# ------------------ INGRESSO ------------------
class Ingresso:
    def __init__(self):
        self.__dia = ""
        self.__hora = 0

    def set_dia(self, d):
        self.__dia = d.lower() #lower tem a função de converter a string para minúscula (pesquisei isso na internet)

    def set_hora(self, h):
        self.__hora = h

    def calc_valor(self):
        # valores base
        if self.__dia in ["segunda", "terça", "quinta"]:
            valor = 16
        elif self.__dia == "quarta":
            valor = 8
        else:
            valor = 20

        # adicional noturno
        if self.__hora >= 17:
            valor *= 1.5

        return valor


# ------------------ UI ------------------
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo() #op significa opção, ou seja, se o usuário escolher a opção 1, a função triangulo() será chamada para calcular a área do triângulo.
            if op == 2: UI.circulo()
            if op == 3: UI.viagem()
            if op == 4: UI.conta()
            if op == 5: UI.ingresso()

    @staticmethod
    def menu(): 
        print("\n1-Triângulo 2-Círculo 3-Viagem 4-Conta Bancária 5-Ingresso 9-Fim") #\n tem a função de pular uma linha, ou seja, deixar um espaço entre as opções do menu.
        return int(input("Escolha uma opção: "))

    @staticmethod
    def triangulo():
        print("Cálculo da área de um triângulo")
        x = Triangulo()
        x.set_base(float(input("Base: ")))
        x.set_altura(float(input("Altura: ")))
        print("Área =", x.calc_area())

    @staticmethod
    def circulo():
        print("Cálculo do círculo")
        c = Circulo()
        c.set_raio(float(input("Raio: ")))
        print("Área =", c.calc_area())
        print("Circunferência =", c.calc_circunferencia())

    @staticmethod
    def viagem():
        print("Cálculo da velocidade média")
        v = Viagem()
        v.set_distancia(float(input("Distância (km): ")))
        v.set_tempo(float(input("Tempo (h): ")))
        print("Velocidade média =", v.velocidade_media(), "km/h")

    @staticmethod
    def conta():
        print("Conta Bancária")
        c = Conta()
        c.set_nome(input("Nome: "))
        c.set_numero(input("Número da conta: "))
        valor = float(input("Depósito inicial: "))
        c.depositar(valor)
        saque = float(input("Valor para saque: "))
        c.sacar(saque)

        print("Saldo final =", c.get_saldo())

    @staticmethod
    def ingresso():
        print("Entrada de cinema")
        i = Ingresso()
        i.set_dia(input("Dia da semana: "))
        i.set_hora(int(input("Hora (0-23): ")))
        print("Valor do ingresso = R$", i.calc_valor())

# parte de inicialização do programa
UI.main()
