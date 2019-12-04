def lazy_sum(*args): 
    def sum():
        ax = 0
        for n in args:
            ax = ax + n 
        return ax
    return sum
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)

# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
# f3,f4,f5 = count()
# print(f3(),f4(),f5())  #9,9,9

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f3,f4,f5 = count()
print(f3(),f4(),f5())  

l = list(map(lambda x: x*x,[1,2,3,4,5,6,7,8,9]))
print(l)


