class SpaceAge:
    seconds_earth = 31557600

    def __init__(self, seconds):
        self.seconds = seconds

    def earth_years_old(self, ratio):
        return round(self.seconds / SpaceAge.seconds_earth / ratio, 2)

    def on_mercury(self):
        return self.earth_years_old(0.2408467)

    def on_venus(self):
        return self.earth_years_old(0.61519726)

    def on_earth(self):
        return self.earth_years_old(1)

    def on_mars(self):
        return self.earth_years_old(1.8808158)

    def on_jupiter(self):
        return self.earth_years_old(11.862615)

    def on_saturn(self):
        return self.earth_years_old(29.447498)

    def on_uranus(self):
        return self.earth_years_old(84.016846)

    def on_neptune(self):
        return self.earth_years_old(164.79132)
