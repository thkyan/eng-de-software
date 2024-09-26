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
print(pessoa1.cumprimentar())   
print(f"Idade: {pessoa1.idade}")  

pessoa1.aniversario()
print(f"Idade nova: {pessoa1.idade}")