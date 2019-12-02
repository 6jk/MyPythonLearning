age = 20
name = 'Ljk'

print('{0} was {1} years old'.format(name,age))
print('Why is {0} playing with that python'.format(name))

print('a', end="")
print('b', end="")
print('c')

#r表示内部字符串默认不转义
print(r"Newlines are indicated by \n")

print(2**3)        #2的3次方
print(-25.5%2.25)  #1.5
print(-20%6)       #4           X - X//Y*Y

# &按位与   |按位或  ^按位异或（0101^0011 = 6） ~按位取反(结果为-(x+1))

x = True 
y = False
print(not x)   #False
print(x and y) #False
print(x or y)  #True

length = 5
breadth = 2
area = length * breadth
print('Area is',area)
