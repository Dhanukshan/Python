def swap_string(string1,string2):
    if len(string1)>=2 and len(string2)>=2:
        new_string1=string2[2:]+string1[:2]
        new_string2=string1[2:]+string2[:2]
        return new_string1 + ' ' + new_string2
    else:
        return string1 + ' ' + string2
input_string1 = "Mike"
input_string2 = "Dice"
output_string = swap_and_combine_strings(input_string1, input_string2)
print(output_string)
