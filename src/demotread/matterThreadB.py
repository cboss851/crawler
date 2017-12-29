import time
import threading
import urllib.parse
import urllib.request

def withdrawTest(name):
    print("我在打码")
    number = 5
    j = 0
    while j <= number:
        print(name,time.strftime('%Y-%m-%d %H:%M:%S',),"我准备写入第" + str(j + 1) +"行代码")
        j = j + 1
        # 假设每写一行代码的时间为1秒
        time.sleep(1)
        print("写下一行代码...")

def withdrawHttp(name):
    print(name,time.strftime('%Y-%m-%d %H:%M:%S',),"开始1")
    #url = 'http://www.baidu.com'
    url = 'http://172.31.20.233:6260/api/notice/send'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }

    request = urllib.request.Request(url, headers=header)
    print(name,time.strftime('%Y-%m-%d %H:%M:%S',),"开始2")
    reponse = urllib.request.urlopen(request).read()
    print(name,time.strftime('%Y-%m-%d %H:%M:%S',),"开始3")
    # print(reponse)

    fhandle = open("./file/finscore"+str(name)+".html", "wb")
    fhandle.write(reponse)
    fhandle.close()
    print(name,time.strftime('%Y-%m-%d %H:%M:%S',),"开始end")

def withdrawHttpLBJ(name):
    print(name,time.strftime('%Y-%m-%d %H:%M:%S',),"开始1")
    #url = 'http://www.baidu.com'
    url = 'http://www.sanjiaojihe.com/app/index.php?i=2&c=entry&mid=22703&do=member&m=sz_yi&p=withdraw&'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.691.400 QQBrowser/9.0.2524.400',
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With':'XMLHttpRequest',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4',
        'Referer':'http://www.sanjiaojihe.com/app/index.php?i=2&c=entry&p=withdraw&type_supp=s&mid=22703&do=member&m=sz_yi',
        'Cookie':'PHPSESSID=1b6c632e64678d04675fa2a0a7240084; PHPSESSID=1b6c632e64678d04675fa2a0a7240084'
    }

    request = urllib.request.Request(url, headers=header)
    print(name,time.strftime('%Y-%m-%d %H:%M:%S',),"开始2")
    reponse = urllib.request.urlopen(request).read()
    print(name,time.strftime('%Y-%m-%d %H:%M:%S',),"开始3")
    # print(reponse)

    fhandle = open("./file/lbj"+str(name)+".html", "wb")
    fhandle.write(reponse)
    fhandle.close()
    print(name,time.strftime('%Y-%m-%d %H:%M:%S',),"开始end")

def withdrawHttpLBJTx(name):
    print(name,time.strftime('%Y-%m-%d %H:%M:%S',),"开始1")
    url = 'http://www.sanjiaojihe.com/app/index.php?i=2&c=entry&mid=22703&do=member&m=sz_yi&p=withdraw'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.691.400 QQBrowser/9.0.2524.400',
        'Origin':'http://www.sanjiaojihe.com',
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With':'XMLHttpRequest',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4',
        'Referer':'http://www.sanjiaojihe.com/app/index.php?i=2&c=entry&p=withdraw&type_supp=s&mid=22703&do=member&m=sz_yi',
        'Cookie':'PHPSESSID=1b6c632e64678d04675fa2a0a7240084; PHPSESSID=1b6c632e64678d04675fa2a0a7240084'
    }
    data={
        'op':'submit',
        'money':'2'
    }
    postdata=urllib.parse.urlencode(data).encode('utf8')

    request = urllib.request.Request(url, postdata , headers=header)
    print(name,time.strftime('%Y-%m-%d %H:%M:%S',),"开始2")
    reponse = urllib.request.urlopen(request).read()
    print(name,time.strftime('%Y-%m-%d %H:%M:%S',),"开始3")
    # print(reponse)

    fhandle = open("./file/lbj"+str(name)+".html", "wb")
    fhandle.write(reponse)
    fhandle.close()
    print(name,time.strftime('%Y-%m-%d %H:%M:%S',),"开始end")

if __name__ == '__main__':
    # 建立一个新数组
    threads = []
    threadCount = 0
    while threadCount<1:
        thingW = threading.Thread(target=withdrawHttpLBJTx, args=(threadCount,))
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
    time.sleep(10)
    # 结束时间
    end = time.time()
    print("完成的时间为1：" + str(end - start))
    time.sleep(100000)
    print("完成的时间为2：" + str(end - start))
