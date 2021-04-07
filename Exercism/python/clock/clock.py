import unittest

class Clock:
    def __init__(self, hour, minute):
        self.minutes = hour*60 + minute
        # Need to include case where it excedes 24 hours
        self.minutes = self.minutes % (24*60)


    def __repr__(self):
        return "%02d:%02d" % (self.minutes//60, self.minutes % 60)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __add__(self, minutes):
        self.minutes += minutes
        self.minutes = self.minutes % (24*60)
        return self

    def __sub__(self, minutes):
        # need to include case with negative minutes
        if self.minutes - minutes <= 0:
            self.minutes += (24*60) * (-(self.minutes-minutes)//1440 + 1)
        self.minutes -= minutes
        return self

