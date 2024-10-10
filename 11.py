import sqlite3

#criando tabela
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS produtos(
id INTEGER PRIMARY KEY,
nome TEXT NOT NULL,
preco REAL NOT NULL,
estoque INTEGER
);"""
cursor.execute(create_table)

#adicionar produto
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()

novo_produto = ('blusa', 20.00, 30)

inserir_produto = 'INSERT INTO produtos (nome, preco, estoque) values (?, ?, ?)'
cursor.execute(inserir_produto, novo_produto)

conn.commit()

conn.close()

#vizualizar produto
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()

selecionar_produto = 'SELECT * FROM produtos'

cursor.execute(selecionar_produto)

produtos = cursor.fetchall()
for produto in produtos:
    print(produto)

conn.close()

#modificar produto
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()

novo_preco = 24.99
produto_id = 1

atualizar_preco = 'UPDATE produtos SET preco = ? WHERE id = ?'

cursor.execute(atualizar_preco, (novo_preco, produto_id))

conn.commit()
conn.close()