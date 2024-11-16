import unittest
from Models.ingrediente import Ingrediente
from Tests.utilidad import *

# Clase de prueba de Ingrediente
class TestIngrediente(unittest.TestCase):
    _heladeria = crear_heladeria()

    # Método de prueba de funcionalidad es sano
    def test_es_sano(self):
        self.assertEqual(self._heladeria.ingredientes[0].es_sano(), False)
        self.assertEqual(self._heladeria.ingredientes[2].es_sano(), True)

if __name__ == '__main__':
    unittest.main()