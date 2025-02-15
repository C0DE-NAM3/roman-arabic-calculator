from roman_numerals import RomanNumerals

class RomanCalculator:
    """A calculator that supports both Arabic and Roman numeral operations."""
    
    @staticmethod
    def add(a, b):
        """Add two numbers (can be Arabic or Roman)."""
        a_val = a if isinstance(a, int) else RomanNumerals.from_roman(a)
        b_val = b if isinstance(b, int) else RomanNumerals.from_roman(b)
        result = a_val + b_val
        return result, RomanNumerals.to_roman(result)
    
    @staticmethod
    def subtract(a, b):
        """Subtract two numbers (can be Arabic or Roman)."""
        a_val = a if isinstance(a, int) else RomanNumerals.from_roman(a)
        b_val = b if isinstance(b, int) else RomanNumerals.from_roman(b)
        result = a_val - b_val
        return result, RomanNumerals.to_roman(abs(result)) if result >= 0 else f"-{RomanNumerals.to_roman(abs(result))}"
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers (can be Arabic or Roman)."""
        a_val = a if isinstance(a, int) else RomanNumerals.from_roman(a)
        b_val = b if isinstance(b, int) else RomanNumerals.from_roman(b)
        result = a_val * b_val
        return result, RomanNumerals.to_roman(result)
    
    @staticmethod
    def divide(a, b):
        """Divide two numbers (can be Arabic or Roman)."""
        a_val = a if isinstance(a, int) else RomanNumerals.from_roman(a)
        b_val = b if isinstance(b, int) else RomanNumerals.from_roman(b)
        if b_val == 0:
            raise ValueError("Division by zero is not allowed")
        result = a_val // b_val  # Integer division
        return result, RomanNumerals.to_roman(result)
