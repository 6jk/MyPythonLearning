class Student:
    pass

s = Student()
s.name = 'lunderfoot'
print(s.name)


#给实例绑定一个方法
def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(26)
print(s.age)

s2 = Student()
# s2.set_age(26)

def set_score(self,score):
    self.score = score

# 给class绑定方法后所有实例都可以使用
Student.set_score = set_score
s.set_score(100)
s2.set_score(99)
print(s.score,s2.score)


class Teacher():
    __slots__ = ('a','b')  # 只允许添加a和b属性，仅对当前类实例起作用，对继承的子类不起作用，
                           # 除非在子类也定义，子类运行定义的属性就是自身加父类的__slots__

t = Teacher()
t.a = 100
t.b = 200
t.c = 300