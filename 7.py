class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, descremento):
        self.velocidade -= descremento 

    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h"
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia

    def acelerar(self, incremento):
        self.velocidade += incremento + self.potencia

carro1 = Carro("Toyota", "Corolla", 2022, 150)
carro1.acelerar(45)

print(f"Marca: {carro1.marca}, Modelo: {carro1.modelo}, Ano: {carro1.ano}, Velocidade: {carro1.velocidade}")