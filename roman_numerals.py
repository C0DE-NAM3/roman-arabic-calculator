class RomanNumerals:
    """Utility class for converting between Arabic and Roman numerals."""
    
    ROMAN_VALUES = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    @staticmethod
    def to_roman(number):
        """Convert Arabic number to Roman numeral."""
        if not 0 < number < 4000:
            raise ValueError("Roman numerals support numbers between 1 and 3999")
        
        result = ''
        for value, symbol in RomanNumerals.ROMAN_VALUES:
            while number >= value:
                result += symbol
                number -= value
        return result
    
    @staticmethod
    def from_roman(roman_str):
        """Convert Roman numeral to Arabic number."""
        roman_str = roman_str.upper()
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in reversed(roman_str):
            current_value = roman_map[char]
            if current_value >= prev_value:
                total += current_value
            else:
                total -= current_value
            prev_value = current_value
        
        # Validate the Roman numeral
        if RomanNumerals.to_roman(total) != roman_str:
            raise ValueError(f"Invalid Roman numeral: {roman_str}")
        
        return total
