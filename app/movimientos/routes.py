from flask import (
    flash,
    url_for,
    redirect,
    render_template,
    request,
    Blueprint,
    Flask,
    jsonify
    
)


from app.movimientos import movimientos_bp 

# asi se llama el metodo de services.py
from app.movimientos.services import (
    
    listar_movimientos,
    crear_movimiento,
    service_buscar_por_cedula,
    service_listar_insumos
    
)

from  app.utils.security import login_required

@movimientos_bp.route('/')
@login_required
def index():
    movimiento = listar_movimientos()
    return render_template('movimientos/index.html',movimiento = movimiento)


@movimientos_bp.route('/create')
@login_required
def create():
    listar_insumos = service_listar_insumos()

    return render_template('movimientos/create.html', listar_insumos=listar_insumos)


@movimientos_bp.route('/movimientos/guardar', methods=['GET', 'POST'])
@login_required
def guardar():
    if request.method == 'POST':
        data = {
            'id_cliente': request.form.get('id_cliente', type=int),
            'id_insumo': request.form.get('txtid_producto', type=int),
            'precio': request.form.get('txtprecio', type=float),
            'cantidad': request.form.get('txtcantidad', type=int),
            'fecha_creacion': request.form.get('txtfecha_creacion'),
            'observaciones': request.form.get('txtobservaciones'),
            'fecha_vencimiento': request.form.get('txtfecha_vencimiento')
        }
        
        crear_movimiento(data)
        
        return redirect(url_for('main.dashboard'))
    return render_template('movimientos/create.html')


@movimientos_bp.route('movimientos/buscar_por_cedula/<cedula>')
@login_required
def buscar_por_cedula(cedula):
    
    cliente = service_buscar_por_cedula(cedula)
    
    if not cliente: 
       return jsonify({"error": "Cliente no encontrado"}) 
 
    return jsonify({ 
        "id": cliente.id, 
        "nombre": cliente.nombre,
        "direccion": cliente.direccion,
        "celular": cliente.celular
    })

@movimientos_bp.route('/edit')
@login_required
def edit():
    return render_template('movimientos/edit.html')

@movimientos_bp.route('/delete')
@login_required
def delete():
    return render_template('movimientos/delete.html')










