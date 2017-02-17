class School:
    def __init__(self, name):
        self.name = name
        self.grades = {}
        for n in range(1,9):
            self.grades[n] = []

    def grade(self, num):
        return self.grades[num]

    def add(self, name, num):
        self.grades[num].append(name)

    def sort(self):
        for i in self.grades:
            self.grades[i].sort()

        result = []
        for j in self.grades:
            if len(self.grades[j]) > 0:
                result.append((j, tuple(name for name in self.grades[j])))

        return result
