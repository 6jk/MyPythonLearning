import sys
import time

f = None

try:
    f = open('poem.txt')
    #我们常用的文件阅读风格
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line,end='')
        sys.stdout.flush()

        print('Press ctrl+c now')

        time.sleep(2)
except IOError:
    print('Could not find file poem.txt')
except KeyboardInterrupt:
    print('You cancelled the reading from the file')
finally:
    if f:
        f.close()
    print('Closed the file')


#with 语句
with open('poem.txt') as f:
    for line in f:
        print(line,end='')