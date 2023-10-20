from abc import ABCMeta, abstractclassmethod

### Create an interface called person. All interface names must begin with 'I'
class IPerson(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    
    @abstractclassmethod
    def person_method():
        """This is an interface method."""

# Interfaces cannot be instantiated. The following code (if executed) will throw an error.
# person1 = IPerson()
# print(person1)

### Create a Student class
class Student(IPerson):
    def _init__(self, name):
        self.name = name

    def person_method(self):
        return f"Student name is {self.name.title()}."
    
### Create a Teacher class.
class Teacher(IPerson):
    def __init_(self, name):
        self.name = name

    def person_method(self):
        return f"Teacher name is {self.name.title()}."

class PersonFactory:
    
    @staticmethod
    def build_person(person_type, person_name):
        build_object = None
        if person_type == 'student':
            build_object = Student(person_name)
            return build_object
        elif person_type == 'teacher':
            build_object = Teacher(person_name)            
            return build_object
        return -1
    
if __name__ == '__main__':
    # student1 = Student("rahul singh")
    # teacher1 = Teacher("ellis solaiman")
    # print(student1.person_method())
    # print(teacher1.person_method())
    person_type = input("Enter person type: ")
    person_name = input('Enter person name: ')

    build_object = PersonFactory.build_person(person_type, person_name)

    print(build_object.person_method())