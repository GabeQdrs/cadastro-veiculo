from Veiculo import Veiculo
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, placa, ano, carga):
        super().__init__(marca, modelo, placa, ano)
        self.__carga = carga
    def __str__(self):
        retornoCaminhao = super().__str__()
        return f'''{retornoCaminhao}
 - Capacidade de Carga: {self.__carga}'''
    

fh540 = Caminhao("Volvo", "FH540", "abc123", 1993, 80000)

print(Caminhao)    
