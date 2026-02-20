from app.extensions import db
from app.clienteproveedor.models import ClienteProveedor 
from app.insumos.models import Insumo
from app.movimientos.models import Movimientos
from sqlalchemy import func

def obtener_metricas_dashboard():
    return{
        "clienteproveedor": ClienteProveedor.query.count(),
        "insumos": Insumo.query.count(),
        "movimientos": Movimientos.query.count()
    }