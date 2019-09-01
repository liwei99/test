#!/usr/bin/python
#-*- conding:utf-8 -*-

from appium import webdriver
from time import sleep
import pytest


@pytest.fixture(scope="module")
def lian():
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
    sleep(15)
    return dr


