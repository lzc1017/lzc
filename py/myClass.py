class fruit(object):
    def __init__(self):
        self.edible=True
        self.cook=False
    def peel(self):
        print "Peel me,please."

class organism(object):
    def __init__(self):
        self.alive=True
class animal(organism):
    def __init__(self):
        super(animal,self).__init__()
        self.moving=True
        self.eating=True
    def kill(self):
        self.alive=False
class vertebrate(animal):
    def __init__(self):
        super(vertebrate,self).__init__()
        self.spnie=True
class mammal(vertebrate):
    def __init__(self):
        super(mammal,self).__init__()
        self.milk=True
        self.egg=False
class dog(mammal):
    def __init__(self):
        super(dog,self).__init__()
        self.carnivorous=True
    def bark(self):
        print "Woof Woof Woof"
