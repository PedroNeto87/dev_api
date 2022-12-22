from flask import request
from flask_restful import Resource
import json

lista_habilidades = ['Python', 'Java', 'Flask']


class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        if dados not in lista_habilidades:
            lista_habilidades.append(dados)
        else:
            return {'mensagem': 'Habilidade já cadastra.'}
        return lista_habilidades


class Habilidade(Resource):
    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados

    def delete(self, id):
        try:
            lista_habilidades.pop(id)
            return {'status': 'Sucesso', 'mensagem': 'Registro excluído.'}
        except IndexError:
            return {'status': 'Erro', 'mensagem': 'Registro informado ID {} não existe.'.format(id)}
