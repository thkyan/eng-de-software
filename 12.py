import sqlite3
#criando a tabela
conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Contatos (
        nome TEXT,
        numero TEXT,
        email TEXT
    )
''')

dados_contatos = [
    ('Thiago', 89-98111-1180, 'thiagoriben@gmail.com'),
    ('Thayná', 89-98111-1180, 'thaynamatos956@gmail.com'),
    ('Gabriel', 89-98111-1180, 'thaynamatos958@gmail.com')
]

cursor.executemany('INSERT INTO Contatos (nome, numero, email) VALUES(?, ?, ?)', dados_contatos)

conn.commit()


cursor.execute('SELECT * FROM Contatos')
contatos = cursor.fetchall()
print('Contatos:')
for contato in contatos:
    print(contato)

# #adicionar contato
# conn = sqlite3.connect("contatos.db")
# cursor = conn.cursor()

# novo_contato = ('Simone', 89-98138-3234, 'simonematos7@gmail.com')
# inserir_produto = 'INSERT INTO Contatos(nome, numero, email) VALUES(?, ?, ?)'

# cursor.execute(inserir_produto, novo_contato)
# conn.commit
# conn.close




