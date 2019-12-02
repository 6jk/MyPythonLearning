class Person:
    def say_hi(self):
        print('Hi,my name is',self.name)
    
    def __init__(self,name):
        self.name = name

p = Person('Ljk')
p.say_hi()