from models.heladeria import Heladeria
from models.producto import Producto
from flask import Blueprint, render_template, request, flash, redirect, url_for
from db import db

heladeria_bp = Blueprint('heladeria_bp',__name__, url_prefix='/vender')

@heladeria_bp.route('/', methods=["GET", "POST"])
def vender():
    if request.method == 'GET':
        productos = Producto.query.all()
        return render_template('venta.html', productos = productos)
    else:
        response = request.form['producto']
        # producto_vender = Producto.query.filter_by(nombre=response).first()
        heladeria = Heladeria.query.filter_by(id=1).first()

        try:
            if heladeria.vender(response):
                db.session.commit()
                flash(f'{response} vendido con éxito')
        except ValueError as error:
            flash(str(error))
            # print (error)
        
        return redirect(url_for('heladeria_bp.vender'))
    
@heladeria_bp.route('/rentable')
def producto_rentable():
    heladeria = Heladeria.query.get(1)
    producto_rentable = heladeria.producto_mas_rentable()
    return render_template('producto_rentable.html', producto_rentable=producto_rentable)
    