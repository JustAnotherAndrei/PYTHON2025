def count_words(text):
    if not text:  # Handle empty string case
        return 0
    # Split by single space and return the number of elements
    return len(text.split(' '))


# Example usage
if __name__ == "__main__":
    test_cases = [
        "I have a Python exam",  # 4 words
        "Suna telefoanele, ca dracii", # 4 words
        "Hello",  # 1 word
        "",  # 0 words (empty string)
        "  "
    ]

    for test in test_cases:
        print(f"'{test}': {count_words(test)} words")