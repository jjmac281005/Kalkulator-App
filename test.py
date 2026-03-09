import unittest
from app import penjumlahan


class TestKalkulator(unittest.TestCase):

    def test_penjumlahan_positif(self):
        self.assertEqual(penjumlahan(5, 3), 8)

    def test_penjumlahan_negatif(self):
        self.assertEqual(penjumlahan(-5, -3), -8)

    def test_penjumlahan_campuran(self):
        self.assertEqual(penjumlahan(-5, 3), -2)

    def test_penjumlahan_nol(self):
        self.assertEqual(penjumlahan(0, 0), 0)

    def test_penjumlahan_desimal(self):
        self.assertEqual(penjumlahan(2.5, 3.5), 6.0)


if __name__ == "__main__":
    unittest.main()