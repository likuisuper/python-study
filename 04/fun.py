# 自定义函数

# 调用另一个函数
def fun(message):
    my_func(message)


def my_func(message):
    print("收到一个消息:{}".format(message))


if __name__ == '__main__':
    my_func("hello word")


    # 函数嵌套
    def my_sum(a, b):
        return a + b;


    print(my_sum(3, 4))


    # 获取列表最大元素
    def find_largest_element(l):
        if not isinstance(l, list):
            print("输入数不是列表")
        if len(l) == 0:
            print("列表为空")
            return
        largest_element = l[0]
        for item in l:
            if item > largest_element:
                largest_element = item
        print("列表中最大元素为:{}".format(largest_element))


    find_largest_element([3, -5, 6, 8, 2, 1])

    fun("你好,python")

    # 参数多态性
    print(my_sum([1, 2], [3, 4]))  # 如果是列表的话，会进行拼接

    try:
        my_sum(5, "7")
    except Exception as error:
        print("发生错误!{}".format(error))


    # 函数嵌套提高效率
    def factorial(input):
        # 输入检查，只运行一次
        if not isinstance(input, int):
            raise Exception("必须输入整数")
        if input < 0:
            raise Exception("输入必须大于等于0")

        # 实际计算
        def inner_factorial(input):
            if input <= 1:
                return 1
            return input * inner_factorial(input - 1)

        return (inner_factorial(input))


    try:
        print(factorial(3))
    except Exception as error:
        print(error)

    # 函数中改变外部变量
    value = 2
    overvalue = 3


    def changeValue():
        # global声明全局变量
        global value
        # 修改全局变量
        value += 1
        overvalue = 6
        print(value, overvalue)  # 3,6


    changeValue()
    print(value)  # 3
    print(overvalue)  # 3

    # 嵌套函数内部修改
    # 加nonlocal
    print("加nonlocal")


    def outer():
        x = 3

        def inner():
            nonlocal x
            x = 5
            print("内部", x)  # 5

        print("外部", x)  # 3
        inner()
        print("外部", x)  # 5


    outer()
    # 不加
    print("不加")


    def outer2():
        x = 3

        def inner2():
            x = 5
            print("内部", x)  # 5

        print("外部", x)  # 3
        inner2()
        print("外部", x)  # 3


    outer2()


    # 闭包
    def nth_power(exp):
        def exponent_of(base):
            return base ** exp

        # 返回值是exponent_of函数
        return exponent_of


    # 第一次调用传递外层函数参数
    square = nth_power(2)
    cube = nth_power(3)

    # 后续调用直接调用变量，只需要传递内层函数所需要的变量
    print(square(3))
    print(cube(3))
