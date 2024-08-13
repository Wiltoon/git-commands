from flask_restx import Resource

class Push(Resource):
    def get(self):
        return {'message': 'Push'}, 200

class Pull(Resource):
    def get(self):
        return {
            'grupo': 'Grupo 2',
            'message': 'Pull'
        }

class Add(Resource):
    def get(self):
        return {
            'grupo': 'Grupo 3',
            'message': 'Add'
        }

class Commit(Resource):
    def get(self):
        return {
            'grupo': 'Grupo 4',
            'message': 'Commit'
        }

class Init(Resource):
    def get(self):
        return {
            'grupo': 'Grupo 5',
            'message': 'Init'
        }

class Clone(Resource):
    def get(self):
        return {
            'grupo': 'Grupo 6',
            'message': 'Clone'
        }

class Checkout(Resource):
    def get(self):
        return {
            'grupo': 'Grupo 7',
            'message': 'Checkout'
        }

class Status(Resource):
    def get(self):
        return {
            'grupo': 'Grupo 8',
            'message': 'Status: exibe as condições do diretório de trabalho e da área de staging. Ele permite que você veja quais alterações foram despreparadas, quais não foram e quais arquivos não estão sendo monitorados pelo Git.'
        }

class Log(Resource):
    def get(self):
        return {
            'grupo': 'Grupo 9',
            'message': 'Log'
        }

class Branch(Resource):
    def get(self):
        return {
            'grupo': 'Grupo 10',
            'message': 'Branch'
        }
    
class Merge(Resource):
    def get(self):
        return {
            'grupo': 'Grupo 11',
            'message': 'Merge'
        }
    
class Rebase(Resource):
    def get(self):
        return {
            'grupo': 'Grupo 12',
            'message': 'Rebase'
        }