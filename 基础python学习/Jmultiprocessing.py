# import os
# print('Process (%s) start'%os.getpid())
# # only work Unix/Linux/Mac
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid
#   ()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 有了fork调用，一个进程接到新任务就可以复制一个子进程处理新任务


from multiprocessing import Process
import os
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.'%os.getpid())
    p = Process(target = run_proc,args = ('text',))
    print('Child process will start.')
    p.start()
    p.join()  # 用于进程间同步 可以等子进程结束后再往下进行
    print('Child process end.')