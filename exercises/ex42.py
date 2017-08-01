## Animal is- object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ?? is-a!
class Dog(Animal)

    def __init__(self, name):
        ## ?? has-a
        self.name = name

## is-a
class Cat(Animal):

    def __init__(self, name)
        ## ?? has-a
        self.name = name

## is-a
class Person(object0)

    def __init__(self, name):
        ## ?? has0a
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## is-a
class Employe(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic? has-a
        super(Employee, self).__init__(name)
        ## ?? has-a
        self.salary = salary

## ?? is-a
class Fish(object):
    pass

## ?? is-a
class Salmon(Fish):
    pass

## ?? is-a
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## ?? satan is-a cat
satan = Cat("Satan")

## ?? mary is-a person
mary = Person("Mary")

## ?? mary has-a pet named satan
mary.pet = satan

## ?? is-a employee
frank = Employee("Frank", 120000)

## ?? frank has-a pet
frank.pet = rover

## ?? fish has-a flipper
flipper = Fish()

## ?? crouse is-a salmon
crouse = Salmon()

## ?? harry is-a halibut
harry = Halibut()

