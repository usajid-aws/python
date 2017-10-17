'''

opens and logs into fb incognito 
user input id and pass

''' 


from selenium import webdriver
from getpass import getpass

user_id = input("please enter User name:")
user_pass = getpass()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
facebook = webdriver.Chrome(chrome_options=chrome_options)
facebook.get("https://www.facebook.com/")
username = facebook.find_element_by_id("email")
username.send_keys(user_id)
password = facebook.find_element_by_id("pass")
password.send_keys(user_pass)
enter = facebook.find_element_by_id("loginbutton")
enter.click()




