#序列
shoplist = ['apple','mango','carrot','banana']
name = 'lujunkai'
print('0--',shoplist[0])
print('-1--',shoplist[-1])
print('-2--',shoplist[-2])

print('Character 0 is',name[0])

print('Item 1 to 3 is',shoplist[1:3])
print('Item 1 to end is',shoplist[1:])
print('Item 1 to -1 is',shoplist[1:-1])
print('Item start to end is',shoplist[:])

print('Characters 1 to 3 is',name[1:3])
print('Characters 1 to end is',name[1:])
print('Characters 1 to -1 is',name[1:-1])
print('Characters start to end is',name[:])

#序列提供第三个参数，视为切片步长（step），默认为1

#集合
bri = set(['zhangsan','lisi','wangwu'])
print('zhangsan' in bri)

bric = bri.copy()
bric.add('ljk')
print(bric.issuperset(bri))

bri.remove('lisi')
print(bri & bric)


str1 = 'I love you.'
str2 = str1.replace(' ','')
str2 = str2.replace('.','')
print(str2)

#判断一个对象是否可迭代
from collections import Iterable
print(isinstance('abc',Iterable))

#enumerate 可以把一个list变成索引-元素对
for i,value in enumerate(['A','B','C']):
    print(i,value)

for x,y in [(1,1),(2,2),(3,3)]:
    print(x,y)

# 生成[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10)))

L = []
for x in range(1,10):
    L.append(x*x)
print(L)

print('---',[x*x for x in range(1,10)])

print([m + n for m in 'ABC' for n in 'XYZ'])

#先去掉非字符串，字符串变小写
List = ['Hello','World',18,'Lu Junkai',[1,2]]
print([s.lower() for s in List if isinstance(s,str)])