from flask_restx import Resource

class Push(Resource):
    def get(self):
        return {
            'message': 'Push',
            'funcionalidade': 'Enviar alterações para o repositório remoto',
            'opcoes': {
                '--force': 'git push origin <nome_branch>',
            }

        }, 200

class Pull(Resource):
    def get(self):
        return {
            'grupo': 'Grupo 2',
            'message': 'fiz a implementacao do pull'
            'funcionalidade': 'Baixar alterações do repositório remoto'
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