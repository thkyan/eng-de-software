# numeros = [1, 2, 3, 4, 6, 6, 8, 7]
# comprimento = len(numeros)
# print(comprimento)



# def soma(a, b):
#     resultado = a + b
#     return resultado

# print(soma(2, 2))



# def e_par(numero):
    
#     if numero % 2 == 0:
#         return True
#     else:
#         return False
    
# numero = int(input('Escolha um numero: '))

# if e_par(numero):
#     print(f"o numero {numero} é par!")
# else:
#     print(f"o numero {numero} é impar!") 

# soma = lambda a, b: a + b
# resultado = soma(3, 5)
# print(resultado)

notas = []

for i in range(4):
    nota = float(input('Insira as 4 notas do aluno: '))
    notas.append(nota)


def calcular_media(notas):
    total = sum(notas)
    media = total/len(notas)
    return media

arrendondar_media = lambda media: round(2)

media = calcular_media(notas)
media_arredondada  = arrendondar_media(media)

situacao = 'aprovado' if media_arredondada >= 7 else 'reprovado'

print(f'a media foi: {media_arredondada}! a sua situação é: {situacao}')