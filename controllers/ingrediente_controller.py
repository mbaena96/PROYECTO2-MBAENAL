from models.ingrediente import Ingrediente
from flask import Blueprint, render_template, flash, redirect, url_for
from db import db

ingrediente_bp = Blueprint('ingrediente_bp', __name__, url_prefix='/ingrediente')

@ingrediente_bp.route('/<int:id>')
def mostrar_ingredientes(id):
    ingrediente = Ingrediente.query.get(id)
    es_sano = ingrediente.es_sano()
    return render_template('ingrediente.html', ingrediente=ingrediente, es_sano=es_sano)

@ingrediente_bp.route('renovar_ingrediente/<int:id>')
def renovar_ingrediente(id):
    ingrediente = Ingrediente.query.get(id)
    ingrediente.renovar_inventario()
    db.session.commit()
    flash(f'Inventario de {ingrediente.nombre} renovado')
    return redirect(url_for('ingrediente_bp.mostrar_ingredientes', id=ingrediente.id))

@ingrediente_bp.route('abastecer_ingrediente/<int:id>')
def abastecer_ingrediente(id):
    ingrediente = Ingrediente.query.get(id)
    ingrediente.abastecer()
    db.session.commit()
    flash(f'{ingrediente.nombre} abastecido')
    return redirect(url_for('ingrediente_bp.mostrar_ingredientes', id=ingrediente.id))

    