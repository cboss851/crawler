import time
import threading

def matter1(music):
    print("我想听这些歌")

    for i in range(0,len(music)):
        print(time.strftime('%Y-%m-%d %H:%M:%S'),"第" + str(i + 1) + "首歌是：" + str(music[i]))
        # 假设每一首歌曲的时间是2秒
        time.sleep(2)
        print("切换下一首歌...")

def matter2(number):
    print("我在打码")

    j = 0
    while j <= number:
        print(time.strftime('%Y-%m-%d %H:%M:%S',),"我准备写入第" + str(j + 1) +"行代码")
        j = j + 1
        # 假设每写一行代码的时间为1秒
        time.sleep(1)
        print("写下一行代码...")

if __name__ == '__main__':
    # 设定我要听的歌为
    music = ["music1","music2","music3"]

    # 设定我要打码的行数
    number = 5
    # 建立一个新数组
    threads = []
    # 将听歌放入数组里面
    thing1 = threading.Thread(target=matter1, args=(music,))
    threads.append(thing1)
    # 将打码放入数组里面
    thing2 = threading.Thread(target=matter2, args=(number,))
    threads.append(thing2)
    threadCount = 0
    while threadCount<10:
        thingW = threading.Thread(target=matter2, args=(number,))
        threads.append(thingW)
        threadCount = threadCount +1

    # 开始时间
    start = time.time()
    # 写个for让两件事情都进行
    for thing in threads:
        # setDaemon为主线程启动了线程matter1和matter2
        # 启动也就是相当于执行了这个for循环
        thing.setDaemon(True)
        thing.start()

    # 子线程没结束前主线程会被卡在这里
    thing1.join()
    thing2.join()
    # 结束时间
    end = time.time()
    print("完成的时间为：" + str(end - start))