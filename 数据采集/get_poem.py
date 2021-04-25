import requests
import re
import threading
import time
import random
from collections import defaultdict

# 代理网站：https://www.xicidaili.com/nn/


def getHeaders():
    user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362']
    headers = {'User-Agent': random.choice(user_agents)}
    return headers


def getHtml(url):
    try:
        time.sleep(random.random())
        req = requests.get(url, headers=getHeaders(),
                           proxies=proxies, timeout=5)
        req.encoding = req.apparent_encoding
        req.close()
        return req.text
    except Exception as e:
        return ""


def getProxies():
    req = requests.get('https://www.xicidaili.com/nn/', headers=getHeaders())
    req.encoding = req.apparent_encoding
    req.close()
    pat = '<td>(.+)</td>(\s+)<td>(.+)</td>(\s+)<td>(\s+)<a href="(.+)">(.+)</a>(\s+)</td>(\s+)<td class="country">高匿</td>(\s+)<td>(.+)</td>'
    result = re.findall(pat, req.text)
    for i in range(0, 8):
        proxies[result[i][10]].append(
            result[i][10]+'://'+result[i][0]+':'+result[i][2])


class From(threading.Thread):
    def __init__(self, url, num):
        threading.Thread.__init__(self)
        self.url = url
        self.num = num

    def run(self):
        content = getHtml(self.url)
        if content == '':
            return
        pat = '<div class="cdhzz">出自诗人<strong><A href="(.+)">(.+)</A></strong>的《<strong><a href="(.+)" target="_blank">(.+)</a></strong>》'
        result = re.findall(pat, content)
        if len(result) > 0:
            sen[self.num].append(result[0][1])
            sen[self.num].append(result[0][3])
        s = ""
        l = len(sen[self.num])
        for i in range(0, 3):
            if i:
                s += ','
            if i < l:
                s += sen[self.num][i]
        f = open('诗词.txt', 'a+', encoding='UTF-8-SIG')
        f.write(s+'\n')
        f.close()


if __name__ == "__main__":
    sen = []
    cnt = 0
    proxies = defaultdict(list)
    getProxies()
    # print(proxies)
    l = int(input('Please input l: '))
    r = int(input('Please input r: '))
    for i in range(l, r):
        if i % 10 == 0:
            time.sleep(random.randint(8, 15))
        url = 'https://m.gswen.cn/rhesis/0/0/0/'+str(i)+'/'
        content = getHtml(url)
        # print(content)
        if content == '':
            continue
        pat = '<div class="li"><h2><a href="(.+)">(.+)</a></h2></div>'
        result = re.findall(pat, content)
        # print(result)
        for j in result:
            sen.append([j[1]])
            url1 = 'https://m.gswen.cn'+j[0]
            t1 = From(url1, cnt)
            t1.start()
            cnt += 1
        print(i, 'ok')
