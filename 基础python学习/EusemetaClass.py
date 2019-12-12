# 元类  type()

class Hello(object):
    def hello(self,name = 'world'):
        print('hello, %s.'%name)

h = Hello()
print(h.hello())
print(type(Hello))
print(type(h))


def fn(self,name = 'world'):
    print('Hello,%s.'%name)
Hi = type('Hi',(object,),dict(hello=fn))
hi = Hi()
print(hi.hello())
print(type(Hi))
print(type(hi))