class Robot:
    '''表示一个带有名字的机器人'''
    population = 0

    def __init__(self,name):
        self.name = name 
        print('(init {})'.format(self.name))
        Robot.population += 1
    
    def die(self):
        print('{} is being destroyed!'.format(self.name))

        Robot.population -= 1
        # self.__class__.population
        if Robot.population == 0:
            print('{} was the last'.format(self.name))
        else:
            print('There are still {:d} Robots working'.format(Robot.population))
    
    def say_hi(self):
        """Hi"""
        print('Greetings,my masters call me {}'.format(self.name))
    
    @classmethod
    def how_many(cls):
             '''打印出当前人口数量'''
             print('We have {:d} robots.'.format(cls.population))

droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C-3PO')
droid2.say_hi()
Robot.how_many()

droid1.die()
droid2.die()

Robot.how_many()


print(Robot.__doc__)
print(Robot.say_hi.__doc__)

# 任何在类或对象之中使用的变量其命名应以下划线开头，其它所有非此格式的名称都将是公开的，\
# 并可以为其它任何类或对象所使用。

