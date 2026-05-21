from datetime import datetime
from enum import Enum


class Pagamento(Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 3


class Boleto:

    def __init__(self, codigo, emissao, vencimento, valor):
        self.codBarras = codigo
        self.dataEmissao = emissao
        self.dataVencimento = vencimento
        self.dataPago = None
        self.valorBoleto = valor
        self.valorPago = 0

    def Pagar(self, valor):

        if self.valorPago + valor <= self.valorBoleto:

            self.valorPago += valor
            self.dataPago = datetime.now()

    def Situacao(self):

        if self.valorPago == 0:
            return Pagamento.EmAberto

        elif self.valorPago < self.valorBoleto:
            return Pagamento.PagoParcial

        else:
            return Pagamento.Pago

    def __str__(self):

        return (f"Código: {self.codBarras}"
                f"Valor: R${self.valorBoleto}"
                f"Pago: R${self.valorPago}"
                f"Situação: {self.Situacao().name}"
                f"Vencimento: {self.dataVencimento.strftime('%d/%m/%Y')}\n")


class BoletoUI:

    boletos = []

    @staticmethod
    def Menu():

        print("1-Inserir")
        print("2-Listar")
        print("3-Atualizar")
        print("4-Excluir")
        print("5-Boletos em aberto")
        print("6-Boletos pagos")
        print("7-Boletos a vencer")
        print("8-Boletos vencidos")
        print("9-Pagar boleto")
        print("0-Sair")

        return int(input("Opção: "))

    @staticmethod
    def Inserir():

        codigo = input("Código: ")

        emissao = input("Emissão (dd/mm/aaaa): ")
        emissao = datetime.strptime(emissao,"%d/%m/%Y")

        venci = input("Vencimento (dd/mm/aaaa): ")
        venci = datetime.strptime(venci,"%d/%m/%Y")

        valor = float(input("Valor: "))

        boleto = Boleto(codigo, emissao, venci, valor)

        BoletoUI.boletos.append(boleto)

        print("Boleto cadastrado!")

    @staticmethod
    def Listar():

        for b in BoletoUI.boletos:
            print(b)

    @staticmethod
    def Atualizar():

        codigo = input("Código do boleto: ")

        for b in BoletoUI.boletos:

            if b.codBarras == codigo:

                novo = float(input("Novo valor: "))

                b.valorBoleto = novo

                print("Atualizado!")
                return

        print("Não encontrado.")

    @staticmethod
    def Excluir():

        codigo = input("Código: ")

        for b in BoletoUI.boletos:

            if b.codBarras == codigo:

                BoletoUI.boletos.remove(b)

                print("Excluído!")
                return

        print("Não encontrado.")

    @staticmethod
    def BoletosEmAberto():

        for b in BoletoUI.boletos:

            if b.Situacao() == Pagamento.EmAberto:

                print(b)

    @staticmethod
    def BoletosPagos():

        for b in BoletoUI.boletos:

            if b.valorPago > 0:

                print(b)

    @staticmethod
    def BoletosAVencer():

        hoje = datetime.now()

        for b in BoletoUI.boletos:

            if b.dataVencimento >= hoje and b.Situacao() != Pagamento.Pago:

                print(b)

    @staticmethod
    def BoletosVencidos():

        hoje = datetime.now()

        for b in BoletoUI.boletos:

            if b.dataVencimento < hoje and b.Situacao() != Pagamento.Pago:

                print(b)

    @staticmethod
    def PagarBoleto():

        codigo = input("Código: ")

        for b in BoletoUI.boletos:

            if b.codBarras == codigo:

                valor = float(input("Valor pago: "))

                b.Pagar(valor)

                print("Pagamento registrado!")
                return

        print("Boleto não encontrado.")

    @staticmethod
    def Main():

        while True:

            op = BoletoUI.Menu()

            if op == 1:
                BoletoUI.Inserir()

            elif op == 2:
                BoletoUI.Listar()

            elif op == 3:
                BoletoUI.Atualizar()

            elif op == 4:
                BoletoUI.Excluir()

            elif op == 5:
                BoletoUI.BoletosEmAberto()

            elif op == 6:
                BoletoUI.BoletosPagos()

            elif op == 7:
                BoletoUI.BoletosAVencer()

            elif op == 8:
                BoletoUI.BoletosVencidos()

            elif op == 9:
                BoletoUI.PagarBoleto()

            elif op == 0:

                print("Saindo...")
                break

            else:

                print("Opção inválida.")


BoletoUI.Main()