import math

def say(num):
    if num < 0 or num >= 1e12:
        raise AttributeError("Bad digits")
    num = int(num)
    string_num = str(num)
    list_num = [int(i) for i in string_num]

    single_digit_dict = {
            0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"
            }

    teen_dict = {
            11: 'eleven',
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen"
            }

    double_digit_dict = {
            2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "ninety"
            }

    if len(string_num) == 1:
        return single_digit_dict[num]
    elif len(string_num) == 2:
        if (num < 20):
            return teen_dict[num]
        else:
            result_string = double_digit_dict[list_num[0]]
            if (num % 10 == 0):
                result_string
            else:
                result_string += '-' + say(list_num[1])
    elif len(string_num) == 3:
        result_string = single_digit_dict[list_num[0]] + ' hundred'
        if (num % 100 == 0):
            result_string
        else:
            result_string += ' and ' + say(int(string_num[1:]))
    elif len(string_num) > 3 and len(string_num) < 7:
        thousand_places = len(string_num) - 3
        result_string = say(int(string_num[0:thousand_places])) + ' thousand'
        if (num % 1000 == 0):
            result_string
        else:
            result_string += ' ' + say(int(string_num[thousand_places:]))
    elif len(string_num) > 6 and len(string_num) < 10:
        million_places = len(string_num) - 6
        result_string = say(int(string_num[0:million_places])) + ' million'
        if (num % 1000 == 0):
            result_string
        else:
            result_string += ' ' + say(int(string_num[million_places:]))
    elif len(string_num) > 9:
        billion_places = len(string_num) - 9
        result_string = say(int(string_num[0:billion_places])) + ' billion'
        if (num % 1000 == 0):
            result_string
        else:
            result_string += ' ' + say(int(string_num[billion_places:]))

    result_list = result_string.split(' ')
    if 'and' not in result_list and len(result_list) > 2:
        last = result_list.pop()
        result_list.append('and')
        result_list.append(last)
    return ' '.join(result_list)
