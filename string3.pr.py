def find_longest_word(sentence):
    words = sentence.split()  
    longest_word = ''
    longest_length = 0

    for word in words:
        if len(word) > longest_length:
            longest_word = word
            longest_length = len(word)

    return longest_word, longest_length


input_sentence = "The quicks brown fox jumps over the lazy dog"
longest_word, length = find_longest_word(input_sentence)
print("Longest word:", longest_word)
print("Length of longest word:", length)
