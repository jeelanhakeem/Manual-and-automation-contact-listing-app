"""
    This file contains Login testcases
    Author: Hmd Jeelan
    Date : 26th Feb 2025
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


class TestDemo:
    def test_demo(self):
        """
        This testcase validates login features with  invalid username and password
            1.Open browser
            2.Load the URL
            3.Enter the Phone number
            4.Click the Get OTP  button
            5.Enter OTP and click On submit
        :return:
        """

        driver = webdriver.Chrome()

        try:
            driver.get("https://pp-web.flurn.in/login")
            time.sleep(2)
            phone_input = driver.find_element(By.NAME, "phone")
            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            phone_input.send_keys('9949127203')
            login_button.click()
            time.sleep(5)

            otp_input = driver.find_element(By.NAME, "otp")
            otp_input.send_keys('565656')
            submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            submit_button.click()
            time.sleep(5)

            print("Login process completed.")
        finally:
            driver.quit()