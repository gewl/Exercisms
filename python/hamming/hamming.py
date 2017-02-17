def distance(first_strand, second_strand):
    first_array = list(first_strand)
    second_array = list(second_strand)
    counter = 0

    for a, b in zip(first_array, second_array):
        if a != b:
            counter += 1

    return counter
