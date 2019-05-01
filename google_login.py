#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
import getpass
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--incognito")
   
chromdriv = '/opt/chromedriver'
os.environ["webdriver.chrome.driver"] = chromdriv
driver = webdriver.Chrome(chromdriv)
url = 'https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default    &ltmplcache=2&emr=1&osid=1'
 #url = 'https://www.facebook.com'
driver.get(url)
  
username = raw_input('enter your gmail login: ')
print 'Passwd wont be echoed'
userpass = getpass.getpass()
user = "Email"
nxtbutton = '//*[@id="next"]'
passes = "Passwd"
logbutton = '//*[@id="signIn"]'
  
userinput = WebDriverWait(driver,10).until(
            lambda driver : driver.find_element_by_name(user))
userinput.clear()
userinput.send_keys(username)
nextbutton = WebDriverWait(driver,10).until(
             lambda driver : driver.find_element_by_xpath(nxtbutton))
nextbutton.click()
passwdbox = WebDriverWait(driver,10).until(
            lambda driver : driver.find_element_by_name(passes))
passwdbox.clear()
passwdbox.send_keys(userpass)
loginbutton = WebDriverWait(driver,10).until(
             lambda driver : driver.find_element_by_xpath(logbutton))
loginbutton.click()

