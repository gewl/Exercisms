from collections import OrderedDict

def numeral(arabic):
    res_str = ''
    while arabic >= 1000:
        res_str += 'M'
        arabic -= 1000

    while arabic >= 900:
        res_str += 'CM'
        arabic -= 900

    while arabic >= 500:
        res_str += 'D'
        arabic -= 500

    while arabic >= 400:
        res_str += 'CD'
        arabic -= 400

    while arabic >= 100:
        res_str += 'C'
        arabic -= 100

    while arabic >= 90:
        res_str += 'XC'
        arabic -= 90

    while arabic >= 50:
        res_str += 'L'
        arabic -= 50

    while arabic >= 40:
        res_str += 'XL'
        arabic -= 40

    while arabic >= 10:
        res_str += 'X'
        arabic -= 10

    while arabic >= 9:
        res_str += 'IX'
        arabic -= 9

    while arabic >= 5:
        res_str += 'V'
        arabic -= 5

    while arabic >= 4:
        res_str += 'IV'
        arabic -= 4

    while arabic >= 1:
        res_str += 'I'
        arabic -= 1

    return res_str
