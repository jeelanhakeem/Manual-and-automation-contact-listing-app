"""
    his file contains valid login testcases
    Author: Jeelan
    Date : 28th Jan 2025
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

class TestValidLogin:
    """
    this is valid details test class
    """
    def test_login_with_valid_username_password(self):

        """
        This testcase validates login features with  invalid username and password
        1.Open browser
        2.Load the URL
        3.Enter the username and password
        4.Click the submit button
        :return:
        """
        driver=webdriver.Chrome()
        driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
        time.sleep(10)
        driver.find_element(By.ID, "ap_email_login").send_keys("jeelan@gmail.com")
        driver.find_element(By.ID, "password").send_keys("jeelan123456")
        driver.find_element(By.ID, "submit").click()
        time.sleep(4)


