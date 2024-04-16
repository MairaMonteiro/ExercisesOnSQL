#import do datbase
import sqlite3
import random
#conexão com o banco
conexao = sqlite3.connect('exerciciosql')
cursor = conexao.cursor()
#Deleta a tabela quando necessário
cursor.execute('DROP TABLE IF EXISTS clientes')

#Questão 1 do exercício
cursor.execute('CREATE TABLE alunos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(200), idade INT, curso VARCHAR(50))')


#Questão 2 do exercício
alunos_exemplos = [
    ('João Silva', 20, 'Engenharia Civil'),
    ('Maria Oliveira', 22, 'Medicina'),
    ('Pedro Santos', 19, 'Direito'),
    ('Ana Costa', 18, 'Administração'),
    ('Lucas Pereira', 21, 'Engenharia de Software'),
    ('Carla Rodrigues', 23, 'Psicologia'),
    ('Gabriel Almeida', 17, 'Arquitetura'),
    ('Juliana Lima', 20, 'Biologia'),
    ('Mateus Souza', 24, 'Economia'),
    ('Larissa Ferreira', 18, 'Nutrição'),
    ('Rafael Gonçalves', 22, 'Jornalismo'),
    ('Amanda Martins', 20, 'História'),
    ('Daniel Barbosa', 25, 'Medicina Veterinária'),
    ('Bruna Santos', 16, 'Engenharia Elétrica'),
    ('Guilherme Oliveira', 26, 'Artes Visuais'),
    ('Fernanda Lima', 19, 'Fisioterapia'),
    ('Diego Costa', 27, 'Letras'),
    ('Camila Alves', 17, 'Engenharia Mecânica'),
    ('Thiago Silva', 28, 'Ciência da Computação'),
    ('Carolina Pereira', 15, 'Administração')
]
cursor.executemany('INSERT INTO alunos(nome, idade, curso) VALUES (?, ?, ?)', alunos_exemplos)


#Questão 3 do exercício
#i
cursor.execute('SELECT * FROM alunos')

#ii
cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')

#iii
cursor.execute('SELECT nome, curso FROM alunos WHERE curso LIKE "%Engenharia%"')

#iv
cursor.execute('SELECT COUNT (*) FROM alunos')


#Questão 4 do exercício
#i
id_aluno = 9
nova_idade = 56
cursor.execute('UPDATE alunos SET idade = ? WHERE id = ?', (nova_idade, id_aluno))

#ii
id_aluno = 20
cursor.execute('DELETE FROM alunos WHERE id = ?', (id_aluno,))


#Questão 5 do exercício
cursor.execute('CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(200), idade INT, saldo REAL)')
clientes_exemplos = [
    ('João', 25, 1077.50),
    ('Maria', 30, 1556.75),
    ('Pedro', 28, 2050.25),
    ('Ana', 35, 1800.00),
    ('Lucas', 22, 1200.00),
    ('Carla', 27, 1350.80),
    ('Gabriel', 33, 2200.45),
    ('Juliana', 29, 1950.60),
    ('Mateus', 26, 1700.25),
    ('Larissa', 31, 2100.90),
    ('Rafael', 24, 1450.70),
    ('Amanda', 37, 2300.50),
    ('Daniel', 32, 25400.75),
    ('Bruna', 23, 1250.40),
    ('Guilherme', 29, 1750.60),
    ('Fernanda', 26, 1850.20),
    ('Diego', 34, 2150.90),
    ('Camila', 31, 1903.75),
    ('Thiago', 28, 2001.30),
    ('Carolina', 30, 18440.45)
]
cursor.executemany('INSERT INTO clientes(nome, idade, saldo) VALUES (?, ?, ?)', clientes_exemplos)


#Questão 6 do exercício
#i
cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

#ii
cursor.execute('SELECT AVG(saldo) FROM clientes')

#iii
cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1')

#iv
cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')


#Questão 7 do exercício
#i
novo_saldo = 15829.33
id_cliente = 23
cursor.execute('UPDATE clientes SET saldo = ? WHERE id = ?', (novo_saldo, id_cliente))

#ii
id_clientes = 33
cursor.execute('DELETE FROM clientes WHERE id = ?', (id_clientes,))
cursor.execute('SELECT COUNT (*) FROM clientes')


#Questão 8 do exercício
cursor.execute('CREATE TABLE compras (id INTEGER PRIMARY KEY AUTOINCREMENT, cliente_id INTEGER, produto VARCHAR(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')
def adicionar_compra(produto, valor, cliente_id): #Função para adicionar uma compra
    cursor.execute('INSERT INTO compras (produto, valor, cliente_id) VALUES (?, ?, ?)', (produto, valor, cliente_id))
    conexao.commit

#Selecionando os ids disponíveis
cursor.execute('SELECT id FROM clientes')
ids_clientes = cursor.fetchall() 

#lista de valores e produtos
produtos = ["Smartphone", "Notebook", "Tablet", "Smartwatch", "Fone de Ouvido", "TV", "Câmera", "Monitor", "Teclado", "Mouse Ópitico"]
valores = [10000.00, 15000.00, 8000.00, 3000.00, 800.00, 2000.00, 500.00, 400.00, 5000.00] 

for i in range(25):
    produto = random.choice(produtos)
    valor = random.choice(valores)
    cliente_id = random.choice(ids_clientes)[0] #Seleciona um id de cliente aleatóriamente
    adicionar_compra(produto, valor, cliente_id)

cursor.execute('''
               SELECT clientes.nome, compras.produto, compras.valor 
               FROM clientes
               JOIN compras on clientes.id = compras.cliente_id
               ''')

#imprime os resultados
resultados = cursor.fetchall()
for i in resultados:
    print(i)

conexao.commit()
conexao.close()