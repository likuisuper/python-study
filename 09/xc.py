# 协程
import asyncio
import time

if __name__ == '__main__':
    # 普通爬虫
    def crawl_page(url):
        print("正在爬取 {}".format(url))
        # 爬取时间取决于url后面的数字
        sleep_time=int(url.split("_")[-1])
        time.sleep(sleep_time)
        print("ok {}".format(url))

    def main(urls):
        for url in urls:
            crawl_page(url)


    start = time.perf_counter()
    #main(['url_1','url_2','url_3','url_4'])
    print("普通耗时:{}秒".format(time.perf_counter()-start))


    # 使用协程并发爬虫，因为在for循环中使用了await，所以这其实是一个使用异步接口写的同步代码
    async def crawl_page2(url):
        print("正在爬取 {}".format(url))
        # 爬取时间取决于url后面的数字
        sleep_time=int(url.split("_")[-1])
        await asyncio.sleep(sleep_time)
        print("ok {}".format(url))

    async def main2(urls):
        for url in urls:
            # await 主程序会阻塞在这里，进入被调用的协程函数，执行完毕后再继续，后面需要跟async函数，否则报错
            await crawl_page2(url)

    # 会提示这是一个协程对象，而不会真正执行这个函数
    # print(crawl_page2('url_3'))
    start = time.perf_counter()
    #main2(['url_1','url_2','url_3','url_4'])
    # async函数需要通过run来执行
    #asyncio.run(main2(['url_1','url_2','url_3','url_4']))
    print("并发爬虫:{}秒".format(time.perf_counter()-start))


    # 真正的并发爬虫
    async def crawl_page3(url):
        print("正在爬取 {}".format(url))
        # 爬取时间取决于url后面的数字
        sleep_time=int(url.split("_")[-1])
        await asyncio.sleep(sleep_time)
        print("ok {}".format(url))

    async def main3(urls):
        tasks=[
            # 创建任务
            asyncio.create_task(crawl_page3(url)) for url in urls
        ]
        # for task in tasks:
        #     # 等待所有任务都结束，不然任务睡眠后的代码不会执行。
        #     await task
        # 上面的tasks可以直接通过gather执行，需要注意这里的tasks要解包，即将列表变成函数参数
        await asyncio.gather(*tasks)

    start = time.perf_counter()
    asyncio.run(main3(['url_1','url_2','url_3','url_4']))
    # 运行总时长等于运行时间最长的任务
    print("真正的并发爬虫，耗时:{}".format(time.perf_counter()-start))