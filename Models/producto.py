from db import db
from sqlalchemy import text, ForeignKey
from funciones import *
from Models.ingrediente import Ingrediente

# Clase que representa el producto
class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(45), nullable = False)
    precio = db.Column(db.Integer, nullable = False)
    id_ingrediente1 = db.Column(db.Integer, nullable=False)
    id_ingrediente2 = db.Column(db.Integer, nullable=False)
    id_ingrediente3 = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(15), nullable = False)
    _ingredientes = None
    _ventas_dia = 0
    _precio_ventas_dia = 0

    # Método que permite calcular el costo del producto
    def calcular_costo(self) -> int:
        lista = []
        if(self.tipo == 'Copa'):
            for ingrediente in self.ingredientes:
                lista.append({"nombre": ingrediente.nombre, "precio": ingrediente.precio})
            costo = calcular_costo_produccion_producto(lista)
            return costo
        # Es malteada
        for ingrediente in self.ingredientes:
            lista.append({"nombre": ingrediente.nombre, "precio": ingrediente.precio})

        costo = calcular_costo_produccion_producto(lista) + 500
        return costo

    # Método que permite calcular las calorías
    def calcular_calorias(self) -> float:
        lista = [x.calorias for x in self.ingredientes]
        calorias = calcular_calorias_producto(lista, True)
        if self.tipo == 'Copa':
            return round(calorias, 2)
        # Es malteada
        return round(calorias, 2) + 200.0

    # Método que permite calcular la rentabilidad del producto
    def calcular_rentabilidad(self) -> int:
        return self.precio - self.calcular_costo()

    # Método que determina si hay suficientes ingredientes para hacer el producto
    def calcular_ingredientes(self) -> bool:
        for ingrediente in self.ingredientes:
            if ingrediente.tipo == 'Complemento':
                if ingrediente.inventario < 1:
                    return False
            else: # Es Base
                if ingrediente.inventario < .2:
                    return False
        return True
    
     # Método que returna el ingrediente faltante de un producto, None si hay suficiente
    def obtener_ingrediente_faltante(self) -> Ingrediente:
        for ingrediente in self.ingredientes:
            if ingrediente.tipo == 'Complemento':
                if ingrediente.inventario < 1:
                     return ingrediente
            else: # Es Base
                if ingrediente.inventario < .2:
                    return ingrediente
        return None

    @property
    def ingredientes(self) -> list:
        """ Devuelve el valor del atributo privado 'ingredientes' """
        return self._ingredientes

    @ingredientes.setter
    def ingredientes(self, value:list) -> None:
        """
        Establece un nuevo valor para el atributo privado 'ingredientes'

        Valida que el valor enviado corresponda al tipo de dato del atributo
        """
        if isinstance(value, list):
            self._ingredientes = value
        else:
            raise ValueError('Expected list')
    
    @property
    def ventas_dia(self) -> int:
        """ Devuelve el valor del atributo privado 'ventas_dia' """
        return self._ventas_dia
    
    @ventas_dia.setter
    def ventas_dia(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'ventas_dia'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self._ventas_dia = value
        else:
            raise ValueError('Expected int')
        
    @property
    def precio_ventas_dia(self) -> int:
        """ Devuelve el valor del atributo privado 'precio_ventas_dia' """
        return self._precio_ventas_dia
    
    @precio_ventas_dia.setter
    def precio_ventas_dia(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'precio_ventas_dia'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self._precio_ventas_dia = value
        else:
            raise ValueError('Expected int')
