from db import db
from sqlalchemy import text, ForeignKey
from funciones import *

# Clase que representa el producto
class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(45), nullable = False)
    precio = db.Column(db.Integer, nullable = False)
    calorias = db.Column(db.NUMERIC(4,2), nullable = False)
    inventario = db.Column(db.NUMERIC(4,2), nullable = False)
    id_ingrediente1 = db.Column(db.Integer, ForeignKey("ingredientes.id"), nullable=False)
    id_ingrediente2 = db.Column(db.Integer, ForeignKey("ingredientes.id"), nullable=False)
    id_ingrediente3 = db.Column(db.Integer, ForeignKey("ingredientes.id"), nullable=False)
    tipo = db.Column(db.String(15), nullable = False)
    
    # Método constructor de la clase
    def __init__(self):
        self.ingredientes = []
        self.ventas_dia = 0
        self.precio_ventas_dia = 0

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

    @property
    def nombre(self) -> str:
        """ Devuelve el valor del atributo privado 'nombre' """
        return self.__nombre

    @nombre.setter
    def nombre(self, value:str) -> None:
        """
        Establece un nuevo valor para el atributo privado 'nombre'

        Valida que el valor enviado corresponda al tipo de dato del atributo
        """
        if isinstance(value, str):
            self.__nombre = value
        else:
            raise ValueError('Expected str')

    @property
    def precio(self) -> int:
        """ Devuelve el valor del atributo privado 'precio' """
        return self.__precio

    @precio.setter
    def precio(self, value:int) -> None:
        """
        Establece un nuevo valor para el atributo privado 'precio'

        Valida que el valor enviado corresponda al tipo de dato del atributo
        """
        if isinstance(value, int):
            self.__precio = value
        else:
            raise ValueError('Expected int')

    @property
    def ingredientes(self) -> list:
        """ Devuelve el valor del atributo privado 'ingredientes' """
        return self.__ingredientes

    @ingredientes.setter
    def ingredientes(self, value:list) -> None:
        """
        Establece un nuevo valor para el atributo privado 'ingredientes'

        Valida que el valor enviado corresponda al tipo de dato del atributo
        """
        if isinstance(value, list):
            if len(value) > 3:
                raise ValueError('Límite de ingredientes superado')
            self.__ingredientes = value
        else:
            raise ValueError('Expected list')
    
    @property
    def ventas_dia(self) -> int:
        """ Devuelve el valor del atributo privado 'ventas_dia' """
        return self.__ventas_dia
    
    @ventas_dia.setter
    def ventas_dia(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'ventas_dia'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self.__ventas_dia = value
        else:
            raise ValueError('Expected int')
        
    @property
    def precio_ventas_dia(self) -> int:
        """ Devuelve el valor del atributo privado 'precio_ventas_dia' """
        return self.__precio_ventas_dia
    
    @precio_ventas_dia.setter
    def precio_ventas_dia(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'precio_ventas_dia'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self.__precio_ventas_dia = value
        else:
            raise ValueError('Expected int')
