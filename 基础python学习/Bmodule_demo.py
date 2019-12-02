import Bmodule_using_sys

Bmodule_using_sys.say_hi()
print('version',Bmodule_using_sys.__version__)

#不推荐
from Bmodule_using_sys import say_hi,__version__
print('version   ',__version__)
say_hi()

#from...import...不会导入__version__  （双下滑）

# import this
#美丽总比丑陋好。
#显式的比隐式的好。
#简单总比复杂好。
#复杂总比复杂好。
#平铺总比嵌套好。
#稀疏总比稠密好。

#函数是程序中可重用的部分，模块是种可重用的程序，包是用于组织模块的另一种层次结构