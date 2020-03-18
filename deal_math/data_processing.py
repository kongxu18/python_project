"""
原始数据处理到数据库
"""
import os
filepath ='/Users/mac/Desktop/膜材弹性常数计算说明/20191227090826第一步.txt'
size =os.path.getsize(filepath)
fr=open(filepath,'r')
for i in fr.readlines():
    print(i)
