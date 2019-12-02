import pickle
import io
shoplistfile = 'shoplist.data'

shoplist = ['apple','banana','carrot']

# wb 写入二进制（binary）模式
f = open(shoplistfile,'wb')

#转存对象至文件（封装）
pickle.dump(shoplist,f)
f.close()

del shoplist

f = open(shoplistfile,'rb')
#从文件中载入对象（拆封）
shoredlist = pickle.load(f)
print(shoredlist)


g = io.open('abc.txt','wt',encoding='utf-8')
g.write(u'Imagine non-English language here')
g.close()

text = io.open('abc.txt',encoding='utf-8').read()
print(text)