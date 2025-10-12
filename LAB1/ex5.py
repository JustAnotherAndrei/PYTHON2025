def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

if __name__ == "__main__":
    test_numbers = [121,7327627, 1010101, -563820, 1234321, 135797531, 3, 0]
    for num in test_numbers:
        print(f"{num}: {'is' if is_palindrome(num) else 'is not'} a palindrome")