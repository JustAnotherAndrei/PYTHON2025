def camel_to_snake(camel_str):

    if not camel_str:
        return ""

    snake_case = [camel_str[0].lower()]

    for char in camel_str[1:]:
        if char.isupper():
            snake_case.append('_' + char.lower())
        else:
            snake_case.append(char)

    return ''.join(snake_case)

if __name__ == "__main__":
    test_cases = [
        "MyVariableName",  # my_variable_name
        "HTTPRequest",  # http_request
        "UserID",  # user_id
        "Simple",  # simple
        "CamelCaseString",  # camel_case_string
        ""  # (empty string)
    ]

    for test in test_cases:
        print(f"'{test}' -> '{camel_to_snake(test)}'")