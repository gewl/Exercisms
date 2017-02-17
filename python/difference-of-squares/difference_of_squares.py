import math

def difference(n):
    return square_of_sum(n) - sum_of_squares(n)

def square_of_sum(n):
    sum = (n * (n+1))/2
    return math.pow(sum, 2)

def sum_of_squares(n):
    sum = 0
    for x in range (0, n+1):
        sum += math.pow(x, 2)
    return sum
