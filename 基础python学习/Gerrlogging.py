import logging
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print('END')




# class FooError(ValueError):
#     pass
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value:%s' %s)
#     return 10/n

# foo('0')


# 可以用断言（assert）来替代print()
# assert   n != 0 应该是true 否则后面会报错
# 启动python可以用-0 关闭assert    python -0 err.py


#--------------调试------------------------
# 1.print
# 2.assert
# 3.logging   好处：允许指定记录信息的级别debug，info，warning，error
# 4.pdb       一行行调试  太麻烦




# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' %n)
# print(10/n)




import pdb
s = '0'
n = int(s)
# pdb.set_trace()  #会自动暂停   输入p n 查看变量   c继续运行
print(10/n)



# 单元测试
# 可以有效测试某个模块的行为，是未来重构代码的信心保证
# 要覆盖常用的输入组合、边界条件和异常
# 代码要简单
# 通过不意味没bug，不通过肯定有bug
