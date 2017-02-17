import math

class Allergies(object):

    def __init__(self, num):
        self.lst = []

        allergies_dict = {
                0: 'eggs',
                1: 'peanuts',
                2: 'shellfish',
                3: 'strawberries',
                4: 'tomatoes',
                5: 'chocolate',
                6: 'pollen',
                7: 'cats'
                }

        while num > 255:
            ignored_component = math.floor(math.log(num, 2))
            num -= 2 ** ignored_component

        while num > 0:
            next_allergy = math.floor(math.log(num, 2))
            self.lst.append(allergies_dict[next_allergy])
            num -= 2 ** next_allergy

    def is_allergic_to(self, allergy):
        if allergy in self.lst:
            return True
        else:
            return False
