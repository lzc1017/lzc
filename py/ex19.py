class parent(object):
    def implicit(self):
        print "parent implicit()"
class child(parent):
    pass
dad=parent()
son=child()
dad.implicit()
son.implicit()

print
class parent(object):
    def override(self):
        print "parent override()"
class child(object):
    def override(self):
        print "child override()"
dad=parent()
son=child()
dad.override()
son.override()

print
class parent(object):
    def altered(self):
        print "parent altered()"
class child(parent):
    def altered(self):
        print "child altered()"
        super(child,self).altered()
dad=parent()
son=child()
dad.altered()
son.altered()

print
class parent(object):
    def fun(self):
        print "parent fun()"
class child(object):
    def __init__(self):
        self.parent=parent()
    def fun(self):
        self.parent.fun()
dad=parent()
son=child()
dad.fun()
son.fun()

