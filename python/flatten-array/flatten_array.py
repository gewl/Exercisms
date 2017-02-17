def flatten(arr):
    res_arr = []
    for i in arr:
        if type(i) is int or type(i) is str:
            res_arr.append(i)
        elif type(i) is list:
            res_arr = res_arr + flatten(i)

    return res_arr
