from db import db
from sqlalchemy import text
from funciones import *
import decimal

class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(45), nullable = False)
    precio = db.Column(db.Integer, nullable = False)
    calorias = db.Column(db.NUMERIC(5,2), nullable = False)
    vegetariano = db.Column(db.BOOLEAN, nullable = False)
    inventario = db.Column(db.NUMERIC(5,2), nullable = False)
    tipo = db.Column(db.String(15), nullable = False)
    sabor = db.Column(db.String(45), nullable = False)

    #Método que determina si un ingrediente es sano
    def es_sano(self) -> bool:
        return es_sano_ingrediente(self.calorias, self.vegetariano)

    # Método que permite abastecer un ingrediente
    def abastecer(self) -> None:
        if self.tipo == 'Ingrediente':
             self.inventario = self.inventario + decimal.Decimal(10.0)
             return
        # Es base
        self.inventario = self.inventario + decimal.Decimal(5.0)

    # Método que permite renovar el inventario
    def renovar_inventario(self):
        self.inventario = 0.0