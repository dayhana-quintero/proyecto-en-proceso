from flask import Blueprint, render_template, jsonify
from app.insumos.services import listar_insumos_activos, service_buscar_por_insumo
from app.insumos import insumos_bp
from app.utils.security import login_required

# Ruta principal de insumos
@insumos_bp.route('/')
@login_required  # O login_required() si tu decorador lo requiere
def index():
    insumos = listar_insumos_activos()
    return render_template('insumos/index.html', insumos=insumos)

# Ruta para buscar un insumo por referencia
@insumos_bp.route('/buscar_por_insumo/<referencia>')
@login_required
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