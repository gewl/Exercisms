class Clock(object):
    def __init__(self, raw_hours, raw_minutes):
        hours = str((raw_hours + raw_minutes/60) % 24)
        if len( hours ) == 1:
            hours = "0" + hours
        self.hours = hours

        minutes = str(raw_minutes % 60)
        if len( minutes ) == 1:
            minutes = "0" + minutes
        self.minutes = minutes

        self.time = "%s:%s" % ( self.hours, self.minutes )

    def __str__(self):
        return self.time

    def __eq__(self, other_clock):
        return self.time == other_clock.time

    def add(self, raw_minutes):
        new_minutes = int(self.minutes) + raw_minutes
        if new_minutes < 0 or new_minutes > 60:
            self.hours = int(self.hours) + (new_minutes/60)

            if self.hours < 0 or self.hours > 23:
                self.hours = self.hours % 24
            self.hours = str(self.hours)

            if len( self.hours ) == 1:
                self.hours = "0" + self.hours
            new_minutes = new_minutes % 60

        new_minutes = str(new_minutes)

        if len( new_minutes ) == 1:
            new_minutes = "0" + new_minutes

        self.minutes = new_minutes
        self.time = "%s:%s" % ( self.hours, self.minutes )
        return self.time
