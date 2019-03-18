from csv import DictReader
from collections import OrderedDict


def read(path):
    f = open(path)
    d = DictReader(f, delimiter=',')
    out = OrderedDict()
    if len(d.fieldnames) == 2:
        for i in d:
            out[int(i[d.fieldnames[0]])] = float(i[d.fieldnames[1]])
    else:
        for i in d:
            out[int(i[d.fieldnames[0]])] = (float(i[d.fieldnames[1]]), float(i[d.fieldnames[2]]))
    f.close()
    return out


class Missile:
    def __init__(self, mass=100, vx=0, vy=0, vz=0, coords=(0, 1000, 0)):
        self.mass = mass
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.v = (vx * vx + vz * vz)**0.5
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]

    def v_count(self):
        self.v = (self.vx * self.vx + self.vz * self.vz)**0.5
        return self.v


d1 = read("Data/F.csv")
d2 = read("Data/Wind.csv")

G = 9.81
t = 0

gruz = Missile()

while gruz.y > 0:
    pass
