#模块 在别的程序中重用一些函数
import sys
print('------:')
for i in sys.argv:
    print(i)
print('\n\n The PYTHONPATH is ',sys.path,'\n')

#from...import...语句，应尽量避免，会出现名称冲突
from math import sqrt
print(sqrt(16))

#__name__
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

def say_hi():
    print('hi')
__version__ = '0.1'