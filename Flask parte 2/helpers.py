from os import path, listdir, remove
from jogateca import app

def recupera_imagem(id):
    for nome_arquivo in listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    remove(path.join(app.config['UPLOAD_PATH'], arquivo))
