#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 12:36
# @Author  : 泽林
# @Site    :
# @File    : 11.py
# @Software: PyCharm
import re
import os, sys
from bs4 import BeautifulSoup
from 本地文件提取aq import taq
DBUG = 0

falt=0
reBODY = r'<body.*?>([\s\S]*?)<\/body>'
reCOMM = r'<!--.*?-->'
reTRIM = r'<{0}.*?>([\s\S]*?)<\/{0}>'
reTAG = r'<[\s\S]*?>|[ \t\r\f\v]'

reIMG = re.compile(r'<img[\s\S]*?src=[\'|"]([\s\S]*?)[\'|"][\s\S]*?>')


class Extractor():
    def __init__(self, url="", blockSize=3, timeout=5, image=False):
        self.url = url
        self.blockSize = blockSize
        self.timeout = timeout
        self.saveImage = image
        self.rawPage = ""
        self.ctexts = []
        self.cblocks = []

    def getRawPage(self):
        try:

            a = open(self.url, "r", encoding="utf-8")
            resp = a.read()
        except Exception as e:
            raise e

        return  200, resp

    # 去除所有tag，包括样式、Js脚本内容等，但保留原有的换行符\n：
    def processTags(self):
        self.body = re.sub(reCOMM, "", self.body)
        self.body = re.sub(reTRIM.format("script"), "", re.sub(reTRIM.format("style"), "", self.body))
        # self.body = re.sub(r"[\n]+","\n", re.sub(reTAG, "", self.body))
        self.body = re.sub(reTAG, "", self.body)

    # 将网页内容按行分割，定义行块 blocki 为第 [i,i+blockSize] 行文本之和并给出行块长度基于行号的分布函数：
    def processBlocks(self):
        self.ctexts = self.body.split("\n")


        self.textLens = [len(text) for text in self.ctexts]

        self.cblocks = [0] * (len(self.ctexts) - self.blockSize - 1)

        lines = len(self.ctexts)

        for i in range(self.blockSize):
            self.cblocks = list(map(lambda x, y: x + y, self.textLens[i: lines - 1 - self.blockSize + i], self.cblocks))

        try:
         maxTextLen = max(self.cblocks)
        except Exception as e:
            falt=1


        if DBUG: print(maxTextLen)
        self.start = self.end = self.cblocks.index(maxTextLen)
        while self.start > 0 and self.cblocks[self.start] > min(self.textLens):
            self.start -= 1
        while self.end < lines - self.blockSize and self.cblocks[self.end] > min(self.textLens):
            self.end += 1
        return "".join(self.ctexts[self.start:self.end])

    # 如果需要提取正文区域出现的图片，只需要在第一步去除tag时保留<img>标签的内容：
    def processImages(self):
        self.body = reIMG.sub(r'{{\1}}', self.body)

    # 正文出现在最长的行块，截取两边至行块长度为 0 的范围：
    def getContext(self):
        code, self.rawPage = self.getRawPage()

        self.body = re.findall(reBODY, self.rawPage)[0]
        if DBUG: print(code, self.rawPage)
        if self.saveImage:
            self.processImages()
        self.processTags()
        return self.processBlocks()

        # print(len(self.body.strip("\n")))


if __name__ == '__main__':
    k=1
    path = "H:/团队/support.huaweicloud.com"
    dirs = os.listdir(path)

    for i in dirs:
        print(k)
        k=k+1
        i = str(i)
        faq="faq"
        if i.find(faq)!=-1:

            f1 = open("C:/Users/czldd/Desktop/last/本地faq文件.txt", 'a')
            f1.write(i)
            f1.write("\n")

        if i=="desktop.ini" or i.find(faq)!=-1 or falt==1:
            print("排除",i)
            print(i.find(faq))
            continue
        name = "H:/团队/support.huaweicloud.com/" + i
        try:
      #获取正文
            ext = Extractor(url=name, blockSize=5, image=False)
           # print(ext.getContext())
      # 获取标题
            a = open(name, "r", encoding="utf-8")
            wenben = a.read()
            soup = BeautifulSoup(wenben)


            i = i.replace(".html", ".txt")
            f1 = open("C:/Users/czldd/Desktop/last/notfaq/"+i, 'a',encoding="utf-8")
            f1.write(soup.title.string)
            f1.write("\n")
            f1.write("\n")
            f1.write(ext.getContext())
        except Exception as e:
            print("此网页出错：",i)
            continue
    work=taq("C:/Users/czldd/Desktop/last/本地faq文件.txt")
    work.do()

