from flask import Blueprint

##declaramos blueprint

movimientos_bp = Blueprint(
    'movimientos',
    __name__,
    template_folder = 'templates',
    static_folder= 'static'
)

from .import routes, models

