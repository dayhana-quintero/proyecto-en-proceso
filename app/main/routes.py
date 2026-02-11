from flask import render_template, request, redirect, url_for
from .import main_bp

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['email']
        password = request.form['password']
        
        if usuario == 'admin@gmail.com' and password =='1234':
            return redirect(url_for('main.dashboard'))
        else:
            return "usuario o contraseña incorrecta"
        
    return render_template('login.html')

@main_bp.route('/')
def home():
    return render_template('login.html')

@main_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')     

