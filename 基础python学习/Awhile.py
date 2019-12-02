number = 25
running = True
while running:
    inputNum = int(input('Enter an integer:'))
    if inputNum == number:
        print('=')
        running = False
    elif inputNum < number:
        print('lower')
    else:
        print('higher')
else:
    print('The while is over.')
print('Done')

for i in range(1,8,3):
    print(i)
else:
    print('done')  

# break 终端for、while循环