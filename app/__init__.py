from flask import Flask
from  app.extensions import db,migrate

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app,db)
    
    from .insumos import insumos_bp
    app.register_blueprint(insumos_bp, url_prefix='/insumos')
    

    from .clienteproveedor import clienteproveedor_bp
    app.register_blueprint(clienteproveedor_bp, url_prefix = '/clienteproveedor')
    
    
    from .movimientos import movimientos_bp
    app.register_blueprint(movimientos_bp, url_prefix = '/movimientos')
    
    
    from .main import main_bp
    app.register_blueprint(main_bp)
    
    
   
    
    return app


    

