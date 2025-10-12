import re


def extract_first_number(text):

    match = re.search(r'\d+', text)
    return int(match.group()) if match else None


if __name__ == "__main__":
    test_cases = [
        "An apple is 123 USD",  # 123
        "abc123abc",  # 123
        "Price: 45.99",  # 45
        "No numbers here",  # None
        "Multiple 123 numbers 456",  # 123
        "123",  # 123
        "abc",  # None
        ""  # None
        "I'll have two number 9, a number 9 large, a number 7, a number 6 with extra dip, two number 45, one with cheese, and a large soda. "
    ]

    for test in test_cases:
        result = extract_first_number(test)
        print(f"'{test}' -> {result}")