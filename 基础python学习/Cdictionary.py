ab = {
    'zhangsan':'25',
    'lisi':'26',
    'wangwu':27,
    '猪八':28
}
print(ab['猪八'])

del ab['lisi']
print('There are {}'.format(len(ab)))

for name,address in ab.items():
    print('Contant {} at {}'.format(name,address))

ab['lujunkai'] = 26