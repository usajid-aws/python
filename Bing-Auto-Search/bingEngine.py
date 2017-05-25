'''
***************************************************************
...............................................................
auto-generated bing search engine
...............................................................
@author------>Usama.S
****************************************************************
'''

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
Edge = webdriver.Edge("C:/Users/usana/Desktop/Extra C/python/MicrosoftWebDriver.exe")
Edge.get("https://www.bing.com")
textfile = open("words.txt", "r")
wordList = textfile.readlines()
search = Edge.find_element_by_class_name("b_searchbox")

for i in range (0,len(wordList)):
	if i==60:
		break
	try:
		me = wordList[randint(0,999)]
		search.send_keys(me)
		search.send_keys(Keys.RETURN)
		search = Edge.find_element_by_class_name("b_searchbox")
		time.sleep(2)
	except Exception:
		search = Edge.find_element_by_class_name("b_searchbox")
		search.clear()
		me = wordList[randint(0,999)]
		search.send_keys(me)
		search.send_keys(Keys.RETURN)
		continue
	
Edge.quit()	
quit()

