from datetime import datetime
class Paciente:
    def __init__(self, id, nome, cpf, telefone, nascimento):
        self.set_id(id)
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)
    def set_id(self, id):
        if id < 0:
            raise ValueError("ID deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def set_cpf(self, cpf):
        if cpf == "":
            raise ValueError("CPF não pode ser vazio")
        self.__cpf = cpf
    def set_telefone(self, telefone):
        if telefone == "":
            raise ValueError("Telefone não pode ser vazio")
        self.__telefone = telefone
    def set_nascimento(self, nascimento):
        if nascimento > datetime.now():
            raise ValueError("Data de nascimento não pode ser no futuro")
        self.__nascimento = nascimento
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_telefone(self):
        return self.__telefone
    def get_nascimento(self):
        return self.__nascimento
    def __str__(self):
        return (f"ID: {self.get_id()}"
                f"Nome: {self.get_nome()}"
                f"CPF: {self.get_cpf()}"
                f"Telefone: {self.get_telefone()}"
                f"Nascimento: {self.get_nascimento().strftime('%d/%m/%Y')}")
    def idade(self):
        tempo = datetime.now() - self.get_nascimento() #medido em dias, horas, .... timedelta
        anos = tempo.days // 365
        meses = (tempo.days % 365) // 30
        return f"{anos} anos e {meses} meses"
    
"""x = Paciente(1, "João José", "123.456.789-00", "(11) 99999-9999", datetime(2009, 10, 28))
print(x)
print(x.idade())"""""

class PacienteUI: 
    __paciente = [] #atributo - fora do init - não tem objetos de PacienteUI, é da classe, é compartilhado por todos os objetos de PacienteUI
    @staticmethod
    def main():
        while op != 9 :
            op = PacienteUI.menu()
            if op == 1:
                PacienteUI.inserir()
            if op == 2:
                PacienteUI.listar()
            elif op == 4:
                PacienteUI.excluir()
            elif op == 5:
                PacienteUI.pesquisar()
            elif op == 6:
                PacienteUI.aniversariante()
    @staticmethod #quando não acessa um atributo da classe, ou seja, não tem self, pode ser staticmethod
    def menu():
        print("1- Inserir, 2- Listar, 3- Sair, 4- excluir, 5-Pesquisar, 6- Aniversariante, 9- Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def inserir():
        id = int(input("Informe o ID: "))
        nome = input("Informe o nome: ")
        cpf = input("Informe o CPF: ")
        telefone = input("Informe o telefone: ")
        nascimento = input("Informe a data de nascimento (dd/mm/yyyy): ")
        nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
        paciente = Paciente(id, nome, cpf, telefone, nascimento)
        PacienteUI.__paciente.append(paciente)

    @staticmethod
    def listar():
        if len(PacienteUI.__paciente) == 0:
            print("Nenhum paciente cadastrado")
        else:
            for paciente in PacienteUI.__paciente:
                print((paciente))
    @staticmethod
    def excluir():
        id = int(input("Informe o ID do paciente a ser excluído: "))
        for paciente in PacienteUI.__paciente:
            if paciente.get_id() == id:
                PacienteUI.__paciente.remove(paciente)
                print("Paciente excluído com sucesso")
                return
        print("Paciente não encontrado")
    @staticmethod
    def pesquisar():
        id = int(input("Informe o ID do paciente a ser pesquisado: "))
        for paciente in PacienteUI.__paciente:
            if paciente.get_id() == id:
                print(paciente)
                return
        print("Paciente não encontrado")
    @staticmethod
    def aniversariante():
        mes = int(input("Informe o mês de nascimento dos pacientes a serem listados: "))
        for paciente in PacienteUI.__paciente:
            if paciente.get_nascimento().month == mes:
                print(paciente)
PacienteUI.main()