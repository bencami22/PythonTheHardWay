##----------------------------------Inheritance---------------------------------
class Parent(object):
    def override(self):
        print("PARENT OVERRIDE")

    def implicit(self):
        print("PARENT IMPLICIT")

    def altered(self):
        print("PARENT ALTERED")

class Child(Parent):
    def override(self):
        print("CHILD OVERRIDE")

    def implicit(self):
        pass

    def altered(self):
        print("CHILD ALTERED 1")
        super(Child, self).altered()
        print("CHILD ALTERED 2")

child=Child()
child.override()
child.implicit()
child.altered()

##----------------------------------Composition---------------------------------

class Other(object):
    def override(self):
        print("OTHER OVERRIDE")

    def implicit(self):
        print("OTHER IMPLICIT")

    def altered(self):
        print("OTHER ALTERED")

class CompChild(object):
    def __init__(self):
        self.other=Other()

    def override(self):
        print("CHILD OVERRIDE")

    def implicit(self):
        self.other.implicit()

    def altered(self):
        print("CHILD ALTERED 1")
        self.other.altered()
        print("CHILD ALTERED 1")

son = CompChild()
son.implicit()
son.override()
son.altered()
