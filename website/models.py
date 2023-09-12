from . import db
from flask_login import UserMixin

class Carrinho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_item = db.Column(db.String(100), db.ForeignKey('item.id'))

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    senha = db.Column(db.String(50))
    itens_carrinho = db.relationship('Carrinho')