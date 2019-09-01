#!/usr/bin/python
#-*- conding:utf-8 -*-

from appium import webdriver
from time import sleep
import yaml



with open(file=r"E:\QQ\element\login.yaml",mode='r',encoding="utf-8") as fb:
    e = yaml.load(fb,Loader=yaml.FullLoader)
# print(e)

d = {
      "platformName": "Android",
      "platformVersion": "5.1.1",
      "deviceName": "emulator-5554",
      "appPackage": "com.tencent.mobileqq",
      "appActivity": ".activity.SplashActivity",
      "noReset": "true",
      "unicodeKeyboard": "true"
}

#建立连接并开启QQ程序
dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
#等待程序驱动
sleep(10)



# 账号、密码登录QQ
def test_3(lian):
    #
    lian.find_element_by_accessibility_id(e["zhang"]).clear()
    #再向输入账号内输入账号
    lian.find_element_by_accessibility_id(e["zhang"]).send_keys("1778109280")
    lian.find_element_by_id(e["passwd"]).clear()
    lian.find_element_by_id(e['passwd']).send_keys("LI84036698WEI")
    lian.find_element_by_id(e["longin"]).click()





# #执行退出账号的操作
# def test_2(lian):
#     lian.find_element_by_xpath(e['tou']).click()
#     sleep(1)
#     lian.find_element_by_id(e["seting"]).click()
#     sleep(1)
#     lian.find_element_by_id(e['zhanghao']).click()
#     sleep(1)
#     lian.find_element_by_id(e['tuihao']).click()
#     sleep(1)
#     lian.find_element_by_id(e['tuichu']).click()
#     sleep(1)
#
#     a = lian.find_element_by_accessibility_id(e['xinyonghu']).text
#     assert a == '用户注册'
#     print(a)

    #退出 QQ程序
    # lian.quit()






