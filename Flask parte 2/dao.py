from models import Usuario, Jogo

SQL_DELETA_JOGO = "delete from jogo where id = '{}'"
SQL_JOGO_POR_ID = "SELECT id, nome, categoria, console from jogo where id = '{}'"
SQL_USUARIO_POR_ID = "SELECT id, nome, senha from usuario where id = '{}'"
SQL_ATUALIZA_JOGO = "UPDATE jogo SET nome='{}', categoria='{}', console='{}' where id = '{}'"
SQL_BUSCA_JOGOS = "SELECT id, nome, categoria, console from jogo"
SQL_CRIA_JOGO = "INSERT into jogo (nome, categoria, console) values ('{}', '{}', '{}')"
SQL_CRIA_RETORNA_ID = "SELECT max(id) as id from jogo"


class JogoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, jogo):
        cursor = self.__db.cursor()

        if (jogo.id):
            cursor.execute(SQL_ATUALIZA_JOGO.format(jogo.nome, jogo.categoria, jogo.console, jogo.id))
        else:
            #print(SQL_CRIA_JOGO.format(jogo.nome, jogo.categoria, jogo.console))
            cursor.execute(SQL_CRIA_JOGO.format(jogo.nome, jogo.categoria, jogo.console))
            jogo.id = cursor.execute(SQL_CRIA_RETORNA_ID).fetchone().id
            #print(jogo.id, jogo.nome, jogo.categoria, jogo.console)
        self.__db.commit()
        return jogo

    def listar(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_BUSCA_JOGOS)
        jogos = traduz_jogos(cursor.fetchall())
        return jogos

    def busca_por_id(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_JOGO_POR_ID.format(id))
        tupla = cursor.fetchone()
        return Jogo(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def deletar(self, id):
        self.__db.cursor().execute(SQL_DELETA_JOGO.format(id))
        self.__db.commit()


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_USUARIO_POR_ID.format(id))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        #print(f'AQUI usuario:  {usuario.nome}. senha: {usuario.senha}, id: {usuario.id}')
        return usuario


def traduz_jogos(jogos):
    def cria_jogo_com_tupla(tupla):
        return Jogo(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(cria_jogo_com_tupla, jogos))


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])
