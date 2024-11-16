from Models.heladeria import Heladeria
from Models.producto import Producto
from Models.ingrediente import Ingrediente

def crear_heladeria():
    ingredientes = []
    productos = []
    heladeria = Heladeria("Disney", ingredientes, productos)
    return heladeria