from app.extensions import db 
from datetime import datetime 

class Movimientos(db.Model): 

    __tablename__ = 'movimientos' 
    id = db.Column(db.Integer, primary_key=True, autoincrement = True) 
    id_cliente = db.Column(db.Integer, db.ForeignKey('clienteproveedor.id'), nullable=False) 
    id_insumo = db.Column(db.Integer, db.ForeignKey('insumos.id'), nullable=False) 
    precio = db.Column(db.Numeric(8,2), nullable=False, default=0) 
    cantidad = db.Column(db.Integer, nullable=False, default=0) 
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    observaciones = db.Column(db.String(150), nullable=True)
    fecha_vencimiento = db.Column(db.Date, nullable=True) 


    # relaciones
    cliente =db.relationship('ClienteProveedor')
    insumo = db.relationship('Insumo')


    
    def __repr__(self): #es para cuando se buscar y este esta filtrado por insumo.
        return f"<Insumo {self.id_insumo}>" 
    
    def __repr__(self): #es para cuando se buscar y este esta filtrado por cliente.
        return f"<Cliente {self.id_cliente}>" 


