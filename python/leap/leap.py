def is_leap_year(num):
    return num % 400 == 0 or (num % 4 == 0 and num % 100 != 0)

