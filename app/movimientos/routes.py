from flask import (
    flash,
    url_for,
    redirect,
    render_template,
    request,
    Blueprint,
    Flask
)

from app.movimientos.services import (
    listar_movimientos, # asi se llama el metodo de services.py
    crear_movimiento
)

from app.movimientos import movimientos_bp 

@movimientos_bp.route('/')
def index():
    movimiento = listar_movimientos()
    return render_template('movimientos/index.html',movimiento = movimiento)


@movimientos_bp.route('/create')
def create():
    return render_template('movimientos/create.html')


@movimientos_bp.route('movomientos /guardar', methods=['GET', 'POST'])
def guardar():
    if request.method == 'POST':
        data = {
            'id_cliente': request.form.get('txtcliente', type=int),
            'id_insumos': request.form.get('txtinsumo', type=int),
            'precio': request.form.get('txtprecio', type=float),
            'cantidad': request.form.get('txtcantidad', type=int),
            'fecha': request.form.get('txtfecha'),
            'observaciones': request.form.get('txtobservaciones'),
            'fecha_vencimiento': request.form.get('txtfechavencimiento')
        }
        
        crear_movimiento(data)
        
        return redirect(url_for('main.dashboard'))
    return render_template('movimientos/create.html')

@movimientos_bp.route('/edit')
def edit():
    return render_template('movimientos/edit.html')

@movimientos_bp.route('/delete')
def delete():
    return render_template('movimientos/delete.html')



