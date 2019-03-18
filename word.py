from collections import OrderedDict


class Word:
    def __init__(self, m, v, h, f, wind, time=0.001):
        self._m = float(m)
        self._v = float(v)
        self._h = float(h)
        self._f = OrderedDict(f)
        self._wind = OrderedDict(wind)
        self._g = 9.81
        self._time = float(time)

    def update(self):
        if self._h <= 0:
            self._v = 0
            self._h = 0
            return

        self._h -= self._time * (self._v + (self._g * self._time) / 2)
        self._v += self._g * self._time
