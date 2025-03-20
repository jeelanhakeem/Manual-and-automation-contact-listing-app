'''
# Parametric fixture for login credentials
@pytest.fixture(params=[
    {"username": "valid_user", "password": "correct_pass", "expected": "success"},
    {"username": "invalid_user", "password": "wrong_pass", "expected": "failure"},
    {"username": "valid_user", "password": "wrong_pass", "expected": "failure"},
    {"username": "", "password": "", "expected": "failure"},
])
def login_data(request):
    return request.param  # Returns each dictionary one by one

# Simulated login function (replace with actual login logic)
def login(username, password):
    if username == "valid_user" and password == "correct_pass":
        return "success"
    return "failure"

# Test function using parametric fixture
def test_login(login_data):
    result = login(login_data["username"], login_data["password"])
    assert result == login_data["expected"]
'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def driver():
    # Setup: Create a WebDriver instance
    print("****driver setup****")
    driver = webdriver.Chrome()
    yield driver
    print("****driver teardown****")
    # Teardown: Close the WebDriver instance
    driver.quit()


class TestLoginInvalid:
        """
        This class contain testcases for login
        """

        @pytest.mark.parametrize("email,password,expected_error_msg",[("jeelan2344@gmail.com","qwwerr","Incorrect username or password"),("jeelan3456@gmail.com","jeelan12rt3456","Incorrect username or password")])
        def test_login_with_invalid_username_password(self,driver,email,password,expected_error_msg):
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
            driver.find_element(By.ID,"email").send_keys(email)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "submit").click()
            time.sleep(4)
            error_mess= driver.find_element(By.ID, "error").text
            assert  error_mess== expected_error_msg,"Error while login"


        @pytest.mark.parametrize("email,password",[("jeelan@gmail.com","jeelan123456")])
        def test_login_with_valid_username_password(self,driver,email,password):
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
            #time.sleep(5)
            driver.find_element(By.ID,"email").clear()
            driver.find_element(By.ID, "email").send_keys(email)
            driver.find_element(By.ID, "password").clear()
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "submit").click()
            time.sleep(2)
            driver.find_element(By.ID, "add-contact")
            time.sleep(3)
            assert driver.current_url == "https://thinking-tester-contact-list.herokuapp.com/contactList"
