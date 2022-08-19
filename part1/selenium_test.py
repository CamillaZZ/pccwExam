#!/usr/python/bin

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import configparser

class Autotest:
    def __init__(self, confile, title, key):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")
        # 读取配置文件
        config = configparser.ConfigParser()
        config.read(confile)
        self.count = int(config.get(title, key))

    # 输入地址
    def gotourl(self, url):
        self.driver.get(url)
        time.sleep(3)

    # 输入文字
    def sendkeys(self, text, filename):
        self.driver.save_screenshot(filename)
        self.driver.find_element_by_id('kw').send_keys(text)
        self.driver.find_element_by_id('kw').send_keys(Keys.ENTER)
        time.sleep(3)

    # click flag=0/123结果单个or多个
    def clickelement(self, method, element, filename, flag):
        # 点击前截屏
        self.driver.save_screenshot(filename)
        if flag == 0:
            self.driver.find_element(method, element).click()
        else:
            self.driver.find_elements(method, element)[self.count].click()
        time.sleep(3)

    # 断言
    def assertTF(self):
        pass

    # 退出
    def quit(self):
        self.driver.quit()


a = Autotest("config.ini", "config", "VISIT_RESULT")
# 进入页面
a.gotourl("https://www.baidu.com/")
# 搜索
a.sendkeys("你好", "begin.png")
# 点击按图片搜索
a.clickelement(By.CLASS_NAME, "s-tab-pic", "search.png", 0)
# 点击所要结果
a.clickelement(By.CLASS_NAME, "imgitem", "result.png", 1)
# 退出
a.quit()
