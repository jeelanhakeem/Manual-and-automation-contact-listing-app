"""
    his file contains invalid login testcases
    Author: Jeelan
    Date : 28th Jan 2025
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class TestLoginInvalid:
        """
        This class contain testcases for login
        """

        def test_login_with_invalid_username_password(self):
            """
            This testcase validates login features with  invalid username and password
            1.Open browser
            2.Load the URL
            3.Enter the username and password
            4.Click the submit button
            :return:
            """
            #driver = webdriver.Chrome()
            #driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
            #time.sleep(10)
            #driver.find_element(By.ID,"email").send_keys("jeelan45@gmail.com")
            #driver.find_element(By.ID, "password").send_keys("jeelan123456")
            #driver.find_element(By.ID, "submit").click()
            #time.sleep(4)
            #error_mess= driver.find_element(By.ID, "error").text
            #assert  error_mess== "Incorrect username or password","Error while login"
            driver = webdriver.Chrome()
            driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
            time.sleep(5)
            #driver.find_element(By.XPATH, "//input[@id='email']").send_keys("jeelu")
            driver.find_element(By.XPATH,"//input[(@id='email')]").send_keys("jeelu123@gmail.com")
            #driver.find_element(By.XPATH, "//input[@id='password']").send_keys("fjnsiinso12")
            driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
            time.sleep(5)
            # Enter credentials and submit
            #email.send_keys("admin")
            #password.send_keys("password123")
            #time.sleep(5)
            #submit_button.click()
            #time.sleep(3)
            error_mess = driver.find_element(By.ID, "error").text
            assert error_mess =="Incorrect username or password", "Error while login"
