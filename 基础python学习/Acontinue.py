running = True
while running:
    s = input('Enter someThing:')
    if len(s) == 3:
        break
    elif len(s) < 3:
        print('太小')
        continue
    else:
        running = False
        print('qqqqqq')
else:
    print('The while is over')
print('Done')

        