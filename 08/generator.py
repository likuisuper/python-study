# 生成器


def fab(max):
    """
    yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，
    调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，
    执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，
    而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。
    如果不使用yield，我们想要返回这个数列集合，肯定是将b放入list，但是这样当max增大时，占用的内存也会增大
    :param max:
    :return:
    """
    n,a,b=0,0,1
    while n<max:
        # 直接返回b，所以下面的print不会输出，第二次迭代的时候从yield下面的语句开始，输出print
        yield b
        print("hhhh")
        a,b=b,a+b
        n+=1

for n in fab(5):
    print(n)

# 需要注意，fab函数此时返回的是一个对象，需要使用list转换为列表
# f=fab(5)
# print(list(f))