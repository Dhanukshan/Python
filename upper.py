def process_string(input_string):
    string_length = len(input_string)

    if string_length % 5 == 0:
        # Reverse the string and capitalize all characters
        processed_string = input_string[::-1].upper()
    else:
        # If the length is not a multiple of 5, keep the original string
        processed_string = input_string

    return processed_string

# Test the function
input_string = "helloworld"
result = process_string(input_string)
print("Processed string:", result)