class Luhn:
    def __init__(self, num):
        self.num = num
        self._addends = self._generate_addends(num)

        num_list = [int(i) for i in str(num)]
        num_list.reverse()
        self.csum = self.generate_checksum(num_list)

        self.valid = (self.csum % 10 == 0)

    def checksum(self):
        return self.csum

    def is_valid(self):
        return self.valid

    def addends(self):
        return self._addends

    def _generate_addends(self, num):
        num_list = [int(i) for i in str(num)]
        num_list.reverse()
        result = []
        for idx, digit in enumerate(num_list):
            if (idx % 2 == 0):
                result.append(digit)
            else:
                tentative_double = digit * 2
                if (tentative_double >= 10):
                    tentative_double -= 9
                result.append(tentative_double)
        return result

    @classmethod
    def generate_checksum(self, nlist):
        result = 0
        for idx, digit in enumerate(nlist):
            if (idx % 2 == 0):
                result += digit
            else:
                tentative_double = digit * 2
                if (tentative_double >= 10):
                    tentative_double -= 9
                result += tentative_double
        return result

    @classmethod
    def create(self, num):
        num_list = [int(i) for i in str(num)]
        num_list.append(0)
        num_list.reverse()
        temp_checksum = self.generate_checksum(num_list)
        remainder = temp_checksum%10
        checkdigit = 10 - remainder if remainder != 0 else 0
        return int( str(num) + str(checkdigit) )
