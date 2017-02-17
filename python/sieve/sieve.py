def sieve(limit):
    num_list = [True for i in range (0, limit + 1)]
    num_list[0] = num_list[1] = False
    sieved_nums = []
    for idx, state in enumerate(num_list):
        if state:
            sieved_nums.append(idx)
            for num in xrange(idx*idx, limit + 1, idx):
                num_list[num] = False

    return sieved_nums
