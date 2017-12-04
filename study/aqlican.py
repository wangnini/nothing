# -*-  coding: utf-8 -*-


from selenium import  webdriver

web=webdriver.Chrome()


web.get('http://sso.aqlicai.cn/')

web.find_element_by_class_name('JS-username').clear()
web.find_element_by_class_name('JS-username').send_keys('wuhan')
web.find_element_by_class_name('JS-password').clear()
web.find_element_by_class_name('JS-password').send_keys('wuhan123')

web.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[3]').click()