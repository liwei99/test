#!/usr/bin/python
#-*- conding:utf-8 -*-

from time import sleep
from until.tools import swipe_left
from until.tools import swipe_right



def test_1(lian):
    swipe_right(lian)
    sleep(10)
    swipe_left(lian)
    sleep(10)





