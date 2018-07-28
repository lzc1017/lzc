a={1,2,3}
b={1:'a',2:'b',3:'c'}
for i in a:
    print b[i]
    print 1+3

print
r=range(11)
for i in r:
    print str(r[i]/10.0+1)+'^'+str(r[i]/10.0+1)+'='+str((r[i]/10.0+1)**(r[i]/10.0+1))
