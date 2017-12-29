#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import time

def matter1(music):
    print("我想听这些歌")

    for i in range(0,len(music)):
        print("第" + str(i + 1) + "首歌是：" + str(music[i]))
        # 当前时间为
        print(time.strftime('%Y%H%M%S', time.localtime()))
        # 假设每一首歌曲的时间是2秒
        time.sleep(2)
        print("切换下一首歌...")

def matter2(number):
    print("我在打码")

    j = 0
    while j <= number:
        print("我准备写入第" + str(j + 1) +"行代码")
        j = j + 1
        # 当前时间为
        print(time.strftime('%Y%H%M%S', time.localtime()))
        # 假设每写一行代码的时间为1秒
        time.sleep(1)
        print("写下一行代码...")

if __name__ == '__main__':

    start = time.time()

    # 设定我要听的歌为
    music = ["music1","music2","music3"]
    # 开始听歌
    matter1(music)
    # 设定我要打码的行数
    number = 5
    # 开始打码
    matter2(number)

    end = time.time()
    print("完成的时间为：" + str(end - start))