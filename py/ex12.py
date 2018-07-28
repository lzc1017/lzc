p1=[1,2,3,'a','b','c']
p2=(1,2,3,'a','b','c')
p3=range(3)
print 2 in p1
print 'a' not in p2
print p1+p1
print p3*2
print p2[4]
print p1[1:3]
print p2[1:6:2]
print len(p2)
print max(p2)
print p1.count('a')
print p1.index('a',3,4)

p1[0]='qq'
p1[1:3]='ww'
del p1[3:5]
p1.append('ee')
print p1

p4={'q':1,'w':2,'e':3,(1,2):4}
print p4
print p4['q']
print p4[(1,2)]
