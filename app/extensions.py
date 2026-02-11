from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#estos dos  estan importados en __init__.py
db = SQLAlchemy()
migrate = Migrate()