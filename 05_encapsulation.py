class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property # With this decorator, the following function can be used like a variable or property.
    def fullname(self):
        return self.first.capitalize() + ' ' + self.last.capitalize()
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print("Full name deleted!")
    
    @property # With this decorator, the following function can be used like a variable or property.
    def generate_email(self):
        return self.first.capitalize() + '.' + self.last.capitalize() + '@gmail.com'
    
e1 = Employee('rahul', 'singh')
print(e1.fullname)
print(e1.generate_email)

e1.first = 'ruirui'
print()
print(e1.fullname)
print(e1.generate_email)

e1.fullname = 'udit jayant'
print()
print(e1.fullname)
print(e1.generate_email)

del e1.fullname
