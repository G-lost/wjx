from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
import random
import requests
import redis
import time

# redis_pool = redis.ConnectionPool(host='127.0.0.1', port='6379')
# redis_con = redis.Redis(connection_pool=redis_pool)
#
# print(redis_con.dbsize())
for i in range(20):
# 	print(redis_con.get(i))

	print(random.randint(0,5))