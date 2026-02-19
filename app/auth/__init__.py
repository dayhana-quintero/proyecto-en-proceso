from flask import Blueprint

##declaramos blueprint

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
    template_folder = "../templates/auth"
   
)

from app.auth import routes 