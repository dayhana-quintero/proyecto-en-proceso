from app.extensions import db
from app.insumos.models import Insumo



def service_buscar_por_insumo(referencia):
    return Insumo.query.filter_by(codigo=referencia).first()
    
    
def listar_insumos_activos(): 
    return Insumo.query.filter_by(activo=True).all() 



def crear_insumo(form): 
    """ 
    Crea un nuevo insumo validando reglas de negocio 
    """ 
    # Validar código único 

    existe = Insumo.query.filter_by(codigo=form.codigo.data).first() 
    if existe: 
        raise ValueError("Ya existe un insumo con ese código") 

    insumo = Insumo( 
        codigo=form.codigo.data, 
        descripcion=form.descripcion.data, 
        lote=form.lote.data, 
        invima=form.invima.data, 
        valor=form.valor.data, 
        iva=form.iva.data, 
        fecha_vencimiento=form.fecha_vencimiento.data 
    ) 

    db.session.add(insumo) 
    db.session.commit() 

    return insumo 

def actualizar_insumo(insumo_id, form): 
    insumo = Insumo.query.get_or_404(insumo_id) 
    insumo.codigo = form.codigo.data 
    insumo.descripcion = form.descripcion.data 
    insumo.lote = form.lote.data 
    insumo.invima = form.invima.data 
    insumo.valor = form.valor.data 
    insumo.iva = form.iva.data 
    insumo.fecha_vencimiento = form.fecha_vencimiento.data 
    db.session.commit() 

    return insumo 

def eliminar_insumo(insumo_id): 
    insumo = Insumo.query.get_or_404(insumo_id) 
    insumo.activo = False 
    db.session.commit() 




def obtener_insumo(insumo_id): 
    return Insumo.query.get_or_404(insumo_id) 


