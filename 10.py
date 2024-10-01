import matplotlib.pyplot as plt

meses = ["janeiro", "feveiro", "março", "abril", "maio"]
vendas = [100, 145, 90, 230, 50]

plt.bar(meses, vendas, color="pink")

plt.xlabel("meses")
plt.ylabel("vendas, de cada mês")
plt.title("Gráfico em barras, vendas em relação dos 5 meses")

plt.show()