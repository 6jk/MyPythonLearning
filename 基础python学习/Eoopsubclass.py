#继承
class SchoolMember:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('SchoolMember:{}'.format(self.name))
    
    def tell(self):
        #end能让print在末尾打印出\n
        print('name:"{}" age:"{}"'.format(self.name,self.age),end = ' ')
    
class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('Teacher:{}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{:d}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print('Student:{}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('marks:"{:d}"'.format(self.marks))

t = Teacher('Mrs.Li',25,5000)
s = Student('Armiky',17,70)

print()

members = [t,s]
for member in members:
    member.tell()