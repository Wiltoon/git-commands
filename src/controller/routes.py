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
            'message': 'Add',
            'description': 'O comando "git add [nome-de-arquivo]" cria um pacote com os arquivos modificados selecionados (no comando) para a branch que você vai commitar (geralmente a main). Caso utilize "git add .", ele vai criar um pacote com todos os aruivos modificados.'
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
            'message': 'Status'
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