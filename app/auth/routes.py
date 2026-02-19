from flask import render_template, redirect, url_for, flash, session
from app.auth import auth_bp
from app.auth.forms import LoginForm
from app.auth.services import autenticar_usuario

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    
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