from roman_numerals import RomanNumerals
from calculator import RomanCalculator

def print_roman_guide():
    """Print an educational guide about Roman numerals."""
    print("\n🏛️ Roman Numeral Learning Guide 🏛️")
    print("\nRoman Numeral Basics:")
    print("I   = 1")
    print("V   = 5")
    print("X   = 10")
    print("L   = 50")
    print("C   = 100")
    print("D   = 500")
    print("M   = 1000")
    print("\nSpecial Rules:")
    print("- Symbols are combined from left to right")
    print("- Smaller values before larger values mean subtraction")
    print("  Example: IV = 4, IX = 9, XL = 40")
    print("\nValid Range: 1 to 3999")

def main():
    while True:
        print("\n🧮 Roman Numeral Calculator 🧮")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Roman Numeral Guide")
        print("6. Exit")
        
        choice = input("Choose an operation (1-6): ")
        
        if choice == '5':
            print_roman_guide()
            continue
        
        if choice == '6':
            print("Thank you for using the Roman Numeral Calculator!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue
        
        print("\nEnter numbers. You can use:")
        print("- Arabic numbers (1, 2, 3)")
        print("- Roman numerals (I, V, X)")
        
        try:
            a = input("First number: ")
            b = input("Second number: ")
            
            # Convert input to int or keep as string for Roman
            a_val = int(a) if a.isdigit() else a.upper()
            b_val = int(b) if b.isdigit() else b.upper()
            
            if choice == '1':
                result, roman_result = RomanCalculator.add(a_val, b_val)
            elif choice == '2':
                result, roman_result = RomanCalculator.subtract(a_val, b_val)
            elif choice == '3':
                result, roman_result = RomanCalculator.multiply(a_val, b_val)
            elif choice == '4':
                result, roman_result = RomanCalculator.divide(a_val, b_val)
            
            print(f"\nResult (Arabic): {result}")
            print(f"Result (Roman): {roman_result}")
        
        except ValueError as e:
            print(f"Error: {e}")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
