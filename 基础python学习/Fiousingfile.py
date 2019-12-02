poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# w写入模式  r阅读模式  a追加模式  t文本模式 b二进制模式
# help(open)
# 默认文件视作文本文件，阅读模式打开
f = open('poem.txt','w')

f.write(poem)

f.close()

f = open('poem.txt')
while True:
    line = f.readline()

    if len(line) == 0:
        break
    print(line,end = '')

f.close()