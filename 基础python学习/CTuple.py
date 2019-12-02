#元组（括号隐式）
zoo = ('python','elephont','cat')
print(len(zoo))

new_zoo = 'monkey','bird','lion',zoo
print(len(new_zoo))

print('new_zoo:',new_zoo)
print(new_zoo[3],new_zoo[3][2])

print(zoo+new_zoo)

zoo = zoo*3
print(zoo)
