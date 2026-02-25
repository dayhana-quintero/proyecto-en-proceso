from app.extensions import db #es donde esta el llamado a la base de datos 

from app.insumos.models import Insumo # llamar el modelo que voy a trabajar

from app.movimientos.models import Movimientos # llamar el modelo que voy a trabajar 
from app.clienteproveedor.models import ClienteProveedor # llamar el modelo que voy a trabajar

def listar_movimientos():
    return Movimientos.query.order_by(Movimientos.fecha.desc()).all()

def crear_movimiento(data):
    
    movimiento = Movimientos(
        id_cliente=data.get('id_cliente'),
        id_insumo=data.get('id_insumo'),
        precio=data.get('precio',0),
        cantidad=data.get('cantidad',0),
        fecha=data.get('fecha'),
        observaciones=data.get('observaciones'),
        fecha_vencimiento=data.get('fecha_vencimiento')
    )
    db.session.add(movimiento)
    db.session.commit()
    
    return movimiento

def service_buscar_por_cedula(cedula):
   cedula_limpia = str(cedula).strip()
   return ClienteProveedor.query.filter_by(nit=cedula_limpia).first()


def service_listar_insumos():
    return Insumo.query.all()