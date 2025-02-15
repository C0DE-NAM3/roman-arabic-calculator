import unittest
from calculator import RomanCalculator

class TestRomanCalculator(unittest.TestCase):
    def test_add_arabic_numbers(self):
        """Test addition with Arabic numbers."""
        test_cases = [
            ((1, 2), (3, 'III')),
            ((4, 5), (9, 'IX')),
            ((10, 40), (50, 'L')),
            ((90, 10), (100, 'C')),
            ((2000, 23), (2023, 'MMXXIII')),
        ]
        for (a, b), expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(RomanCalculator.add(a, b), expected)

    def test_add_roman_numbers(self):
        """Test addition with Roman numerals."""
        test_cases = [
            (('I', 'II'), (3, 'III')),
            (('IV', 'V'), (9, 'IX')),
            (('X', 'XL'), (50, 'L')),
            (('XC', 'X'), (100, 'C')),
            (('MM', 'XXIII'), (2023, 'MMXXIII')),
        ]
        for (a, b), expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(RomanCalculator.add(a, b), expected)

    def test_subtract_arabic_numbers(self):
        """Test subtraction with Arabic numbers."""
        test_cases = [
            ((5, 3), (2, 'II')),
            ((10, 4), (6, 'VI')),
            ((100, 1), (99, 'XCIX')),
            ((2023, 23), (2000, 'MM')),
        ]
        for (a, b), expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(RomanCalculator.subtract(a, b), expected)

    def test_subtract_roman_numbers(self):
        """Test subtraction with Roman numerals."""
        test_cases = [
            (('V', 'III'), (2, 'II')),
            (('X', 'IV'), (6, 'VI')),
            (('C', 'I'), (99, 'XCIX')),
            (('MMXXIII', 'XXIII'), (2000, 'MM')),
        ]
        for (a, b), expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(RomanCalculator.subtract(a, b), expected)

    def test_multiply_arabic_numbers(self):
        """Test multiplication with Arabic numbers."""
        test_cases = [
            ((2, 3), (6, 'VI')),
            ((5, 5), (25, 'XXV')),
            ((10, 10), (100, 'C')),
            ((50, 20), (1000, 'M')),
        ]
        for (a, b), expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(RomanCalculator.multiply(a, b), expected)

    def test_multiply_roman_numbers(self):
        """Test multiplication with Roman numerals."""
        test_cases = [
            (('II', 'III'), (6, 'VI')),
            (('V', 'V'), (25, 'XXV')),
            (('X', 'X'), (100, 'C')),
            (('L', 'XX'), (1000, 'M')),
        ]
        for (a, b), expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(RomanCalculator.multiply(a, b), expected)

    def test_divide_arabic_numbers(self):
        """Test division with Arabic numbers."""
        test_cases = [
            ((6, 2), (3, 'III')),
            ((25, 5), (5, 'V')),
            ((100, 10), (10, 'X')),
            ((1000, 50), (20, 'XX')),
        ]
        for (a, b), expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(RomanCalculator.divide(a, b), expected)

    def test_divide_roman_numbers(self):
        """Test division with Roman numerals."""
        test_cases = [
            (('VI', 'II'), (3, 'III')),
            (('XXV', 'V'), (5, 'V')),
            (('C', 'X'), (10, 'X')),
            (('M', 'L'), (20, 'XX')),
        ]
        for (a, b), expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(RomanCalculator.divide(a, b), expected)

    def test_mixed_number_types(self):
        """Test operations with mixed Arabic and Roman numbers."""
        self.assertEqual(RomanCalculator.add(10, 'X'), (20, 'XX'))
        self.assertEqual(RomanCalculator.subtract('C', 50), (50, 'L'))
        self.assertEqual(RomanCalculator.multiply(5, 'X'), (50, 'L'))
        self.assertEqual(RomanCalculator.divide('C', 4), (25, 'XXV'))

    def test_error_cases(self):
        """Test various error cases."""
        # Division by zero
        with self.assertRaises(ValueError):
            RomanCalculator.divide(10, 0)
        with self.assertRaises(KeyError):
            RomanCalculator.divide('X', 'N')  # Invalid Roman numeral
        
        # Result out of range
        with self.assertRaises(ValueError):
            RomanCalculator.multiply('MM', 'MM')  # 2000 * 2000 > 3999

if __name__ == '__main__':
    unittest.main()
