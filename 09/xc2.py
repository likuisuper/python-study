# 解密协程运行时
# Async是单线程的，它只有一个主线程，但是可以进行多个不同的任务，就是特殊的future对象，也可以类比多线程中的多个线程
# 这些不同的任务被一个叫做event loop的对象所控制
# 也就是说，其内部的event loop机制，可以让它并发地运行多个不同的任务


import asyncio


async def worker_1():
    print("worker_1 start")
    await asyncio.sleep(1)
    print("worker_1 done")

async def worker_2():
    print("worker_2 start")
    await asyncio.sleep(1)
    print("worker_2 done")

async def main():
    print("before await")
    await worker_1()
    print("awaiter worker_1")
    await worker_2()
    print("awaiter worker_2")

#-------------------------------

async def worker1():
    print("worker1 start")
    await asyncio.sleep(1)
    print("worker1 done")

async def worker2():
    print("worker2 start")
    await asyncio.sleep(1)
    print("worker2 done")

async def main2():
    task1=asyncio.create_task(worker1())
    task2=asyncio.create_task(worker2())
    print("before await")
    # 等待task1执行完，期间也会执行task2
    await task1
    print("awaited worker1")
    await task2
    print("awaited worker2")

if __name__ == '__main__':
    # run就是拿到event loop，运行输入的coro，直到它结束，然后关闭这个event loop
    #asyncio.run(main())
    asyncio.run(main2())
