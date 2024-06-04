# 列表和元组

if __name__ == '__main__':
    l = [1, 2, "hello", "world"]
    tup = ("jason", 22)
    print(l)
    print(tup)

    # 增加元素
    new_tup = tup + (5,)
    print(new_tup)
    l.append(5)
    print(l)

    # 片切操作
    l1 = [1, 2, 3, 4]
    print(l1[1:3])
    tup1 = ((1, 2, 3), (4, 5, 6))
    print(l1)
    print(tup1)

    # 嵌套
    l2 = [[1, 2, 3], [4, 5]]
    tup2 = ((1, 2, 3), (4, 5, 6))
    print(l2)
    print(tup2)

    # 相互转换，元组转换为列表，列表转换为元组
    print(list((1, 2, 3)))
    print(tuple([1, 2, 3]))

    # 内置函数
    l3 = [3, 2, 3, 1, 5]
    # 3出现的次数
    print(l3.count(3))
    print(l3.index(1))
    # 反转
    l3.reverse()
    print(l3)
    # 默认升序
    l3.sort()
    print(l3)
    tup3 = (3, 2, 3, 7, 8, 1)
    print(tup3.count(3))
    print(tup3.index(7))
    print(list(reversed(tup3)))
    print(sorted(tup3))

    # 列表和元组的存储差异
    l4 = [1, 2, 3]
    tup4 = (1, 2, 3)
    # sizeof返回对象在内存中占用的字节大小，只计算对象本身的内存占用，结果可以发现列表占用的字节大小比元组要大
    print(l4.__sizeof__())
    print(tup4.__sizeof__())
