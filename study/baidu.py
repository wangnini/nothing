# -*- coding: utf-8 -*-

#导入selenium的webdirver包，导入webdirver包才能使用webdirver API进行自动化脚本的开发
from selenium import  webdriver
import time

#获得浏览器对象
browser =webdriver.Chrome()


#通过id =kw 定位到百度输入框，通过键盘方法 send_keys()向输入框中输入selenium
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()

print '浏览器最大化'
browser.maximize_window()


print '设置浏览器宽480、高800显示'
browser.set_window_size(480,800)

#访问百度首页

first_url ='http://www.baidu.com'
print 'now access %s' %(first_url)
browser.get(first_url)

#访问新闻页面

second_url ='http://news.baidu.com'
print 'now access %s' %(second_url)
browser.get(second_url)

#返回到百度首页
print 'back to %s' %(first_url)
browser.back()

#前进到新闻页
print  'forward to %s' %(second_url)
browser.forward()




