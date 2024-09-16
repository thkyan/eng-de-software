filmes = ['O Poderoso Chefão (1972)','Interestelar (2014)','A Vida é Bela (1997) ','Vingadores: Ultimato (2019)','Forrest Gump (1994) ']

print("Seja bem-vindo! avalie os filmes a seguir de 1 a 5. (Digite '0' se quiser parar!)")
print('')
for filme  in filmes:
    classificacao = int(input(f' De 1 a 5, qual nota você avalia esse filme: {filme} '))
    
    if classificacao == 0:
        print(' é uma pena que queira parar de avaliar nossos filmes! obrigado!')
        break



    if classificacao < 1 or classificacao > 5:
        print('Digite uma nota valida, de 1 a 5!')
    else:
        print(f'Você avaliou o filme {filme} com a nota: {classificacao}!')
