from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, ano, n_portas):
        super().__init__(marca, modelo, placa, ano)
        self.__n_portas = n_portas
    def __str__(self):
        retornoCarro = super().__str__()
        return f'''{retornoCarro}
 - Num. Portas: {self.__n_portas}'''