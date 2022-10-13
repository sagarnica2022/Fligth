from crypt import methods
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash

from models import User, db
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/administrador')
def admin():
    return render_template('admin/dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        user = User.query.filter_by(correo = request.form['correo']).first()
        if user and check_password_hash(request.form['password'], user.contraseña):
            return "esta adentro "
        return "los datos no coinciden"
        
    return render_template('login.html')

@app.route('/vuelos')
def vuelos():
    return render_template('vuelos.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/usuarios')
def listUsers():
    users = User.query.all()
    return render_template('admin/users.html', users = users)

@app.route('/createUser', methods=['POST'])
def addUser():
    hashed_pw = generate_password_hash(request.form['contraseña'], method='sha256')
    user = User(
        nombres = request.form['nombres'], 
        apellidos = request.form['apellidos'],
        contraseña = hashed_pw,
        correo = request.form['correo'],
        telefono = request.form['telefono'],
        documento = request.form['documento'],
        nacimiento = request.form['nacimiento'])
    
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('login'))

@app.route('/delete/<id>')
def delete(id):
    User.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('usuarios'))


db.init_app(app)
with app.app_context():
    db.create_all()
