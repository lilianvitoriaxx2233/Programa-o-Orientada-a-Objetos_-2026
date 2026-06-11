from datetime import datetime
class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distância(distancia)
        self.set_tempo(tempo)
    def set_id(self, id):
        if id <= 0:
            print("ID deve ser um número positivo.")
        else:
            self.id = id
    def set_data(self, data):
        try:
            self.data = datetime.strptime(data, "%Y-%m-%d")
        except:
            print("A data deve estar no formato proposto")

    def set_distancia(self, distancia):
        if distancia <= 0:
            print("A distância deve ser um número positivo.")
        else:
            self.distancia = distancia

    def set_tempo(self, tempo):
        if tempo <= 0:
            print("O tempo deve ser positivo")
        else:
            self.tempo = tempo
    
    def get_id(self):
        return self.id
    def get_data(self):
        return self.data
    def get_distancia(self):
        return self.distancia
    def get_tempo(self):
        return self.tempo
    
    def __str__(self):
        return f"ID: {self.id}, Data: {self.data.strftime('%Y-%m-%d')}, Distância: {self.distancia} km, Tempo: {self.tempo} min"
    

class TreinoUI:
    treinos = []

    @staticmethod

    def menu():
        print("1 - Inserir um novo treino")
        print("2 - Listar todos os treinos")
        print("3 - Listar um treino específico")
        print("4 - Atualizar dados de um treino")
        print("5 - Excluir um treino")
        print("6- Encontrar o treino mais rápido/velocidade")
        print("9 - Sair")
    
        return int(input("Opção: "))
    @staticmethod
    def inserir():
        id = int(input("ID: "))
        data = input("Data: ")
        distancia = float(input("Distância (km): "))
        tempo = float(input("Tempo (min): "))
        treino = Treino(id, data, distancia, tempo)
        TreinoUI.treinos.append(treino)
    @staticmethod
    def listar():
        for treino in TreinoUI.treinos:
            print(treino)
    @staticmethod
    def listar_id():
        id = int(input("ID do treino: "))
        for treino in TreinoUI.treinos:
            if treino.get_id() == id:
                print(treino)
                return
        print("Treino não encontrado.")
    @staticmethod
    def atualizar():
        id = int(input("ID do treino: "))
        for treino in TreinoUI.treinos:
            if treino.get_id() == id:
                data = input("Nova data: ")
                distancia = float(input("Nova distância (km): "))
                tempo = float(input("Novo tempo (min): "))
                treino.set_data(data)
                treino.set_distancia(distancia)
                treino.set_tempo(tempo)
                print("Treino atualizado.")
                return
        print("Treino não encontrado.")
    @staticmethod
    def excluir():
        id = int(input("ID do treino: "))
        for treino in TreinoUI.treinos:
            if treino.get_id() == id:
                TreinoUI.treinos.remove(treino)
                print("Treino excluído.")
                return
        print("Treino não encontrado.")
    @staticmethod
    def MaisRapido():
        if not TreinoUI.treinos:
            print("Nenhum treino cadastrado.")
            return
        mais_rapido = TreinoUI.treinos[0]
        for treino in TreinoUI.treinos:
            if treino.get_velocidade() > mais_rapido.get_velocidade():
                mais_rapido = treino
        print("Treino mais rápido:")
        print(mais_rapido)
    @staticmethod
    def main():
        while True:
            opcao = TreinoUI.menu()
            if opcao == 1:
                TreinoUI.inserir()
            elif opcao == 2:
                TreinoUI.listar()
            elif opcao == 3:
                TreinoUI.listar_id()
            elif opcao == 4:
                TreinoUI.atualizar()
            elif opcao == 5:
                TreinoUI.excluir()
            elif opcao == 6:
                TreinoUI.MaisRapido()
            elif opcao == 9:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
TreinoUI.main()