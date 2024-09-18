# texto = "Me chamo Thayná e estou aprendendo a linguagem Python!"

# print(f"O tamanho do texto é: {len(texto)}")
# print(f"Python no texto: {'Python' in texto}")
# print(f"Quantidade de a no texto: {texto.count('a')}")
# print(f"As 5 primeiras letras do texto são: {texto[:5]}")




# cores = ['rosa', 'azul', 'verde', 'amarelo']

# for cor in cores:
#     print(f"Posição = {cores.index(cor)}, cor = {cor}")





# nomes = ['Thayná', 'Thiago']
# print(nomes)
# nomes_minusculo = list(map(str.lower, nomes)) #(nome.lower() for nome in nomes)
# print(nomes_minusculo)



# preco_dolar = [100, 40, 60, 30]
# taxa_de_cambio = 5.25
# preco_em_real = list(map(lambda x : x * taxa_de_cambio, preco_dolar))
# print(preco_em_real)


# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
# print(numeros_pares)



#tuplas
# vogais = ('a', 'e', 'i', 'o', 'u')
# print(f'tipo de objeto de vogais = {type(vogais)}')
# for vogal in vogais:
#     print(vogal)
# for p, x in enumerate(vogais):
#     print(f"Posição = {p}, Valor = {x}")




convidados = ('Thayná', 'Thiago', 'Gabriel', 'Lorrany', 'Larice')

confirmados = ['Gabriel', 'Lorrany']

for convidado in convidados:
    if convidado is not confirmados:
        print(f"{convidado} não foi confirmado!")