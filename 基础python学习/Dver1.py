import os
import time
source = ['/Users/swa/notes']

target_dir = '/Users/swa/backup'

# os.sep:它将根据你的操作系统给出相应的分隔符，在 GNU/Linux 与 Unix 中它\
# 会是 '/'，在 Windows 中它会是 '\\'，在 Mac OS 中它会是 ':'。使用 os.sep 而非直\
# 接使用这些字符有助于使我们的程序变得可移植，从而可以在上述这些系统中都能正常工作。
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip -r {0} {1}'.format(target,''.join(source))

print('Zip command is:')
print(zip_command)
print('running:')
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')