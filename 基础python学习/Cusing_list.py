#列表
shoplist = ['apple','mango','banana','orange']
shoplist.insert(1,'melo')
shoplist.pop(1)
print('I have',len(shoplist),'items')

print('These items are:',end='')

for item in shoplist:
    print(',',item,end='')

print('\nhave rise')

shoplist.append('rise')
print(shoplist)
print(shoplist[0])

shoplist.sort()
print('sort list is',shoplist)

str1 = '苹果,橘子,香蕉'
#分割字符串
result = str1.split(',')
print(result)

my_url = 'http://www.baidu.com'
result2 = my_url.startswith('http')
result3 = my_url.endswith('.com')
print(result2,result3)

my_str = 'aaabbbccc'
result4 = my_str.partition('bbb')

result5 = '-'.join('abc')
print(result4,result5)

#去除空格
str2 = ' hello '
result6 = str2.strip()#左右，不传参数默认去空格
result7 = str2.lstrip()
result8 = str2.rstrip()
print(result6)
print(result7)
print(result8)

#列表可以放任何数据类型
#从0开始，负数下标从-1开始