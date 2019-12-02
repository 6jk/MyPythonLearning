#传递元组
def details():
    return(2,'detail')

a,b = details()
print('{0},{1}'.format(a,b))

#交换两变量
c = 2
d = 5
c,d = d,c
print('c={0},d={1}'.format(c,d))

#特殊方法
# __init__
# __del__(self)
# __str__(self)
# __lt__(self,other)
# __getitem__(self,key)
# __len__(self)

#Lambda表格
points = [{'x':2,'y':4},{'x':1,'y':5}]
points.sort(key = lambda i : i['x'])
print(points)

#列表推导
listone = [2,3,4]
listtwo = [2*i for i in listone if i>2]
print(listtwo)

#在函数中接收元组或字典
def powersum(power,*args):
    total = 0
    for i in args:
        total += pow(i,power)
    return total
print(powersum(2,3,3,4))#9+9+16

#assert语句:用于断言某事是真的
mylist = ['item']
assert len(mylist) >= 1 
mylist.pop()

assert len(mylist) >= 1

#装饰器