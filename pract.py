#from selenium import webdriver
#driver=webdriver.Chrome()
import time

from selenium import webdriver
import pytest
driver=webdriver.Chrome()
driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
time.sleep(60)
driver.back()