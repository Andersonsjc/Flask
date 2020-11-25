import pyodbc
#import MySQLdb
datasource = f'DSN=Sybase_BDI'
print('Conectando...')
#conn = MySQLdb.connect(user='root', passwd='admin', host='127.0.0.1', port=3306)
conn = pyodbc.connect(datasource)

# Descomente se quiser desfazer o banco...
conn.cursor().execute("DROP table jogo;")
conn.cursor().execute("DROP table usuario;")

criar_tabelas = '''
   CREATE TABLE jogo(
      id integer default autoincrement primary key,
      nome varchar(50) NOT NULL,
      categoria varchar(40)  NOT NULL,
      console varchar(20) NOT NULL
    ) ;
    CREATE TABLE usuario (
      id varchar(8) default autoincrement primary key,
      nome varchar(20)  NOT NULL,
      senha varchar(8)  NOT NULL
    ) ;'''

conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.execute(
      "INSERT INTO usuario (id, nome, senha) VALUES ('luan', 'Luan Marques', 'flask'); INSERT INTO usuario (id, nome, senha) VALUES ('nico', 'Nico', '7a1'); INSERT INTO usuario (id, nome, senha) VALUES ('danilo', 'Danilo', 'vegas');")

cursor.execute('select * from usuario')
print(' -------------  Usuarios:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
cursor.execute(
      "INSERT INTO jogo (nome, categoria, console) VALUES ('God of War 4', 'Acao', 'PS4'); INSERT INTO jogo (nome, categoria, console) VALUES ('NBA 2k18', 'Esporte', 'Xbox One'); INSERT INTO jogo (nome, categoria, console) VALUES ('Rayman Legends', 'Indie', 'PS4'); INSERT INTO jogo (nome, categoria, console) VALUES ('Super Mario RPG', 'RPG', 'SNES'); INSERT INTO jogo (nome, categoria, console) VALUES ('Super Mario Kart', 'Corrida', 'SNES'); INSERT INTO jogo (nome, categoria, console) VALUES ('Fire Emblem Echoes', 'Estrategia', '3DS'); "
      )

cursor.execute('select * from jogo')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando senao nada tem efeito
conn.commit()
cursor.close()
