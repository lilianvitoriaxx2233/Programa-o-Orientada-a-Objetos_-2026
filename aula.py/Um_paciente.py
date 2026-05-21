from datetime import datetime
class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.nascimento = nascimento

    def idade(self):
        hoje = datetime.now()

        anos = hoje.year - self.nascimento.year
        meses = hoje.month - self.nascimento.month

        if hoje.day < self.nascimento.day:
            meses -= 1

        if meses < 0:
            anos -= 1
            meses += 12

        return f"{anos} anos e {meses} meses"

    def __str__(self):
        return (f"Nome: {self.nome}"
                f"CPF: {self.cpf}"
                f"Telefone: {self.telefone}"
                f"Idade: {self.idade()}")


class PacienteUI:

    pacientes = []

    @staticmethod
    def Menu():
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("5 - Pesquisar")
        print("6 - Aniversariantes")
        print("0 - Sair")

        return int(input("Escolha: "))

    @staticmethod
    def Inserir():
        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        nasc = input("Nascimento (dd/mm/aaaa): ")

        nascimento = datetime.strptime(nasc,"%d/%m/%Y")

        paciente = Paciente(nome, cpf, telefone, nascimento)

        PacienteUI.pacientes.append(paciente)

        print("Paciente cadastrado!")

    @staticmethod
    def Listar():

        if len(PacienteUI.pacientes) == 0:
            print("Nenhum paciente cadastrado.")
            return

        for p in PacienteUI.pacientes:
            print(p)

    @staticmethod
    def Atualizar():

        nome = input("Nome do paciente: ")

        for p in PacienteUI.pacientes:

            if p.nome.lower() == nome.lower():

                p.nome = input("Novo nome: ")
                p.cpf = input("Novo CPF: ")
                p.telefone = input("Novo telefone: ")

                nasc = input("Nova data (dd/mm/aaaa): ")
                p.nascimento = datetime.strptime(nasc,"%d/%m/%Y")

                print("Atualizado!")
                return

        print("Paciente não encontrado.")

    @staticmethod
    def Excluir():

        nome = input("Nome do paciente: ")

        for p in PacienteUI.pacientes:

            if p.nome.lower() == nome.lower():

                PacienteUI.pacientes.remove(p)

                print("Paciente removido.")
                return

        print("Paciente não encontrado.")

    @staticmethod
    def Pesquisar():

        letras = input("Iniciais do nome: ").lower()

        for p in PacienteUI.pacientes:

            if p.nome.lower().startswith(letras):

                print(p)

    @staticmethod
    def Aniversariantes():

        mes = int(input("Digite o mês: "))

        for p in PacienteUI.pacientes:

            if p.nascimento.month == mes:

                print(p.nome)

    @staticmethod
    def Main():

        while True:

            op = PacienteUI.Menu()

            if op == 1:
                PacienteUI.Inserir()

            elif op == 2:
                PacienteUI.Listar()

            elif op == 3:
                PacienteUI.Atualizar()

            elif op == 4:
                PacienteUI.Excluir()

            elif op == 5:
                PacienteUI.Pesquisar()

            elif op == 6:
                PacienteUI.Aniversariantes()

            elif op == 0:
                print("Saindo...")
                break

            else:
                print("Opção inválida.")


PacienteUI.Main()