from database import db
from flask_login import UserMixin  # type: ignore #vai ajudar a gerenciar as sessões de login dos usuários, fornecendo métodos #1 e propriedades úteis para lidar com autenticação e autorização

class User(db.Model, UserMixin): # mapeamento da tabela User no banco de dados #herança multipla, UserMixin é necessário para o Flask-Login funcionar corretamente
    # id (int), username (text), password (text)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)