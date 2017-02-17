class Garden:
    def __init__(self, garden, students = None):
        self.students = students
        if self.students != None:
            self.students.sort()
        self.garden = garden.split('\n')

    _plant_guide = {
            "V": "Violets",
            "C": "Clover",
            "G": "Grass",
            "R": "Radishes"
            }

    def plants(self, kid):
        if self.students == None:
            kid_code = ord(kid[0]) - 65
        else:
            kid_code = self.students.index(kid)
        kid_matrix = [[(kid_code * 2), 1 + (kid_code * 2)], [(kid_code * 2), 1 + (kid_code * 2)]]
        result_list = []
        for idx, coords in enumerate(kid_matrix):
            for coord in coords:
                result_list.append(self._plant_guide[self.garden[idx][coord]])

        return result_list
