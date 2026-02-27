from flask import render_template, redirect, url_for, flash, session
from app.auth import auth_bp
from app.auth.forms import LoginForm, RegisterForm
from app.auth.services import autenticar_usuario
from werkzeug.security import generate_password_hash

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    print("Formulario recibido:", form.data)  # Depuración: muestra los datos del formulario
    
    if form.validate_on_submit():
        usuario = autenticar_usuario(form.username.data, form.password.data)
        
        if usuario:
            session["user_id"] = usuario.id
            session["username"] = usuario.username
            session["rol"] = usuario.rol
            
            
            flash("Bienvenido al sistema", "success")
            return redirect(url_for("main.dashboard"))
        
        
        flash("Credenciales incorrectas", "danger")
        
    return render_template("auth/login.html", form=form)


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("sesion finalizada", "info")
    return redirect(url_for("auth.login"))

@auth_bp.route("/guardar", methods=["GET", "POST"])
def guardar():
    form = RegisterForm()
    if form.validate_on_submit():
        # Verificar si el username ya existe
        existing_user = Usuario.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash("El nombre de usuario ya existe", "danger")
            return redirect(url_for("create_usuario"))

        # Crear nuevo usuario
        nuevo_usuario = Usuario(
            username=form.username.data,
            password_hash=generate_password_hash(form.password.data),
            nombre=form.nombre.data,
            rol=form.rol.data,
            activo=form.activo.data
        )

        db.session.add(nuevo_usuario)
        db.session.commit()

        flash("Usuario creado exitosamente", "success")
        return redirect(url_for("lista_usuarios"))  # Ajusta a tu vista de listado

    return render_template("form.html")


@auth_bp.route("/create")
def create():
    form = RegisterForm()
    return render_template('form.html', form=form)

    