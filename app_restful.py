from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, Habilidade
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'Pedro',
        'habilidades': ['Python', 'Flask', 'Java']
     },
    {
        'id': 1,
        'nome': 'Rafael',
        'habilidades': ['Python', 'Django']
    }
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'Erro', 'mensagem': 'Desenvolvedor de ID {} não existe.'.format(id)}
        except Exception:
            response = {'status': 'Erro', 'mensagem': 'Erro desconhecido, procure o ADM da API.'}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'Sucesso', 'mensagem': 'Registro excluído.'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(Habilidade, '/habilidade/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)
