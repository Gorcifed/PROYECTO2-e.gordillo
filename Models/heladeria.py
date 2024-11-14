from Models.ingrediente import Ingrediente
from Models.producto import Producto
from funciones import *

# Clase que representa la heladería
class Heladeria():
    # Método constructor
    def __init__(self, nombre: str, ingredientes: list, productos: list) -> None:
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.productos = productos

    # método que permite vender un producto
    # producto: producto a vender
    def vender_producto(self, producto: Producto) -> None:
        if not producto.calcular_ingredientes():
            return False

        self.descontar_inventario(producto)
        producto.ventas_dia = producto.ventas_dia + 1
        producto.precio_ventas_dia = producto.precio_ventas_dia + producto.precio_publico
        return True

    # método que descuenta del inventario el producto vendido
    # producto: producto a descontar inventario
    def descontar_inventario(self, producto):
        for ingrediente in producto.ingredientes:
            if ingrediente.tipo == 'Complemento':
                ingrediente.inventario = ingrediente.inventario - 1.0
            elif ingrediente.tipo == 'Base': # ingrediente base
                ingrediente.inventario = ingrediente.inventario - 0.2

    # Método que renueva el inventario de ingredientes a 0 (solo aplica para complementos)
    def renovar_inventario(self):
        for ingrediente in self.ingredientes:
            if ingrediente.tipo == 'Complemento':
                ingrediente.renovar_inventario()

    # Método que permite renovar el inventario de ingredientes
    def abastecer_inventario(self):
        for ingrediente in self.ingredientes:
            ingrediente.abastecer()

    # Método que calcula el producto más rentable
    def obtener_producto_mas_rentable(self):
        lista = []
        for producto in self._productos:
             lista.append({"nombre": producto.nombre, "rentabilidad": producto.calcular_rentabilidad()})
        return calcular_producto_mas_rentable(lista)

    # Método que permite agregar un ingrediente al sistema, validando que el tipo sea correcto
    def agregar_ingrediente(self, ingrediente: Ingrediente):
        if isinstance(ingrediente, Ingrediente):
            self._ingredientes.append(ingrediente)
        else:
            raise ValueError('Expected Ingrediente')

    # Método que permite agregar un producto al sistema,validando que el tipo sea correcto
    def agregar_producto(self, producto: Producto):
        if isinstance(producto, Producto):
            self._productos.append(producto)
            for ingrediente in producto.ingredientes:
                if not ingrediente in self._ingredientes:
                    self.ingredientes.append(ingrediente)
        else:
            raise ValueError('Expected Producto')

    @property
    def productos(self) -> list:
        """ Devuelve el valor del atributo privado '_productos' """
        return self._productos

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
            self.__ingredientes = value
        else:
            raise ValueError('Expected list')

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
