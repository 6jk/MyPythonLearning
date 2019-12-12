class Student(object):
    def get_score(self):
        return self._score
    
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('Score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0 ~ 100')
        self._score = value

s = Student()
s.set_score(100)
# s.set_score(101)

class Teacher(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('Score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0 ~ 100')
        self._score = value
t = Teacher()
t.score = 60  #s.set_score
print(t.score)#s.get_score
t.score = 70
print(t.score)

# 还可以定义只读属性，只定义getter方法


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 
    def __iter__(self):
        return self # 迭代对象
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  
        if self.a > 100: 
            raise StopIteration() 
        return self.a 

for n in Fib():
    print(n)

class Fibx(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):
            a,b = 1,1
            L = []
            start = n.start
            stop = n.stop
            if start == None:
                start = 0
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b = b,a+b
            return L
f = Fibx()
print(f[0:5])
print(f[:10])            

print(list(range(100)[5:10]))