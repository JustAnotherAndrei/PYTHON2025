def count_occurrences(substring, text):
    if not substring:  # Handle empty substring case
        return 0
    return text.count(substring)

if __name__ == "__main__":
    test_cases = [
        ("ana", "banana"),  # 2
        ("aa", "aaaa"),  # 2 (non-overlapping)
        ("test", "testing"),  # 1
        ("hello", "world"),  # 0
        ("", "empty")  # 0 (empty substring)
    ]

    for sub, txt in test_cases:
        count = count_occurrences(sub, txt)
        print(f"'{sub}' occurs {count} time(s) in '{txt}'")