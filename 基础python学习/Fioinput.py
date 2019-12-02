#用户输入内容
def reverse(text):
    #第三个参数为步长，默认为1，-1表示翻转文本
    return text[::-1]

def is_palindrone(text):
    return text == reverse(text)

something = input('Enter text:')
if is_palindrone(something):
    print('Yes,it is a palindrone')
else:
    print('No,it is not a palindrone')
