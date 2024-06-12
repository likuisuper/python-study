# 匿名函数
from functools import reduce

if __name__ == '__main__':
    # lambda表达式
    square = lambda x: x ** 2
    print(square(2))

    # 列表内部使用
    l = [(lambda x: x ** 2)(x) for x in range(10)]
    print(l)

    # 用作函数参数
    l = [(1, 20), (3, 0), (9, 10), (2, -1)]
    l.sort(key=lambda x: x[1])
    print(l)

    # 让程序简洁
    squares = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
    print(list(squares))

    # 函数式编程，将列表元素增加
    # 函数式编程，即函数

    # filter函数
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    new_list = filter(lambda x: x % 2 == 0, l)
    print(list(new_list))

    # reduce计算阶乘
    from functools import reduce

    product = reduce(lambda x, y: x * y, l)
    print(product)
