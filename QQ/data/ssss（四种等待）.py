#!/usr/bin/python
#-*- conding:utf-8 -*-

# appium的四种等待
"""
    1、sleep ：强制等待。工作的线程会停止一段时间
    2、implicitly_wait(time_to_wait) ：隐形等待。
        设置最大等待时间，关键字参数：time_to_wait=10，超过最大等待时间后则会抛出异常
    3、wait_activity() ：安卓独有的等待
         等待某个activity出现，设置最大等待时间，超出最大等待的时间，就会抛出异常

         只能用于等待activity
    4、智能等待


"""


# WebDriverWait    等待某一个元素加载出来
# expected_conditions       selenium的异常处理类
# By  指的是通过什么方式进行定位     例如：By.ID    通过ID的方式进行定位

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait       #等待某一个元素加载出来
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.common.by import By

WebDriverWait("参数一","参数二","参数三").until(EC.presence_of_all_elements_located("参数四"))

"""
    参数一 ：我们与手机建立的参数  ---->  dr
    参数二 ：最大等待时间，单位：秒
    参数三 ：刷新页面的时间间隔，单位：秒
    # 直到某个元素被找到，停止等待
    until(EC.presence_of_all_elements_located("参数四")
    参数四 ：一个由定位方法和元素组成的元组   例如：(By.ID,"元素")
"""


"""
# 
locator = (By.ID, "android:id/tabs")    #此为定位某个元素
try:
    WebDriverWait(dr, 20, 0.5).until(EC.presence_of_element_located((locator))
except:
   print("元素未找到")

"""