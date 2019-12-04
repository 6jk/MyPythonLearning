def int2(x,base=2):
    return int(x,base)

print(int2('1010101'))

import functools
int3 = functools.partial(int,base=2)
print(int3('1010101'))

print(int3('1010101',base=10))

max2 = functools.partial(max,10)
print(max2(5,6,7))

#相当于
args = (10,5,6,7)
max(*args)