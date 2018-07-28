def f1(d1,d2):
    d1=float(d1)
    d2=float(d2)
    d=d1-d2
    return d
print "5.444-3.316="+str(f1(5.444,3.316))

print
import numpy as np
def f2(r):
    r=float(r)
    c=2*np.pi*r
    return c
print "Earth's circumference:",f2(6378)

print
print "Mars's circumference:",f2(3396)
