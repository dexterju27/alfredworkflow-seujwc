# encoding: utf-8
from feedback import Feedback
import re
fb = Feedback()
# 设置 'utf-8'
from bs4 import BeautifulSoup     
import requests
keywords="{query}"
def news():
	r=requests.get("http://jwc.seu.edu.cn")
	r.encoding="utf-8"
	doc=r.text
	soup = BeautifulSoup(''.join(doc))
	soup.prettify() 
	news=soup.findAll("a",class_="font1",target="_blank")
	for each_item in news:
		if (each_item.text.encode("utf-8")=="新课程中心" or each_item.text.encode('utf-8')=="旧版网站"):
			url=each_item["href"].encode("utf-8")
		else:
			url="http://jwc.seu.edu.cn"+each_item["href"].encode("utf-8")
		fb.add_item(each_item.text,'click to see more',arg=url)
	print fb


def accnews():
	r=requests.get("http://jwc.seu.edu.cn/s/99/t/2128/p/5/list.htm")
	r.encoding="utf-8"
	doc=r.text
	soup=BeautifulSoup("".join(doc))
	soup.prettify()
	news=soup.findAll("a",target="_blank")
	news.pop()
	for each_item in news:
		url="http://jwc.seu.edu.cn"+each_item["href"].encode("utf-8")
		fb.add_item(each_item.text,"click to see more",arg=url)
	print fb
def management():
	r=requests.get("http://jwc.seu.edu.cn/s/99/t/2128/p/6/list.htm")
	r.encoding="utf-8"
	doc=r.text
	soup=BeautifulSoup("".join(doc))
	soup.prettify()
	news=soup.findAll("a",target="_blank")
	news.pop()
	for each_item in news:
		url="http://jwc.seu.edu.cn"+each_item["href"].encode("utf-8")
		fb.add_item(each_item.text,"click to see more",arg=url)
	print fb
	
def srtp():
	r=requests.get("http://jwc.seu.edu.cn/s/99/t/2128/p/7/list.htm")
	r.encoding="utf-8"
	doc=r.text
	soup=BeautifulSoup("".join(doc))
	soup.prettify()
	news=soup.findAll("a",target="_blank")
	news.pop()
	for each_item in news:
		url="http://jwc.seu.edu.cn"+each_item["href"].encode("utf-8")
		fb.add_item(each_item.text,"click to see more",arg=url)
	print fb
def internationl():
	r=requests.get("http://jwc.seu.edu.cn/s/99/t/2128/p/8/list.htm")
	r.encoding="utf-8"
	doc=r.text
	soup=BeautifulSoup("".join(doc))
	soup.prettify()
	news=soup.findAll("a",target="_blank")
	news.pop()
	for each_item in news:
		url="http://jwc.seu.edu.cn"+each_item["href"].encode("utf-8")
		fb.add_item(each_item.text,"click to see more",arg=url)
	print fb
if keywords=="news":
	news()
elif keywords=="info":
	accnews()
elif keywords=="man":
	management()
elif keywords=="srtp":
	srtp()
elif keywords=="inter":
	internationl()
