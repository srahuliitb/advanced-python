from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):

    def person_method():
        """ Interface method. """

class Person(IPerson):
    
    def person_method(self):
        print("This is a person.")

class ProxyPerson(IPerson):
    
    def __init__(self):
        self.person = Person()

    def person_method(self):
        print('This is the proxy functionality.')
        self.person.person_method()

p1 = Person()
p2 = ProxyPerson()

p1.person_method()
p2.person_method()