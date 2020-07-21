# 一个简单的函数
def say_hello():
    print("Please input: ")
    word = input()
    if len(word) > 0:
        print("Say {0}".format(word))
    else:
        print("input something")

# 函数可以返回多个值
def fun_return_more(x, y, z):
    return x, y, z


# 定义可变参数，可变参数使用*前缀，功能是可以传入0个或任意个函数变量
def fun_alterable(*numbers):
    for i in numbers:
            print("Numbers has: {0}".format(i))

# 定义关键词参数，用**前缀，可传入任意名字的关键词以及值，python用dict形式包装
def fun_mutiple_variable(name, age, **anyekeyword):
    print("Name: {0}, age: {1}, {2}".format(name, int(age), anyekeyword))

# 递归函数
def fun_recursion(n):
    if n == 1:
        return n
    else:
        return n * fun_recursion(n-1)



if __name__ == '__main__':
    # say_hello()
    # for element in fun_return_more(1, 2, 3):
    #     print(element)
    ## 可以传入任意多个参数，参数组成了一个tuple，因此函数本身也是接收不可变对象
    # fun_alterable(5, 7 ,8 ,9)
    ## 在穿衣任意多个参数的基础上，可以给参数加上key值，其自动组成一个dict
    # fun_mutiple_variable("Tom", 21, City="BJ", Dog="DuDu", Cat = "LULU")
    ## 使用递归的方式计算阶乘n!
    print(fun_recursion(3))