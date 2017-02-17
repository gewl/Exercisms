def slices(string, length):
    if length > len(string) or length < 1:
        raise ValueError
    result_list = []
    for i in range (len(string) - length + 1):
        result_list.append(map(int, string[i:i + length]))
    return result_list

