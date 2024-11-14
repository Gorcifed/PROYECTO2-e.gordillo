from flask import jsonify, Blueprint, render_template
from Models.ingrediente import Ingrediente
from Models.producto import Producto
from Models.heladeria import Heladeria
#from app import app

heladeria_blueprint = Blueprint('heladeria_bp', __name__, url_prefix="/")

""" with app.app_context():
    ingredientes = Ingrediente.query.all()
    productos = Producto.query.All()

    for producto in productos:
        for ingrediente in ingredientes:
            if ingrediente.id == producto.id_ingrediente1:
                producto.ingredientes.append(ingrediente)
            elif ingrediente.id == producto.id_ingrediente2:
                producto.ingredientes.append(ingrediente)
            elif ingrediente.id == producto.id_ingrediente3:
                producto.ingredientes.append(ingrediente)

    heladeria = Heladeria('Disney', [], []) """

@heladeria_blueprint.route('/ingredientes')
def ingredientes():
    ingredientes = Ingrediente.query.all()
    return render_template("ingredientes.html", ingredientes = ingredientes)

@heladeria_blueprint.route('/productos')
def productos():
    productos = Producto.query.all()
    return render_template("productos.html", productos = productos)