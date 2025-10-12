def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary_digits = []
    is_negative = n < 0
    n = abs(n)  # Work with positive numbers first

    while n > 0:
        binary_digits.append(str(n % 2))  # Get the least significant bit
        n = n // 2  # Right shift (integer division by 2)

    # Reverse to get the correct order and handle negative numbers
    binary_str = ''.join(reversed(binary_digits))
    return f"-{binary_str}" if is_negative else binary_str


# Example usage
if __name__ == "__main__":
    test_numbers = [0, 5, 10, 42, -13]
    for num in test_numbers:
        print(f"Decimal: {num:3} -> Binary: {decimal_to_binary(num)}")