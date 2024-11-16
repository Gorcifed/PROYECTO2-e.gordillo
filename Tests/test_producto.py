import unittest
from Models.producto import Producto

# Clase de prueba de Ingrediente
class TestProducto(unittest.TestCase):
    # Método de setup de la prueba
    def setUp(self):
        self.setUpMyStuff()

    _productos = Producto("Disney")

    # Método de prueba de funcionalidad es sano
    def test_es_sano(self):
        self.assertEqual(self._ingrediente.es(), "¡Tsss!")

if __name__ == '__main__':
    unittest.main()