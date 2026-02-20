from flask import render_template, redirect,url_for, session
from app.main import main_bp
from app. main.services import obtener_metricas_dashboard
from app.utils.security import login_required


@main_bp.route("/")
def index():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    
    return redirect(url_for("main.dashboard"))


@main_bp.route("/dashboard")
@login_required
def dashboard():
    metricas = obtener_metricas_dashboard()
    return render_template("main/dashboard.html",metricas=metricas)

