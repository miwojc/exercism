class SpaceAge:
    SECONDS_EARTH = 31557600
    RATIOS = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def __init__(self, seconds):
        self.seconds = seconds

    def earth_years_old(self, ratio):
        return round(self.seconds / SpaceAge.SECONDS_EARTH / ratio, 2)

    def on_mercury(self):
        return self.earth_years_old(SpaceAge.RATIOS["mercury"])

    def on_venus(self):
        return self.earth_years_old(SpaceAge.RATIOS["venus"])

    def on_earth(self):
        return self.earth_years_old(SpaceAge.RATIOS["earth"])

    def on_mars(self):
        return self.earth_years_old(SpaceAge.RATIOS["mars"])

    def on_jupiter(self):
        return self.earth_years_old(SpaceAge.RATIOS["jupiter"])

    def on_saturn(self):
        return self.earth_years_old(SpaceAge.RATIOS["saturn"])

    def on_uranus(self):
        return self.earth_years_old(SpaceAge.RATIOS["uranus"])

    def on_neptune(self):
        return self.earth_years_old(SpaceAge.RATIOS["neptune"])
