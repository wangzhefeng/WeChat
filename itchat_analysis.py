#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: tinker
@date: 2019-01-06
"""

"""
pip install itchat
pip install matplotlib
pip install numpy
pip install PIL/Pillow
"""


# load packages
import itchat
import re
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
from os import listdir
import math
import pandas as pd

# font config
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False   # 用来正常显示负号
zhfont = mpl.font_manager.FontProperties(fname = "E:/DataScience/wechat/msyh.ttf")


# 登录微信
itchat.auto_login(hotReload = True)


def get_friends():
	# 获取好友信息
	friends = itchat.get_friends(update = True)
	print(friends)
	# 好友数量
	print(len(friends))

	return friends


def parse(friends):
	df = pd.DataFrame(friends)
	return df


def main():
	friends = get_friends()
	df = parse(friends)
	print(df)
	df.to_excel("E:/wechat_friends.xlsx")

if __name__ == "__main__":
	main()