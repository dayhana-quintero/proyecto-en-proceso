from app.extensions import db 
from datetime import datetime 

class Insumo(db.Model): 

    __tablename__ = 'insumos' 
    id = db.Column(db.Integer, primary_key=True, autoincrement = True) 
    codigo = db.Column(db.String(15), unique=True, nullable=False) 
    descripcion = db.Column(db.String(150), nullable=False) 
    lote = db.Column(db.String(12), nullable=False) 
    invima = db.Column(db.String(15), nullable=True) 
    valor = db.Column(db.Numeric(8, 2), nullable=False, default=0) 
    iva = db.Column(db.Numeric(2,2), default=0) 
    fecha_vencimiento = db.Column(db.Date, nullable=True) 
    activo = db.Column(db.Boolean, default=True) 
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow) 

    def __repr__(self): #es para cuando se buscar y este esta filtrado por codigo.
        return f"<Insumo {self.codigo}>" 

    def __repr__(self): #es para cuando se buscar y este esta filtrado por cliente.
        return f"<Cliente {self.id_cliente}>" 