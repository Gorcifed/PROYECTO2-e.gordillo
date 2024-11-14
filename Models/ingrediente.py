from db import db
from sqlalchemy import text
from funciones import *

class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(45), nullable = False)
    precio = db.Column(db.Integer, nullable = False)
    calorias = db.Column(db.NUMERIC(4,2), nullable = False)
    vegetariano = db.Column(db.BOOLEAN, nullable = False)
    inventario = db.Column(db.NUMERIC(4,2), nullable = False)
    tipo = db.Column(db.String(15), nullable = False)
    sabor = db.Column(db.String(45), nullable = False)

    #Método que determina si un ingrediente es sano
    def es_sano(self) -> bool:
        return es_sano_ingrediente(self.calorias, self.vegetariano)

    # Método que permite abastecer un ingrediente
    def abastecer(self) -> None:
        if self.tipo == 'Ingrediente':
             self.inventario = self.inventario + 10.0
             return
        # Es base
        self.inventario = self.inventario + 5.0

    # Método que permite renovar el inventario
    def renovar_inventario(self):
        self.inventario = 0.0

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
    def calorias(self) -> float:
        """ Devuelve el valor del atributo privado 'calorias' """
        return self.__calorias

    @calorias.setter
    def calorias(self, value:float) -> None:
        """
        Establece un nuevo valor para el atributo privado 'calorias'

        Valida que el valor enviado corresponda al tipo de dato del atributo
        """
        if isinstance(value, float):
            self.__calorias = value
        else:
            raise ValueError('Expected float')

    @property
    def vegetariano(self) -> bool:
        """ Devuelve el valor del atributo privado 'vegetariano' """
        return self.__vegetariano

    @vegetariano.setter
    def vegetariano(self, value:bool) -> None:
        """
        Establece un nuevo valor para el atributo privado 'vegetariano'

        Valida que el valor enviado corresponda al tipo de dato del atributo
        """
        if isinstance(value, bool):
            self.__vegetariano = value
        else:
            raise ValueError('Expected bool')

    @property
    def inventario(self) -> float:
        """ Devuelve el valor del atributo privado 'inventario' """
        return self.__inventario

    @inventario.setter
    def inventario(self, value:float) -> None:
        """
        Establece un nuevo valor para el atributo privado 'inventario'

        Valida que el valor enviado corresponda al tipo de dato del atributo
        """
        if isinstance(value, float):
            self.__inventario = value
        else:
            raise ValueError('Expected float')

    @property
    def sabor(self) -> str:
        """ Devuelve el valor del atributo privado 'sabor' """
        return self.__sabor

    @sabor.setter
    def sabor(self, value:str) -> None:
        """
        Establece un nuevo valor para el atributo privado 'sabor'

        Valida que el valor enviado corresponda al tipo de dato del atributo
        """
        if isinstance(value, str):
            self.__sabor = value
        else:
            raise ValueError('Expected str')
