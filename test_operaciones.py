import unittest
from operaciones import sumar, restar, multiplicar, dividir

class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)  # 5 - 3 = 2
        self.assertEqual(restar(-1, 1), -2)  # -1 - 1 = -2
        self.assertEqual(restar(0, 0), 0)  # 0 - 0 = 0

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)  # 3 * 2 = 6
        self.assertEqual(multiplicar(-1, 1), -1)  # -1 * 1 = -1
        self.assertEqual(multiplicar(0, 5), 0)  # 0 * 5 = 0

    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)  # 6 / 3 = 2
        self.assertEqual(dividir(-4, 2), -2)  # -4 / 2 = -2
        self.assertEqual(dividir(0, 5), 0)  # 0 / 5 = 0

        with self.assertRaises(ValueError):
            dividir(5, 0)

if __name__ == '__main__':
    unittest.main()
