class Student:
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname
        self.fullname= name + '_kumar_' + lastname

std1=Student("garv","mehra")
print(std1.fullname)
