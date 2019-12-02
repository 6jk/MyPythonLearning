#如何创建我们自己的 Python 程序与脚本
import os
import time
source = ['/Users/swa/notes']

target_dir = '/Users/swa/back'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('enter a comment -->')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +\
        comment.replace(' ','_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
print('Successfully created',today)

zip_command = 'zip -r {0} {1}'.format(target,''.join(source))

print('Zip command is:')
print(zip_command)
print('running:')
#如果成功返回0
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')

# 软件开发流程
# What/做什么（分析）
# How/怎么做（设计）
# Do It/开始做（执行）
# Test/测试（测试与修复错误）
# Use/使用（操作或开发）
# Maintain/维护（改进）
# 程序是成长起来的，不是搭建出来的