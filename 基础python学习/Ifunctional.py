#打印1000内素数
def _odd_iter():
    n = 1
    while True:
        n = n + 1 
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

for i in primes():
    if i < 100:
        print(i)
    else:
        break


print(sorted([12,-12,5,26,-49,-1]))
print(sorted([12,-12,5,26,-49,-1],key=abs))#先转换绝对值排序

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse=True))#反向排序，忽略大小写