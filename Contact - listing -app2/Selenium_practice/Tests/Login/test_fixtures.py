'''
@pytest.fixture()
def setup():
   print("Login into application")

def test_add_to_cart(setup):
    print("User is able to add a cart")

def test_choose_product(setup):
    print("User is able to choose the product")

def test_payment():
    print("User is able to pay money")

def test_logout():
    print("User is able to logout the application")
'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def driver():
    # Setup: Create a WebDriver instance
    driver = webdriver.Chrome()
    yield driver
    # Teardown: Close the WebDriver instance
    driver.quit()


class TestLoginInvalid:
        """
        This class contain testcases for login
        """
        def test_login_with_invalid_username_password(self,driver):
            """
            This testcase validates login features with  invalid username and password
            1.Open browser
            2.Load the URL
            3.Enter the username and password
            4.Click the submit button
            :return:
            """
            driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
            time.sleep(5)
            driver.find_element(By.ID,"email").send_keys("jeelan45@gmail.com")
            driver.find_element(By.ID, "password").send_keys("jeelan123456")
            driver.find_element(By.ID, "submit").click()
            time.sleep(4)
            error_mess= driver.find_element(By.ID, "error").text
            assert  error_mess== "Incorrect username or password","Error while login"

        def test_signup_with_valid_details(self,driver):

            driver.get("https://thinking-tester-contact-list.herokuapp.com/addUser")
            time.sleep(3)
            driver.find_element(By.ID, "firstName").send_keys("Jeelan")
            driver.find_element(By.ID, "lastName").send_keys("Hakeem")
            driver.find_element(By.ID, "email").send_keys("jeelan@gmail.com")
            driver.find_element(By.ID, "password").send_keys("jeelan123456")
            driver.find_element(By.ID, "submit").click()
            time.sleep(6)
            error_mess = driver.find_element(By.ID, "error").text
            assert error_mess == "Email address is already in use", "Error while signup"
            driver.find_element(By.ID, "cancel").click()


        def test_login_with_valid_username_password(self,driver):
            """
            This testcase validates login features with  invalid username and password
            1.Open browser
            2.Load the URL
            3.Enter the username and password
            4.Click the submit button
            :return:
            """
            driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
            time.sleep(5)
            driver.find_element(By.ID, "email").send_keys("jeelan@gmail.com")
            driver.find_element(By.ID, "password").send_keys("jeelan123456")
            driver.find_element(By.ID, "submit").click()
            time.sleep(4)

            #error_mess = driver.find_element(By.ID, "error").text
            #assert error_mess == "Incorrect username or password", "Error while login"

