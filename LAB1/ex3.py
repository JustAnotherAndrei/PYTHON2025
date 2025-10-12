def count_prefixes(x, y):
    # Split the input strings into lists of words
    words_x = x.split()
    words_y = y.split()

    # Create a set of all possible prefixes from words in y
    y_prefixes = set()
    for word in words_y:
        for i in range(1, len(word) + 1):
            y_prefixes.add(word[:i])

    # Count how many words in x are in the set of prefixes
    count = 0
    for word in words_x:
        if word in y_prefixes:
            count += 1

    return count


# Example usage
if __name__ == "__main__":
    x = "ap app appl banana banananana hell"
    y = "apple banana application app appliances hello"
    result = count_prefixes(x, y)
    print(f"Number of prefix matches: {result}")  # Output: 3 ("ap", "app", "appl" are all prefixes of "apple")
