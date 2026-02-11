from app.extensions import db 
from datetime import datetime 

class ClienteProveedor(db.Model): 

    __tablename__ = 'clienteproveedor' 
    id = db.Column(db.Integer, primary_key=True, autoincrement = True) 
    nit = db.Column(db.String(15), unique=True, nullable=False) 
    nombre = db.Column(db.String(150), nullable=False) 
    direccion = db.Column(db.String(150), nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    tipo = db.Column(db.String(1), nullable=False)
    
    def __repr__(self): #es para cuando se buscar y este esta filtrado por codigo.
        return f"<ClienteProveedor {self.nombre}>" 
