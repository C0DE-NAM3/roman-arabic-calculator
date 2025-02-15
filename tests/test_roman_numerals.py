import unittest
from roman_numerals import RomanNumerals

class TestRomanNumerals(unittest.TestCase):
    def test_to_roman_basic_numbers(self):
        """Test basic number conversions to Roman numerals."""
        test_cases = [
            (1, 'I'),
            (4, 'IV'),
            (5, 'V'),
            (9, 'IX'),
            (10, 'X'),
            (40, 'XL'),
            (50, 'L'),
            (90, 'XC'),
            (100, 'C'),
            (400, 'CD'),
            (500, 'D'),
            (900, 'CM'),
            (1000, 'M'),
        ]
        for arabic, roman in test_cases:
            with self.subTest(arabic=arabic):
                self.assertEqual(RomanNumerals.to_roman(arabic), roman)

    def test_to_roman_complex_numbers(self):
        """Test more complex number conversions to Roman numerals."""
        test_cases = [
            (14, 'XIV'),
            (99, 'XCIX'),
            (2023, 'MMXXIII'),
            (3999, 'MMMCMXCIX'),
        ]
        for arabic, roman in test_cases:
            with self.subTest(arabic=arabic):
                self.assertEqual(RomanNumerals.to_roman(arabic), roman)

    def test_from_roman_basic_numbers(self):
        """Test basic Roman numeral conversions to numbers."""
        test_cases = [
            ('I', 1),
            ('IV', 4),
            ('V', 5),
            ('IX', 9),
            ('X', 10),
            ('XL', 40),
            ('L', 50),
            ('XC', 90),
            ('C', 100),
            ('CD', 400),
            ('D', 500),
            ('CM', 900),
            ('M', 1000),
        ]
        for roman, arabic in test_cases:
            with self.subTest(roman=roman):
                self.assertEqual(RomanNumerals.from_roman(roman), arabic)

    def test_from_roman_complex_numbers(self):
        """Test more complex Roman numeral conversions to numbers."""
        test_cases = [
            ('XIV', 14),
            ('XCIX', 99),
            ('MMXXIII', 2023),
            ('MMMCMXCIX', 3999),
        ]
        for roman, arabic in test_cases:
            with self.subTest(roman=roman):
                self.assertEqual(RomanNumerals.from_roman(roman), arabic)

    def test_invalid_roman_numerals(self):
        """Test that invalid Roman numerals raise ValueError."""
        invalid_numerals = [
            'IIII',  # Should be IV
            'VV',    # Invalid repetition
            'IC',    # Invalid subtractive
            'XM',    # Invalid subtractive
            'MMMM',  # Exceeds 3999
        ]
        for numeral in invalid_numerals:
            with self.subTest(numeral=numeral):
                with self.assertRaises(ValueError):
                    RomanNumerals.from_roman(numeral)

    def test_out_of_range_numbers(self):
        """Test that numbers outside valid range raise ValueError."""
        invalid_numbers = [0, -1, 4000, 5000]
        for number in invalid_numbers:
            with self.subTest(number=number):
                with self.assertRaises(ValueError):
                    RomanNumerals.to_roman(number)

    def test_case_insensitivity(self):
        """Test that Roman numeral parsing is case-insensitive."""
        test_cases = [
            ('xiv', 14),
            ('XCIX', 99),
            ('mmxxiii', 2023),
            ('MmXxIiI', 2023),
        ]
        for roman, arabic in test_cases:
            with self.subTest(roman=roman):
                self.assertEqual(RomanNumerals.from_roman(roman), arabic)

if __name__ == '__main__':
    unittest.main()
