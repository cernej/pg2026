import unittest


def deleni(a, b):
    if b == 0:
        raise ZeroDivisionError("Nelze dělit nulou.")
    return a / b


class TestDeleni(unittest.TestCase):
    def test_deleni_nulou(self):
        with self.assertRaises(ZeroDivisionError):
            deleni(10, 0)


if __name__ == "__main__":
    unittest.main()
