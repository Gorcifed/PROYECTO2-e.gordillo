import unittest
from Models.heladeria import Heladeria
from Tests.utilidad import *

# Clase de prueba de heladeria
class TestHeladeria(unittest.TestCase):
    ingredientes = []
    productos = []
    _heladeria = crear_heladeria()

    # Método que prueba la funcionalidad deabastecer inventario
    def test_abastecer_inventario(self):
        self.assertEqual(self._boa1.impuestos, 20.2)

    # Método que prueba la renovación de inventario
    def test_renovar_inventario(self):
        self.assertEqual(self._boa1.ratones_comidos, 1)

if __name__ == '__main__':
    unittest.main()