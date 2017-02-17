def sum_of_multiples(num, arr):
    multiples = []

    for i in arr:
        j = i
        while j < num and j != 0:
            if j not in multiples:
                multiples.append(j)
            j += i

    return sum(multiples)
