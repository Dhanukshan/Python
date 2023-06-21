def get_new_string(string):
    if len(string) < 2:
        return ''
    else:
        new_string = string[:2] + string[-2:]
        return new_string
input_string = "arnesh"
output_string = get_new_string(input_string)
print(output_string)
