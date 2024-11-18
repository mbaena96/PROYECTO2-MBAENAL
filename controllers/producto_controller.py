from models.producto import Producto
from flask import Blueprint, render_template, flash, redirect, url_for
from db import db

producto_bp = Blueprint('producto_bp',__name__, url_prefix='/productos')

@producto_bp.route('/lista')
def listar_productos():
    productos = Producto.query.all()
    return render_template('consultar_productos.html', productos = productos)

@producto_bp.route('/detalle/<int:id>')
def detalle_producto(id):
    producto = Producto.query.get(id)
    calorias = producto.calcular_calorias()
    costo = producto.calcular_costo()
    rentabilidad = producto.calcular_rentabilidad()
    return render_template('detalle_producto.html', producto=producto, calorias=calorias, costo=costo, rentabilidad=rentabilidad)

@producto_bp.route('renovar_producto/<int:id>')
def renovar_producto(id):
    producto = Producto.query.get(id)
    for ingrediente in producto.ingredientes:
        ingrediente.renovar_inventario()

    db.session.commit()
    flash(f'Inventario de {producto.nombre} renovado')
    return redirect(url_for('producto_bp.listar_productos'))

@producto_bp.route('abastecer_producto/<int:id>')
def abastecer_producto(id):
    producto = Producto.query.get(id)
    for ingrediente in producto.ingredientes:
        ingrediente.abastecer()

    db.session.commit()
    flash(f'ingredientes de {producto.nombre} abastecidos')
    return redirect(url_for('producto_bp.listar_productos'))