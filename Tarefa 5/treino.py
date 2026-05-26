from datetime import datetime, timedelta
class Treino:
    def __init__(self, id:int, dt: datetime, ds:float, t:timedelta):
        self.__id = id
        self.__data = dt
        self.__distancia = ds
        self.__tempo = t

# GETTERS
    def get_id(self):
        return self.__id
        
    def get_data(self):
        return self.__data
        
    def get_distancia(self):
        return self.__distancia

    def get_tempo(self):
        return self.__tempo
    
# SETTERS
    def set_id(self, id):
        self.__id = id

    def set_data(self, dt):
        self.__data = dt

    def set_distancia(self, ds):
        self.__distancia = ds
        
    def set_tempo(self, t):
        self.__tempo = t
    
    
    # Método Pace
    def pace(self):
        segundos = self.__tempo.total_seconds()
        pace_segundos = segundos / self.__distancia

        minutos = int(pace_segundos // 60)
        segundos_restantes = int(pace_segundos % 60)

        return f"{minutos}min {segundos_restantes}s por km"
    
    def __str__(self):
        return f"Treino {self.__id}: Data: {self.__data.strftime('%d/%m/%Y')}, Distância: {self.__distancia} km, Tempo: {self.__tempo}, Pace: {self.pace()}"
    
    class TreinoUI:
        @staticmethod
        def main():
            while True:
                print("==== MENU =====")
                print("1. Cadastrar Treino")
                print("2. Sair")