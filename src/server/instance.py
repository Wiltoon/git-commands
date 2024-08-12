from src.controller.routes import Push,Pull,Add,Commit,Init,Clone,Checkout,Status,Log,Branch,Merge,Rebase
from flask import Flask
from flask_restx import Api, fields

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(
            self.app, 
            version='1.0', 
            title='GIT COMMANDS', 
            description='Descrevendo os comandos do git para aprendizagem de GIT', 
            doc='/doc'
        )
        self.api.add_resource(Push, '/push')
        self.api.add_resource(Pull, '/pull')
        self.api.add_resource(Add, '/add')
        self.api.add_resource(Commit, '/commit')
        self.api.add_resource(Init, '/init')
        self.api.add_resource(Clone, '/clone')
        self.api.add_resource(Checkout, '/checkout')
        self.api.add_resource(Status, '/status')
        self.api.add_resource(Log, '/log')
        self.api.add_resource(Branch, '/branch')
        self.api.add_resource(Merge, '/merge')
        self.api.add_resource(Rebase, '/rebase')


    def run(self):
        self.app.run(
            debug=True,
            port=5000
        )