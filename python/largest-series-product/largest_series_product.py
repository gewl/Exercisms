from operator import mul

def slices(string, length):
    if length > len(string) or length < 1:
        raise ValueError
    result_list = []
    for i in range (len(string) - length + 1):
        result_list.append(map(int, string[i:i + length]))
    return result_list

def largest_product(series, n):
    if n == 0:
        return 1
    result_list = slices(series, n)
    current_max = 0
    for set in result_list:
        product = reduce(mul, set, 1)
        if product > current_max:
            current_max = product

    return current_max
