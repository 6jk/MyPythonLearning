class Robot:
    '''表示一个带有名字的机器人'''
    population = 0

    def __init__(self,name):
        self.__name = name 
        print('(init {})'.format(self.__name))
        Robot.population += 1
    
    def die(self):
        print('{} is being destroyed!'.format(self.__name))

        Robot.population -= 1
        # self.__class__.population
        if Robot.population == 0:
            print('{} was the last'.format(self.__name))
        else:
            print('There are still {:d} Robots working'.format(Robot.population))
    
    def say_hi(self):
        """Hi"""
        print('Greetings,my masters call me {}'.format(self.__name))
    
    @classmethod
    def how_many(cls):
             '''打印出当前人口数量'''
             print('We have {:d} robots.'.format(cls.population))

droid1 = Robot('R2-D2')
print(droid1._Robot__name)#内部变量仍可以访问   _name:可以访问，但视为私有变量，不要随意访问  
#__name__：特殊变量
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


#直接.score也可以修改，方法中可以对参数做检查，避免传入无效参数
# class Student(object): 
#     ...
#     def set_score(self, score): 
#         if 0 <= score <= 100:
#             self.__score = score 
#         else:
#             raise ValueError('bad')