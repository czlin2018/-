#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 13:56
# @Author  : 泽林
# @Site    :
# @File    : 11.py
# @Software: PyCharm
from bs4 import BeautifulSoup
import os, sys

class taq():
    def __init__(self,path=""):
        self.path=path
    def do(self):
        dirs=open(self.path)

        j = 1
        for i in dirs:
            j = j + 1
            i = str(i)
            i=i.replace("\n","")
            name = "H:/团队/support.huaweicloud.com/" + i
            a = open(name, "r", encoding="ansr")
            wenben = a.read()
            soup = BeautifulSoup(wenben)
            que = soup.find_all("h1", class_="topictitle1")  # 找到问题
            try:
                # print(que[0].string)
                ans = que[0].next_sibling.text  # 找到问题下的解释
                print(j)
                a.close()
                i = i.replace(".html", ".txt")

                open1 = "C:/Users/czldd/Desktop/last/faq/" + i
                f = open(open1, 'w')

                que = str(que[0].string)
                ans = str(ans)
                f.write(que)
                f.write("\n")
                f.write("\n")
                f.write(ans)
                f.close()
            except:
                print("err:" + name)
                f1 = open("C:/Users/czldd/Desktop/last/faq/1err.txt", 'a')
                f1.write(name)
                f1.write("\n")
                continue

        open1 = open("C:/Users/czldd/Desktop/last/faq/1err.txt", "r")
        for i in open1:
            j = j + 1
            i = str(i)
            i = i.replace("\n", "")

            name = i
            a = open(name, "r", encoding="utf-8")
            wenben = a.read()
            soup = BeautifulSoup(wenben)

            que = soup.find_all("p", class_="hc-title")  # 找到问题
            try:
                print(que[0].string)
                ans = que[0].parent.text  # 找到问题下的解释
                print(ans)
                print(j)
                a.close()

                i = i.replace(".html", ".txt")
                i = i.replace("Desktop/faq", "Desktop/last")

                open1 = i
                f = open(open1, 'w')

                que = str(que[0].string)
                ans = str(ans)

                f.write(ans)
                f.close()
            except:
                print("err:" + name)
                f1 = open("C:/Users/czldd/Desktop/last/faq/1err1.txt", 'a')
                f1.write(name)
                f1.write("\n")
                continue

        os.remove("C:/Users/czldd/Desktop/last/faq/1err.txt")

        open1 = open("C:/Users/czldd/Desktop/last/faq/1err1.txt", "r")
        for i in open1:
            j = j + 1
            i = str(i)
            i = i.replace("\n", "")

            name = i
            a = open(name, "r", encoding="utf-8")
            wenben = a.read()
            soup = BeautifulSoup(wenben)

            try:
                que = soup.find_all("h1", class_="topictitle1")  # 找到问题
                ans = soup.find_all("div", id="body8662426")  # 找到答案
                print(que[0].string)
                print(ans[0].get_text())

                if ans[0].get_text().isspace() or ans[0].get_text() == "":
                    print("++++++++++++++++++++++++++++++++++++" + name)
                    f1 = open("C:/Users/czldd/Desktopp/last/faq/1err.txt", 'a')
                    f1.write(name)
                    f1.write("\n")
                    continue

                i = i.replace(".html", ".txt")
                i = i.replace("Desktop/faq", "Desktop/last")
                open1 = i
                f = open(open1, 'w')

                que = str(que[0].string)
                ans = str(ans[0].get_text())
                f.write(que)
                f.write("\n")
                f.write(ans)
                f.close()
            except:
                print("err:" + name)
                f1 = open("C:/Users/czldd/Desktop/last/faq/1err2.txt", 'a')
                f1.write(name)
                f1.write("\n")
                continue

        os.remove("C:/Users/czldd/Desktop/last/faq/1err1.txt")
        os.remove("C:/Users/czldd/Desktop/last/faq/1err2.txt")
# if __name__ == '__main__':
#         path = "C:/Users/czldd/Desktop/last/本地faq文件.txt"
#         work=taq(path)
#         work.do()










