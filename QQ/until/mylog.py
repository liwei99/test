#!/usr/bin/python
#-*- conding:utf-8 -*-
import logging
import datetime


# 日志文件夹/目录
LOG_DIR = "E:\\QQ\\log\\"

# 创建一个日志文件，名为：日期.txt
a = LOG_DIR  + str(datetime.datetime.now().date()) + '.txt'
# print(a)


# logging  ：python定义日志的库

#定义日志输出的格式
formatter = logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S')

# print(formatter)

#logging的两种输出方式：
#第一种：输出到pycharm控制台
c = logging.StreamHandler()

#添加日志样式
c.setFormatter(formatter)

#第二种：输出到文本
w = logging.FileHandler(a,encoding="utf-8")

#添加日志样式
w.setFormatter(formatter)


# 写日志
def get_logger(file):
    #获取执行日志的脚本名字
    l = logging.getLogger(file)
    #添加输出内容到控制台
    l.addHandler(c)

    #添加输出内容到文本
    l.addHandler(w)

    #定义日志的等级    INFO / DBBUG：建议（最低等级） （最低等级中可以放最高等级的）
    l.setLevel(logging.INFO)
    return l



# log = get_logger()
# log.info("44444")
# log.error("888888")   #错误





