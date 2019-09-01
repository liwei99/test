#!/usr/bin/python
#-*- conding:utf-8 -*-

with open(file=r"E:\QQ\data\login.txt",mode="r",encoding="utf-8") as f:
    datas = f.read().split(';')
s = []
for i in datas:
    k = i.replace('\n','').split(",")
    s.append(tuple(k))

if __name__ == "__main__":
    print(s)










