#装饰器：在函数调用前后自动打印日志，不修改函数定义
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw) 
#     return wrapper

# @log
# def now():
#     print('2019-12-2')
# print(now())

# import functools
# def log(text):
#     def decorator(func):
#         @functools.wraps(func) #now.__name__可以打印now，不然会打印wrapper
#         def wrapper(*args,**kw):
#             print('%s %s():'%(text,func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator

# @log('execute')
# def now():
#     print('2019-12-3')
# print(now.__name__)
# print(now())

# now = log('execute')(now)
# print(now.__name__)
# print(now)


#打印函数执行时间
import time,functools
def metric(fn):
    def wrapper(*args,**kw):
        start = time.time()
        fn(*args,**kw)
        end = time.time()
        print('%s executed in %s ms'%(fn.__name__,end-start))
        return fn(*args,**kw)
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')