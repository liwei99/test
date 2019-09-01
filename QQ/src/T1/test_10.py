#!/usr/bin/python
#-*- conding:utf-8 -*-


from appium import webdriver
from time import sleep
import yaml
import pytest
from until.ReadData import s
from selenium.common.exceptions import NoSuchElementException
from until.mylog import get_logger


log = get_logger(file="test_1.py")


with open(file=r"E:\QQ\element\login.yaml",mode='r',encoding="utf-8") as fb:
    e = yaml.load(fb,Loader=yaml.FullLoader)




"""
@pytest.mark.parametrize("zh,mm",s)
# 账号、密码登录QQ
def test_3(zh,mm,lian):

    lian.find_element_by_accessibility_id(e["zhang"]).clear()
    log.info(f"输入的账号是{zh}")

    #再向输入账号内输入账号
    lian.find_element_by_accessibility_id(e["zhang"]).send_keys(zh)

    lian.find_element_by_id(e["passwd"]).clear()
    log.info(f"输入的密码是{mm}")
    lian.find_element_by_id(e['passwd']).send_keys(mm)

    lian.find_element_by_id(e["longin"]).click()

    try:
        a = lian.find_element_by_accessibility_id(e['ree']).text
        assert a == '忘记密码'
        log.info(f"断言成功，显示{a}")

    except NoSuchElementException:
        b = lian.find_element_by_id(e['shibai']).text
        assert b == '确定'
        log.info(f"断言成功，显示{b}")

        lian.find_element_by_id(e['shibai']).click()

    try:
        c = lian.find_element_by_id(e['xiao']).text
        assert c == '消息'
        log.info(f"断言成功，显示{c}")


    except:
        pass

"""

# 账号、密码登录QQ
def test_1(lian):
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



