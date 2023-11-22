import string

def clean_url(input_string):
    punctuation = string.punctuation
    # Find the last occurrence of a punctuation character in the URL
    last_punctuation_index = -1
    for i in range(len(input_string) - 1, -1, -1):
        if input_string[i] in punctuation:
            last_punctuation_index = i
            break
    # If punctuation is found at the end, remove it and everything after it
    if last_punctuation_index >= 0 and input_string[last_punctuation_index] != '/':
        cleaned_url = input_string[:last_punctuation_index]
    else:
        cleaned_url = input_string

    return cleaned_url