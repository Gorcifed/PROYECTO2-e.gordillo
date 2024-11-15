from flask import Flask,  render_template
from dotenv import load_dotenv
from db import db, init_db
from Controllers.controller_heladeria import heladeria_blueprint
from Models.ingrediente import Ingrediente
from Models.producto import Producto
from Models.heladeria import Heladeria
import os
import traceback 

load_dotenv(override=True)

app = Flask(__name__, template_folder = "Views")
DB_STRING_CONNECTION = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config["SQLALCHEMY_DATABASE_URI"] = DB_STRING_CONNECTION
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    ingredientes = Ingrediente.query.all()
    productos = Producto.query.all()

    for producto in productos:
        producto.ingredientes = []
        for ingrediente in ingredientes:
            if ingrediente.id == producto.id_ingrediente1:
                producto.ingredientes.append(ingrediente)   
            elif ingrediente.id == producto.id_ingrediente2:
                producto.ingredientes.append(ingrediente)
            elif ingrediente.id == producto.id_ingrediente3:
                producto.ingredientes.append(ingrediente)

    heladeria = Heladeria('Disney', ingredientes, productos)

@app.template_filter()
def currencyFormat(value):
    value = float(value)
    return "${:,.0f}".format(value)

@app.route('/ingredientes')
def ingredientes():
    return render_template("ingredientes.html", ingredientes = heladeria.ingredientes)

@app.route('/productos')
def productos():
    return render_template("productos.html", productos = heladeria.productos)

@app.route('/abastecer')
def abastecer():
     try:
         heladeria.abastecer_inventario()
         return render_template('Success.html', mensaje = f"Se abasteció el inventario 📦")
     except Exception as e:
        return render_template('Error.html', mensaje = f"Error {str(e)}")

@app.route('/renovarInventario')
def renovarInventario():
     try:
         heladeria.renovar_inventario()
         return render_template('Success.html', mensaje = f"Se renovó el inventario de complementos 🫗")
     except Exception as e:
        return render_template('Error.html', mensaje = f"Error {str(e)}")

@app.route('/vender')
def venderLista():
    return render_template("productosVenta.html", productos = heladeria.productos)

@app.route('/productoMasRentable')
def productoMasRentable():
     try:
         producto_mas_rentable = heladeria.obtener_producto_mas_rentable().get("nombre", "")
         rentabilidad = heladeria.obtener_producto_mas_rentable().get("rentabilidad", "")
         return render_template('Success.html', mensaje = f"El producto más rentable es {producto_mas_rentable}, rentabilidad: {currencyFormat(rentabilidad)} ")
     except Exception as e:
        return render_template('Error.html', mensaje = f"Error {str(e)}")

@app.route('/vender/<idProducto>')
def vender(idProducto):
    try:
        for producto in heladeria.productos:
            if producto.id == int(idProducto):
                ingrediente_faltante = producto.obtener_ingrediente_faltante()
                if ingrediente_faltante != None:
                    return render_template('Warning.html', mensaje = f"“¡Oh no! Nos hemos quedado sin {ingrediente_faltante.nombre} 😥 para hacer {producto.nombre}")
                vendido = heladeria.vender_producto(producto)
                if vendido:
                    return render_template('Success.html', mensaje = f"¡Vendido el producto {producto.nombre}!")
                else:
                    return render_template('Warning.html', mensaje = f"No se pudo vender el producto {producto.nombre}")
        return render_template('Warning.html', mensaje = f"No se encontró el producto {idProducto}")
    except Exception as e:
        return render_template('Error.html', mensaje = f"Error {str(e)}")

@app.route('/')
def index():
    return render_template('Index.html')

#app.register_blueprint(heladeria_blueprint)

if __name__ == '__main__':
    app.run(debug=True)