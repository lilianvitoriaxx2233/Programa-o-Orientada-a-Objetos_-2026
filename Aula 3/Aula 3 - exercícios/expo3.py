class ContaBancaria:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito realizado com sucesso!")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")

    def mostrar_saldo(self):
        print("Saldo atual:", self.saldo)


# Programa de teste
titular = input("Digite o nome do titular: ")
numero = input("Digite o número da conta: ")
saldo_inicial = float(input("Digite o saldo inicial: "))

conta = ContaBancaria(titular, numero, saldo_inicial)

# Operações
conta.depositar(100)
conta.mostrar_saldo()

conta.sacar(50)
conta.mostrar_saldo()

conta.sacar(1000)  # Teste de saldo insuficiente