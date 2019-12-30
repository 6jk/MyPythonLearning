import time,sys,queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManageer
class QueueManager(BaseManager):
    pass

# 由于这个Queuemanager只从网络上获取Queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_manager.py的机器
server_addr = '223.64.140.201'
print('Connent to server %s...'%server_addr)

# 端口和验证码注意保持也task_master.py设置的完全一致
m = QueueManager(address=(server_addr,5000),authkey=b'abc')
# 从网络连接
m.connect()
# 获取Queue的对象
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务，并把结果写入result队列
for i in range():
    try:
        n = task.get(timeout=1)
        print('run task %d*%d...'%(n,n))
        r = '%d*%d = %d'%(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
print('worker exit.')