# 异常处理：如何提高程序的稳定性

# 自定义异常类
class MyInputError(Exception):
    # self参数是对当前类实例的引用，用于访问属于该类的变量，它可以不叫self，但它必须在函数的第一个参数
    # init类似java中的构造函数，该函数总是在类启动时执行
    def __init__(self, value):
        self.value = value

    def __str__(self):
        # 类似于java中的toString
        # repr用于生成对象的官方字符串表示形式
        return ("{} is invalid input".format(repr(self.value)))


if __name__ == '__main__':
    # try except语句
    # try:
    #     s = input("输入数字，以,分隔:")
    #     num1 = int(s.split(",")[0].strip())
    #     num2 = int(s.split(",")[1].strip())
    # except ValueError as err:
    #     print("值错误:{}".format(err))
    # except Exception as err:
    #     print("其它异常:{}".format(err))
    # print("继续")

    # 自定义异常
    try:
        # raise类似与java中的throw，即抛出异常
        raise MyInputError(1)
    except MyInputError as err:
        print("error:{}".format(err))
    print("继续2")
