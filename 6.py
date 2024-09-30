class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        
    def cumprimentar(self):
        return f"Olá, tudo bem? Me chamo {self.nome}!"
    
    def aniversario(self):
        self.idade += 1


pessoa1 = Pessoa("Thayná", 18, "Feminino")
# print(pessoa1.cumprimentar())   
# print(f"Idade: {pessoa1.idade}")  

pessoa1.aniversario()
# print(f"Idade nova: {pessoa1.idade}")



class Animal:
    def __init__(self, nome):
        self.nome = nome
    def fazer_barulho(self):
        pass
class Cachorro(Animal):
    def fazer_barulho(self):
        return "AuAu"
class Gato(Animal):
    def fazer_barulho(self):
        return "Miau"
    
jully = Cachorro("jully")
gata = Gato("gata")

# print(f"{jully.nome} faz: {jully.fazer_barulho()}")
# print(f"{gata.nome} faz: {gata.fazer_barulho()}")