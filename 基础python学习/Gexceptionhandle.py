#处理异常
try:
    text = input('Enter something -->')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))

class ShortInputException(Exception):
    '''一个由用户定义的异常类'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something -->')
    if len(text)<3:
        raise ShortInputException(len(text),3)
except EOFError:
    print('Why did you do an EOF on me')
except ShortInputException as ex:
    print('{0} long,expected at least {1}'.format(ex.length,ex.atleast))
else:
    print('No exception was raised')