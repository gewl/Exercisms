def encode(string):
    current_letter = ''
    current_count = 1
    result_string = ''

    for letter in string:
        if letter == current_letter:
            current_count += 1
        else:
            if current_count == 1:
                result_string = result_string + current_letter
            else:
                result_string = ''.join((result_string, str(current_count), current_letter))
            current_letter = letter
            current_count = 1
    if current_count == 1:
        result_string = result_string + current_letter
    else:
        result_string = ''.join((result_string, str(current_count), current_letter))

    return result_string

def decode(string):
    current_count = ''
    result_string = ''

    for char in string:
        if char.isnumeric():
            current_count = current_count + char
        else:
            if len(current_count) > 0:
                expanded_string = char * int(current_count)
                result_string = result_string + expanded_string
                current_count = ''
            else:
                result_string = result_string + char
    return result_string
