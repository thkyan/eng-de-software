import numpy as np

# my_array = np.array([1, 2, 3, 4, 5])
# print('array original:')
# print(my_array)

# elevar_ao_quadrado = my_array**2
# print(elevar_ao_quadrado)
# somar_elementos = np.sum(my_array)
# print(somar_elementos)


participantes = [
    {
    'nome': 'julia',
    'localização': 'brasil',
    'afiliação': 'universidade A',
    'interesses': ['ciencias', 'fisica']

    },
    {
        'nome': 'ana',
        'localização': 'argentina',
        'afliação': 'instituto B',
        'interesses': ['ciencias','quimica']
    },
    {
        'nome': 'joão',
        'localização': 'usa',
        'afiliação': 'universidade C',
        'interesses': ['ciencias', 'quimica']
    }
]

regioes = set(participante['localização'] for participante in participantes)
afiliacoes = {}

for participante in participantes:
    afiliacao = participante['afiliação']
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
    afiliacoes[afiliacao].append(participante['nome'])

areas_de_interesse = np.array([interesse['interesses'] for interesse in participantes])
interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts= True)
area_mais_popular = interesses_unicos[np.argmax(contagem)]

print('Regioes dos participantes', regioes)
print('Afliações do participantes:')
for afiliacao, nome in afiliacoes.intem():
    print(f'{afiliacao}: {','.join(nome)}')
print('Area mais popular:', area_mais_popular)