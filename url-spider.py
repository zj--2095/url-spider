# coding: UTF-8
import urllib2
import sys
import re
from bs4 import BeautifulSoup

class spider(object):
	def gethtml(self,url):
		list=[]
		try:
			request = urllib2.Request(url)
			response = urllib2.urlopen(request).read()
		
			soup = BeautifulSoup(response)
			for link in soup.find_all('a'):
				list.append(link.get('href'))
		except:
			pass
		return set(list)
	
	def analysis(self,url,get=[]):
		result=[]
		for i in get:
			if re.match('^(javascript|:;|#)',str(i)) or str(i) is None or re.match('.(jpg|png|bmp|mp3|wma|wmv|gz|zip|rar|iso|pdf|txt|db)$',str(i)):
				continue
			if re.match('^(http|https)',str(i)):
				if not re.match('^'+url,str(i)):
					continue
				else:
					result.append(str(i))
			else:
				a=str(url)+"/"+str(i)
				result.append(a)
		return set(result)

	
if __name__ == '__main__':
	url=sys.argv[1]
	deep=sys.argv[2]
	deep=int(deep)
	result=[]
	list=[]
	html=spider()
	result=html.gethtml(url)
	list=html.analysis(url,result)
	f=open("result1.txt","w")
	for i in list:
		f.write(i)
		f.write("\n")
	f.close()
	if (deep > 1):
		for count in range(1,deep):
			result=[]
			list=[]
			f = open("result"+str(count)+".txt")
			lines = f.readlines()
			for line in lines:
				result=html.gethtml(line)
				
				list=html.analysis(url,result)
				list=set(list)
				d=open("result"+str(count+1)+".txt","a")
				for i in list:
					d.write(i)
					d.write("\n")
				d.close()
			f.close()