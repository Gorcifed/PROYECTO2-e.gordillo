from flask import Flask,  render_template
from dotenv import load_dotenv
from db import db
from Controllers.controller_heladeria import *
from Models.ingrediente import Ingrediente
from Models.producto import Producto
from Models.heladeria import Heladeria
import os

load_dotenv(override=True)

def create_app():
    app = Flask(__name__, template_folder = "Views")
    DB_STRING_CONNECTION = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_STRING_CONNECTION
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    return app

app = create_app()

@app.template_filter()
def currencyFormat(value):
    value = float(value)
    return "${:,.0f}".format(value)

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
    print("pre-establecer_objetos")
    app.config['Heladeria'] = heladeria


@app.route('/')
def index():
    return render_template('Index.html')

app.register_blueprint(heladeria_blueprint)

if __name__ == '__main__':
    app.run(debug=True)