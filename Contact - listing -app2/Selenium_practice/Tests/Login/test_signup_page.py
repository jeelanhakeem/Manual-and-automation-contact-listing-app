"""
    This file contains signup testcases
    Author: Jeelan
    Date : 28th Jan 2025
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

class TestSignup:
    def test_signup_with_valid_details(self):
        driver = webdriver.Chrome()
        driver.get("https://thinking-tester-contact-list.herokuapp.com/addUser")
        time.sleep(10)
        driver.find_element(By.ID, "firstName").send_keys("Jeelan")
        driver.find_element(By.ID, "lastName").send_keys("Hakeem")
        driver.find_element(By.ID, "email").send_keys("jeelan@gmail.com")
        driver.find_element(By.ID, "password").send_keys("jeelan123456")
        driver.find_element(By.ID, "submit").click()
        time.sleep(10)
        error_mess = driver.find_element(By.ID, "error").text
        assert error_mess == "Email address is already in use", "Error while signup"

