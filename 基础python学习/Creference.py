#引用
shoplist = ['apple','banana','catfood','duck']
mylist = shoplist
shelist = shoplist.copy()

del shoplist[0]
print(mylist)#同一个对象
print(shelist)

del mylist[0]
print(shoplist)

#通过生成完整切片制作一份列表副本
mylist = shoplist[:]
del mylist[0]
print('shoplist is',shoplist)
print('mylist is',mylist)

# help(str)

#字符串更多内容
name = 'lujunkai'
print(name.startswith('lu'))
print('a' in name)
print(name.find('jun'))
print(name.find('ren'))

delimiter = '_*_'
print(delimiter.join(shoplist))