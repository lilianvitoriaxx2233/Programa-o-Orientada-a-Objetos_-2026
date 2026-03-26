print("Leia os dados de um país:")
class Pais:
    def __init__(self, nome, populacao, area):
        self.nome = nome
        self.populacao = populacao
        self.area = area

    def densidade(self):
        return self.populacao / self.area

# A principal ntrada de dados
nome = input("Digite o nome do país: ")
populacao = int(input("Digite a população: "))
area = float(input("Digite a área em km2: "))

pais = Pais(nome, populacao, area)

print(f"A densidade demográfica do {pais.nome} é de {pais.densidade():.2f} hab/km2")
