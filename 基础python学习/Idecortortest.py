# import functools
# def log(text):
#     if isinstance(text,str):
#         def decorator(func):
#             @functools.wraps(func)
#             def wrapper1(*args,**kw):
#                 print('begin call')
#                 func(text)
#                 print('end call')
#                 return func(*args,**kw)
#             return wrapper1
#         return decorator
#     else:
#     #    @functools.wraps(func)
#         def wrapper2(*args,**kw):
#             # print('begin call')
#             # func(*args,**kw) 
#             print('end call')

# @log
# def f1(text):
#     print(f1.__name__,text)

# @log('execute')
# def f2(text):
#     print(f2.__name__,text)

# f1(22)
# f2(11)






# import functools
# def call(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print('begin call')
#         func(*args,**kw)
#         print('end all')
#     return wrapper

# def log(funcortext):
#     def dec1(func):#传入文本
#         def wrapper(*args,**kw):
#             print("传入文本时:"+funcortext,func.__name__)
#         return wrapper
#     def dec2(*args,**kw):#传入函数
#         print("传入函数时:"+funcortext.__name__)
#     dec=dec1 if isinstance(funcortext, str) else dec2
#     return dec

# @log
# def now1():
#     print('2019-12-3')
# now1()

# @log('execute')
# def now2():
#     print('2019-12-3')
# now2()