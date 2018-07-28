cats=20
dogs=30
if cats<dogs:
    print "More dogs than cats."
elif cats>dogs:
    print "More cats than dogs."
else:
    print "Same number of dogs and cats."

print
from sys import argv
import numpy as np
def cir(r):
    r=float(r)
    c=2*np.pi*r
    return c
cearth=cir(6378)
cmars=cir(3396)
script,rinput=argv
rinput=float(rinput)
cinput=cir(rinput)
if  cinput>(cearth+cmars)/2:
    print "Earth"
elif cinput<(cearth+cmars)/2:
    print "Mars"
else:
    print "Same"
