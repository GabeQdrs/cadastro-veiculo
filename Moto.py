from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cilindradas):
        super().__init__(marca, modelo, placa, ano)
        self.__cilindradas = cilindradas
    def __str__(self):
        retornoMoto = super().__str__()
        return f'''{retornoMoto}
 - Cilindradas: {self.__cilindradas}'''


