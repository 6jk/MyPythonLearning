number = 25
running = True
guess = int(input('Enter an integer:'))
if number == guess:
    print('==')
elif number < guess:
    print('<')
else:
    print('>')
print('Done')

