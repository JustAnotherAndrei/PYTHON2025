# Read a string from the user
text = input("Enter a string: ")

# Build a new string containing only letters
only_letters = ''.join(ch for ch in text if ch.isalpha())

# Display the result
print("String with only letters:", only_letters)
