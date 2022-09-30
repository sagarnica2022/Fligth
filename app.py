from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/administrador')
def admin():
    return render_template('/admin/home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/vuelos')
def vuelos():
    return render_template('vuelos.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')
