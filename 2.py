valor_produto = float(input("Insira o valor do produto: "))
porcentual_desconto = float(input("Insira a porcentagem que foi descontado: "))

if porcentual_desconto < 0 or porcentual_desconto > 100:
    print("Erro! o desconto só é valido de 0 a 100%...")
else:
    desconto = valor_produto * (porcentual_desconto/100)

valor_final = valor_produto - desconto

print(f"O valor descontado foi: R${valor_final}")