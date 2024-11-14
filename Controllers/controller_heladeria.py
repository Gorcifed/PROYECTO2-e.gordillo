from flask import jsonify, Blueprint, render_template, current_app
from Models.ingrediente import Ingrediente
from Models.producto import Producto
from Models.heladeria import Heladeria
#from app import app

heladeria_blueprint = Blueprint('heladeria_bp', __name__, url_prefix="/")

@heladeria_blueprint.route('/ingredientes')
def ingredientes():
    ingredientes = Ingrediente.query.all()
    return render_template("ingredientes.html", ingredientes = ingredientes)

@heladeria_blueprint.route('/productos')
def productos():
    productos = Producto.query.all()
    return render_template("productos.html", productos = productos)