import numpy as np
c=np.pi*2*6378
s=np.pi*6378**2
print "Earth\n\t circumference\t%f\n\t surface area\t%f" %(c,s)

print
print "What's your name?"
name=raw_input()
print "How old are you?"
age=raw_input()
print "My name is %s and I am %s years old." %(name,age)

print
name=raw_input("What's your name?")
age=raw_input("How old are you?")
print "My name is %s and I am %s years old." %(name,age)
