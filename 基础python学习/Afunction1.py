#函数指可以重复使用的程序片段
def sayHello():
    print('hello')

sayHello()
sayHello()

#带参数
def printMax(x,y):
    if x == y:
        print('x isEqual to y')
    elif x < y:
        print(y,'is maximum')
    else:
        print(x,'is maximum')
printMax(2,6)

#局部变量
x = 1
def func(x):
    print('x is',x)
    x = 2
    print('change x to',x)
func(x)
print('x is',x)

#global 把变量赋值为全局变量（应该避免）

#默认参数值
def say(message,times = 2):
    print(message * times)
say('hello')
say('world',5)

#关键字参数 优点；1不需要考虑参数的顺序 2可以只对需要赋值的参数赋值，其他都有默认值
def keyword(a,b=3,c=5):
    print('a is',a,'b is',b,'and c is',c)
keyword(1,100)
keyword(26,c=50)
keyword(c=50,a=11)

#可变参数
def total(a=5,*numbers,**persons):
    print('a',a)
    for num in numbers:
        print('item ',num)
    for part1,part2 in persons.items():
        print(part1,part2)
print(total(10,1,2,3,zhang=3,li=4,wang=5))

#return语句用于函数中的返回，如果没搭配任何值返回None

#DocStrings
def print_max(x,y):
    '''打印两个数值中的最大数。
    
    这两个数都应该是整数'''
    x = int(x)
    y = int(y)

    if x>y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')
print_max(100,200)
print(print_max.__doc__)