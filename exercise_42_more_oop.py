##Animal is-a obect *yes, sort of confusing* look at the extra credit
class Animal(object):
    pass

## Dog is an Animal
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## Cat is an Animal
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## Person is a object
class Person(object):
    def __init__(self, name):
        ## person has a name
        self.name = name
        ##Person has-a pet of some kind
        self.pet = None

##employee is a person
class Employee(Person):
    def __init__(self, name, salary):
        ##employee has a name
        super(Employee, self).__init__(name)
        ## employee has a salary
        self.salary = salary

## fish is an object
class Fish(object):
    pass

##salmon is a fish
class Salmon(Fish):
    pass

## Halibut is a fish
class Halibut(Fish):
    pass

##Rover is-a dog
rover = Dog("Rover")

##satan is a cat
satan = Cat("Satan")

##mary is a erson
mary = Person("Mary")

##mary has a pet
mary.pet = satan

##frank is an employee
frank = Employee("Frank", 120000)

##frank has a pet
frank.pet = rover

##flipper is a fish
flipper = Fish()

##crouse is a salmon
crouse = Salmon()

##harry is a halibut
harry = Halibut()
