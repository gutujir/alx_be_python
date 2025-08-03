import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        cases = [
            (2, 3, 5),
            (-1, 1, 0),
            (0, 0, 0),
            (1.5, 2.5, 4.0),
            (-2, -3, -5),
            (1e9, 1e9, 2e9),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), expected)

    def test_subtraction(self):
        cases = [
            (5, 3, 2),
            (3, 5, -2),
            (0, 0, 0),
            (2.5, 1.0, 1.5),
            (-2, -3, 1),
            (1e9, 1e8, 9e8),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.subtract(a, b), expected)

    def test_multiplication(self):
        cases = [
            (2, 3, 6),
            (0, 100, 0),
            (-2, 3, -6),
            (1.5, 2, 3.0),
            (-1.5, -2, 3.0),
            (1e5, 1e5, 1e10),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.multiply(a, b), expected)

    def test_division(self):
        # normal division cases
        normal_cases = [
            (10, 2, 5.0),
            (3, 2, 1.5),
            (-6, 3, -2.0),
            (7.5, 2.5, 3.0),
            (0, 5, 0.0),
        ]
        for a, b, expected in normal_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.divide(a, b), expected)

        # division by zero cases
        zero_cases = [
            (10, 0),
            (0, 0),
            (-5, 0),
        ]
        for a, b in zero_cases:
            with self.subTest(a=a, b=b):
                self.assertIsNone(self.calc.divide(a, b))

    def test_idempotent_and_commutativity_where_applicable(self):
        # addition and multiplication are commutative
        self.assertEqual(self.calc.add(4, 5), self.calc.add(5, 4))
        self.assertEqual(self.calc.multiply(4, 5), self.calc.multiply(5, 4))
        # subtraction and division are not necessarily commutative
        self.assertNotEqual(self.calc.subtract(5, 4), self.calc.subtract(4, 5))
        if self.calc.divide(5, 4) is not None and self.calc.divide(4, 5) is not None:
            self.assertNotEqual(self.calc.divide(5, 4), self.calc.divide(4, 5))

    def test_non_numeric_input_raises_type_error_or_fails_gracefully(self):
        with self.assertRaises(TypeError):
            _ = self.calc.add("a", 1)
        with self.assertRaises(TypeError):
            _ = self.calc.subtract("a", "b")
        with self.assertRaises(TypeError):
            _ = self.calc.multiply("x", 3)
        with self.assertRaises(TypeError):
            _ = self.calc.divide("10", "2")

    def test_large_and_small_values(self):
        self.assertEqual(self.calc.add(1e308, 1e308),
                         float('inf'))  # overflow to inf
        self.assertEqual(self.calc.multiply(1e154, 1e154), float('inf'))
        self.assertAlmostEqual(self.calc.divide(1e-308, 1e308), 0.0)

    def test_identity_elements(self):
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.divide(5, 1), 5.0)


if __name__ == "__main__":
    unittest.main()
