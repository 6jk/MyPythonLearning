class Person(object):
    def say_hi(self):
        print('Hi,my name is',self.name)
    
    def __init__(self,name):
        self.name = name

p = Person('Ljk')
p.say_hi()


# 获取对象信息
import types
def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(1,10)) == types.GeneratorType)
print(type('abc') == str)

# isinstance
# dir() 获得一个对象所有属性

print('-',hasattr(p,'name'))
print('-',hasattr(p,'x'))
setattr(p,'x',26)
print('--',hasattr(p,'x'))
print('--',p.x)
print('--',getattr(p,'x'))
print('---',getattr(p,'y',404))  #如果没有默认404

print(hasattr(p,'say_hi'))
print(getattr(p,'say_hi'))
fn = getattr(p,'say_hi')
fn()


#实例属性属于各个实例所有，互不干扰
#类属性属于类所有，所有实例共享一个属性


#    定制类
class Student(object):
    def __init__(self):
        self.name = 'lunderfoot'

    # 动态返回一个属性
    def __getattr__(self,attr):
        if attr == 'score':
            return 60
        if attr == 'age':
            return lambda : 26
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s = Student()

print(s.score)
print(s.age())#返回函数
# print(s.abc)


class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __getatter__(self,path):
        return Chain('%s/%s'%(self._path,path))
    def __str__(self):
        return self._path
    __repr__ = __str__   # 返回开发者看到的字符串，为调试服务,终端还是显示__str__的

    def __call__(self):
        print('123414')


# print(Chain().status.user.timeline)  不懂
# 无论api怎么变，sdk都可以根据url实现完全动弹调用，不随着api增加而改变

c = Chain()
print(c())  #不用传参数


# callable(None) 判断是否可调用对象