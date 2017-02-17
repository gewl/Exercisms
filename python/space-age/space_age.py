from __future__ import division

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self._earth_year = 31557600
        self._mercury_year = self._earth_year * 0.2408467
        self._venus_year = self._earth_year * 0.61519726
        self._mars_year = self._earth_year * 1.8808158
        self._jupiter_year = self._earth_year * 11.862615
        self._saturn_year = self._earth_year * 29.447498
        self._uranus_year = self._earth_year * 84.016846
        self._neptune_year = self._earth_year * 164.79132

    def on_earth(self):
        return round(self.seconds/self._earth_year, 2)

    def on_mercury(self):
        return round(self.seconds/self._mercury_year, 2)

    def on_venus(self):
        return round(self.seconds/self._venus_year, 2)

    def on_mars(self):
        return round(self.seconds/self._mars_year, 2)

    def on_jupiter(self):
        return round(self.seconds/self._jupiter_year, 2)

    def on_saturn(self):
        return round(self.seconds/self._saturn_year, 2)

    def on_uranus(self):
        return round(self.seconds/self._uranus_year, 2)

    def on_neptune(self):
        return round(self.seconds/self._neptune_year, 2)
