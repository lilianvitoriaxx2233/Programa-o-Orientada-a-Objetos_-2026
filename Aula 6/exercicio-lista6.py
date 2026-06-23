class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"
    
    def ToJson(self):
        return {"id" : self.id, "nome" : self.nome, "email" : self.email, "fone" : self.fone }
    
    #Cria um objeto Cliente a partir de um dicionário
    @staticmethod
    def FromJson(data):
        return Cliente(data["id"], data["nome"], data["email"], data["fone"])
    
    def get_id(self):
        return self.id
    def get_nome(self):
        return self.nome
    def get_email(self):
        return self.email
    def get_fone(self):
        return self.fone
    
    def set_id(self, id):
        self.id = id
    def set_nome(self, nome):
        self.nome = nome
    def set_email(self, email):
        self.email = email
    def set_fone(self, fone):
        self.fone = fone

class ClienteUI:
    clientes = []
    @staticmethod
    def main():
        op = -1
        while op!= 0:
            print("1 - Cadastrar Cliente")
            print("2 - Listar Clientes")
            print("3 - Buscar Cliente por ID")
            print("4 - Atualizar Cliente")
            print("5 - Deletar Cliente")
            print("0 - Sair")
            op = int(input("Digite a opção: "))
            if op == 1:
                ClienteUI.inserir()
            elif op == 2:
                ClienteUI.listar_clientes()
            elif op == 3:
                ClienteUI.listar_id()
            elif op == 4:
                ClienteUI.atualizar_cliente()
            elif op == 5:
                ClienteUI.deletar_cliente()
            elif op == 0:
                print("Sair")
            else:
                print("Opção inválida")
    @staticmethod
    def menu():
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Buscar Cliente por ID")
        print("4 - Atualizar Cliente")
        print("5 - Deletar Cliente")
        print("0 - Sair")
        return int(input("Digite a opção: "))
    
    @staticmethod
    def inserir():
        id = int(input("Digite o ID do cliente: "))
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o email do cliente: ")
        fone = input("Digite o telefone do cliente: ")
        cliente = Cliente(id, nome, email, fone)
        ClienteUI.clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")
    
    @staticmethod
    def listar():
        if len(ClienteUI.clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in ClienteUI.clientes:
                print(cliente)
    @staticmethod
    def listar_id():
        id = int(input("Digite o ID do cliente: "))
        for cliente in ClienteUI.clientes:
            if cliente.get_id() == id:
                print(cliente)
                return
        print("Cliente não encontrado.")
    @staticmethod
    def atualizar():
        id = int(input("Digite o ID do cliente: "))
        for cliente in ClienteUI.clientes:
            if cliente.get_id() == id:
                nome = input("Digite o novo nome do cliente: ")
                email = input("Digite o novo email do cliente: ")
                fone = input("Digite o novo telefone do cliente: ")
                cliente.set_nome(nome)
                cliente.set_email(email)
                cliente.set_fone(fone)
                print("Cliente atualizado com sucesso!")
                return
        print("Cliente não encontrado.")
    @staticmethod
    def excluir():
        id = int(input("Digite o ID do cliente: "))
        for cliente in ClienteUI.clientes:
            if cliente.get_id() == id:
                ClienteUI.clientes.remove(cliente)
                print("Cliente excluído com sucesso!")
                return
        print("Cliente não encontrado.")
ClienteUI.main()