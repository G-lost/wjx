from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
import random
import requests
import redis
import time

flag = 0
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
randNum = 0
flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0
flag5 = 0

redis_pool = redis.ConnectionPool(host='127.0.0.1', port='6379')
redis_con = redis.Redis(connection_pool=redis_pool)
print(redis_con.dbsize())


def proxies_ip(ip):
    if 'https' not in ip:
        proxies = {'http': ip}
    else:
        proxies = {'https': ip}
    return proxies


def get_proxies():
    # 这个while True 在这里针对我的redis写的。自己用时自行修改
    while True:
        global randNum
        randNum = random.randint(0, 300)
        ip = redis_con.get(randNum)
        if ip:
            ip = str(ip)[2:-1]
            try:
                r = requests.get('http://www.ip138.com/', headers=headers, proxies=proxies_ip(ip), timeout=1, verify=False)
                # 验证该代理是否可用
                break
            except Exception as e:
                continue
    print('正在使用代理', ip)
    return ip


def click(i, tag):
    tar = i.find_elements_by_tag_name(tag)
    for r in tar:
        global flag
        global flag1
        global flag2
        global flag3
        global flag4
        global flag5

        flag = flag + 1
        a = r.find_elements_by_tag_name('a')
        le = len(a)-1
        # randnum = random.randint(0, le)
        randnum = -1
        if flag == 2:
            while randnum < 0 or randnum > le:
                randnum = int(random.normalvariate(1.5, 1))

        elif flag == 4:
            randnum = 0
        # elif flag >=8 and flag <=23:
        #     while randnum < 0 or randnum > le:
        #         randnum = int(random.normalvariate(3, 1.5))

        elif flag >= 5 and flag <= 7:
            if flag1 ==0 :
                while randnum < 0 or randnum > le:
                    randnum = random.randint(0, le)
                if randnum >= 2:
                    flag1 = 1
                elif randnum < 2:
                    flag1 = -1
            elif flag1 ==1:
                while randnum < 2 or randnum > le:
                    randnum = int(random.normalvariate(3, 1.2))
            elif flag1 == -1:
                while randnum < 0 or randnum > 2:
                    randnum = int(random.normalvariate(1, 1.2))

        elif flag >= 8 and flag <= 12:
            if flag2 == 0:
                while randnum < 0 or randnum > le:
                    randnum = int(random.normalvariate(3, 1.2))
                if randnum >= 2:
                    flag2 = 1
                elif randnum < 2:
                    flag2 = -1
            elif flag2 == 1:
                while randnum < 2 or randnum > le:
                    randnum = int(random.normalvariate(3, 1.2))
            elif flag2 == -1:
                while randnum < 0 or randnum > 2:
                    randnum = int(random.normalvariate(1, 1.2))

        elif flag >= 13 and flag <= 16:
            if flag3 == 0:
                while randnum < 0 or randnum > le:
                    randnum = int(random.normalvariate(3, 1.2))
                if randnum >= 2:
                    flag3 = 1
                elif randnum < 2:
                    flag3 = -1
            elif flag3 == 1:
                while randnum < 2 or randnum > le:
                    randnum = int(random.normalvariate(3, 1.2))
            elif flag3 == -1:
                while randnum < 0 or randnum > 2:
                    randnum = int(random.normalvariate(1, 1.2))

        elif flag >= 17 and flag <= 21:
            if flag4 == 0:
                while randnum < 0 or randnum > le:
                    randnum = int(random.normalvariate(3, 1.2))
                if randnum >= 2:
                    flag4 = 1
                elif randnum < 2:
                    flag4 = -1
            elif flag4 == 1:
                while randnum < 2 or randnum > le:
                    randnum = int(random.normalvariate(3, 1.2))
            elif flag4 == -1:
                while randnum < 0 or randnum > 2:
                    randnum = int(random.normalvariate(1, 1.2))

        elif flag == 22 or flag == 23:
            if flag5 == 0:
                while randnum < 0 or randnum > le:
                    randnum = int(random.normalvariate(3, 1.2))
                if randnum >= 2:
                    flag5 = 1
                elif randnum < 2:
                    flag5 = -1
            elif flag5 == 1:
                while randnum < 2 or randnum > le:
                    randnum = int(random.normalvariate(3, 1.2))
            elif flag5 == -1:
                while randnum < 0 or randnum > 2:
                    randnum = int(random.normalvariate(1, 1.2))

        else:
            randnum = random.randint(0, le)

        for k, n in enumerate(a):
            try:
                n.click()
                if k == randnum:
                    break
            except:
                pass


def main():
    div_question = chrome.find_elements_by_class_name('div_question')
    for i in div_question:
        click(i, 'ul')
        click(i, 'tr')
        #submit_content(i)
    submit = chrome.find_element_by_id('submit_button').click()



if __name__ == '__main__':
    #url = input('请输入问卷星的问卷调查链接：')
    url = "https://www.wjx.cn/jq/43346879.aspx"
    #url = "http://www.ip138.com"
    #proxy = Proxy({'proxyType': ProxyType.MANUAL, 'httpProxy': 'ip:port'})
    chrome_options = webdriver.ChromeOptions()
    while True:
        chrome_options.add_argument('--proxy-server={}'.format(get_proxies()))
        chrome = webdriver.Chrome(chrome_options=chrome_options)
        # chrome.maximize_window()
        try:
            chrome.get(url)
            main()
            chrome.quit()
            break
        except:
            redis_con.delete(randNum)
            chrome.quit()


    for i in range(70):
        flag = 0
        flag1 = 0
        flag2 = 0
        flag3 = 0
        flag4 = 0
        flag5 = 0
        time.sleep(2)
        #chrome.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        while True:
            chrome_options.add_argument('--proxy-server={}'.format(get_proxies()))
            chrome = webdriver.Chrome(chrome_options=chrome_options)
            try:
                chrome.get(url)
                main()
                chrome.quit()
                break
            except:
                redis_con.delete(randNum)
                chrome.quit()
        #chrome.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    print('问卷填写完成！')
    chrome.quit()