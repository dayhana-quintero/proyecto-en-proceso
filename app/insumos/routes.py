from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    jsonify,
    request
)

from app.insumos.services import (
    
    crear_insumo,
    actualizar_insumo,
    eliminar_insumo,
    listar_insumos_activos,
    obtener_insumo,
    service_buscar_por_insumo  ##este es el que deben de hacer en services. 
)
        

from app.insumos import insumos_bp

@insumos_bp.route('/')
def index():
    insumos = listar_insumos_activos()
    return render_template('insumos/index.html', insumos=insumos)

@insumos_bp.route('/buscar_por_insumo/<referencia>')
def buscar_por_insumo(referencia):
    
    insumo = service_buscar_por_insumo(referencia)
    
    if not insumo:
        return jsonify({'error': 'Insumo no encontrado'})
        
    return jsonify({
      'id': insumo.id,
      'codigo': insumo.codigo,
      'descripcion': insumo.descripcion,
      'valor': str(insumo.valor),
      'fecha_vencimiento': insumo.fecha_vencimiento.isoformat() if insumo.fecha_vencimiento else None,
      'fecha_creacion': insumo.fecha_creacion.isoformat() if insumo.fecha_creacion else None
    })

