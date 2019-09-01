#!/usr/bin/python
#-*- conding:utf-8 -*-



def swipe_left(driver,t=500):
    # 获取手机屏幕的大小
    l = driver.get_window_size()

    # 放缩屏幕
    x1 = l["width"] * 0.2
    x2 = l["width"] * 0.75
    y1 = l["height"] * 0.25
    y2 = l["height"] * 0.8
    driver.swipe(x2,y1,x1,y1,duration=t)

def swipe_right(driver,t=500):
    # 获取手机屏幕的大小
    l = driver.get_window_size()

    # 放缩屏幕
    x1 = l["width"] * 0.1
    x2 = l["width"] * 0.9
    y1 = l["height"] * 0.1
    y2 = l["height"] * 0.9
    driver.swipe(x1,y1,x2,y1,duration=t)






# # 左滑动
# driver.swipe(x2,y1,x1,y1,t = 500)    # t 为点击时间，单位为毫秒
#
# # 右滑动
# driver.swipe(x1,y2,x2,y2,t = 500)



# 源码
# swipe(self, start_x, start_y, end_x, end_y, duration=None)
#     Swipe from one point to another point, for an optional duration.
#     从一个点滑动到另外一个点，duration是持续时间
#
#     :Args:
#     - start_x - 开始滑动的x坐标
#     - start_y - 开始滑动的y坐标
#     - end_x - 结束点x坐标
#     - end_y - 结束点y坐标
#     - duration - 持续时间，单位毫秒
#
#     :Usage:
#     driver.swipe(100, 100, 100, 400)
