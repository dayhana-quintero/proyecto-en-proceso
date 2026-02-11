import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Configuración base (común a todos los entornos)"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'lUIS159753CsiLosMatoEstudian+tes@')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Configuración general de sesión
    SESSION_PERMANENT = False


class DevelopmentConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://@localhost\\SQLEXPRESS/proyectosis"
        "?driver=ODBC+Driver+17+for+SQL+Server"
        "&Trusted_Connection=yes"
    )

class ProductionConfig(Config):
    """Configuración para producción"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "mssql+pyodbc://@localhost/DatosFarmacia"
        "?driver=ODBC+Driver+17+for+SQL+Server"
        "&Trusted_Connection=yes"
    )