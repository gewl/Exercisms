NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Robot:

    def __init__(self, direction = NORTH, x = 0, y = 0):
        self.bearing = direction
        self.coordinates = (x, y)

    def turn_left(self):
        self.bearing -= 1
        if self.bearing < 0:
            self.bearing += 4

    def turn_right(self):
        self.bearing += 1
        if self.bearing > 3:
            self.bearing -= 4

    def advance(self):
        if self.bearing == NORTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
        if self.bearing == EAST:
            self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
        if self.bearing == SOUTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
        if self.bearing == WEST:
            self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])

    def simulate(self, commands):
        for char in commands:
            if char == "A":
                self.advance()
            if char == "L":
                self.turn_left()
            if char == "R":
                self.turn_right()
