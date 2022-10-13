from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key= True)
    nombres = db.Column(db.String(150))
    apellidos = db.Column(db.String(150))
    correo = db.Column(db.String(50))
    contraseña = db.Column(db.String(66))
    telefono = db.Column(db.Integer)
    documento = db.Column(db.Integer)
    nacimiento = db.Column(db.String(150))
    tipoUsuario = db.Column(db.String(150))