# 定义类时传入的参数是该类所要继承的父类
# object是所有类的原始父类，在没有合适的继承父类时，用object
class Animal(object):
    # 类初始器函数的第一个变量永远是self
    def __init__(self, name, sex, *key):
        self.name = name
        self.sex = sex
        # age is a private var
        # private var use _ as prefix
        self._age = key[0]

    # 将对象抽象为类，将对象的数据抽象为类中方法的过程，称为数据封装
    def wink(self):
        wink_action = "{0} is winking".format(self.name)
        return wink_action

    def get_age(self):
        return self._age

if __name__ == '__main__':
    dudu_dog = Animal("DuDU", "male", 7)
    print("The animal is {0}, it's sex is {1}".format(dudu_dog.name, dudu_dog.sex))
    print(dudu_dog.wink())
    print("It's age is {0}".format(dudu_dog.get_age()))
