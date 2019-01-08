#!/usr/bin/env python3
# -*- coding: utf-8 -*-



from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import json

#===========================================================
#
#===========================================================
bot = Bot()

def get_news():
	url = "http://open.iciba.com/dsapi"
	r = requests.get(url)
	content = json.loads(r.text)['content']
	print(content)
	note = json.loads(r.text)['note']
	print(note)
	return content, note

def send_news():
	try:
		content, note = get_news()
		print(content)
		print(note)
		my_friend = bot.friends().search(u'FWL')[0]
		my_friend.send(content)
		my_friend.send(content)
		my_friend.send(u'Have a good one!')
		t = Timer(1, send_news())
		t.start()
	except:
		my_friend = bot.friends().search(u'wanghefeng')[0]
		my_friend.send(u'今天发送消息失败了')

if __name__ == "__mian__":
	send_news()
