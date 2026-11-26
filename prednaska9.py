import unittest


def scitej(a, b):
    a = int(a)
    b = int(b)
    return a + b


def odecitej(a, b):
    return a - b

class TestMatematika(unittest.TestCase):
    def test_scitej(self):
        self.assertEqual(scitej(2, 3), 5)
        self.assertEqual(scitej(1, 1), 2)
        self.assertEqual(scitej("1", "10"), 11)
    def test_scitej_vyjimka(self):
        with self.assertRaises(ValueError):
            scitej("ahoj", "cau")
    def test_odecitej(self):
        self.assertEqual(odecitej(3, 2), 1)


if __name__ == "__main__":
    unittest.main()
