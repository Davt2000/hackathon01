import csv
from collections import OrderedDict


def read(obj):
    d = csv.DictReader(obj, delimiter=',')
    return d


f1 = open("Data/F.csv")
f2 = open("Data/Wind.csv")

d1 = read(f1)
d2 = read(f2)

print(*d1, sep="\n")
print("******\n")
print(*d2, sep="\n")

f1.close()
f2.close()