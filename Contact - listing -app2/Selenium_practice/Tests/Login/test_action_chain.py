#Test cases for action chain
from os import times

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

'''
class TestActionChain:


    def test_action_chain_demo(self):
        """
        Test case for action chain
        #open the browser and click on blogs
        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://omayo.blogspot.com/#")
        time.sleep(3)

        action=ActionChains(driver)
        blogs=driver.find_element(By.ID,"blogsmenu")
        action.move_to_element(blogs).perform()
        time.sleep(5)
        s_arun=driver.find_element(By.XPATH,"//a/span[text()='SeleniumByArun']")
        action.move_to_element(s_arun).perform()
        time.sleep(3)

        driver.quit()



class TestMouseLeftClick:

    def test_mouse_left_click(self):
        """
        Test case for action chain
        1.open the browser and click on blogs
        2.Mouse left click
        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://omayo.blogspot.com/#")
        time.sleep(3)

        action = ActionChains(driver)
        #blogs = driver.find_element(By.ID, "blogsmenu")
        #action.move_to_element(blogs).perform()
        #time.sleep(5)
        arun = driver.find_element(By.ID, "link1")
        action.click(arun).perform()
        time.sleep(3)

        driver.quit()


class TestRightClick:
    def test_right_click(self):
        """
        This is a test case for Mouse Right Click
        1.It will open the browser.
        2.it will right-click on search bar.
        :return:
        """
        driver = webdriver.Chrome()
        driver.get("https://tutorialsninja.com/demo/")
        search_box = driver.find_element(By.NAME,"search")
        time.sleep(5)
        action = ActionChains(driver)
        #action.context_click(search_box).perform()
        action.context_click().perform()  # If we're not providing search_box element it right-clicks on up left corner i,e x and y coordinate

        time.sleep(5)

        driver.quit()

class TestDoubleClick:
    def test_double_click(self):
        """
        This is a test case for mouse double click

        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://omayo.blogspot.com/2013/05/page-one.html")
        double_click = driver.find_element(By.ID,"testdoubleclick")

        time.sleep(3)
        action =ActionChains(driver)
        action.double_click(double_click).perform()
        time.sleep(8)
        driver.quit()



class TestClickHoldRelease:
    def test_click_hold_release(self):
        """
        This is a test case for click hold and release

        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
        time.sleep(6)
        oslo=driver.find_element(By.ID,"box1")
        denmark=driver.find_element(By.ID,"box104")
        actions =ActionChains(driver)
        actions.click_and_hold(oslo).move_to_element(denmark).release().perform()
        time.sleep(6)
        driver.quit()

class TestDragDrop:
    def test_drag_drop(self):
        """
        This is a test case for Drag and Drop

        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
        time.sleep(6)
        oslo=driver.find_element(By.ID,"box1")
        denmark=driver.find_element(By.ID,"box104")
        actions =ActionChains(driver)
        actions.drag_and_drop(oslo,denmark).perform()
        time.sleep(6)
        driver.quit()

class TestValidLoginEnterKey:
    """
    this is valid details test class by using enter key
    """
    def test_login_with_valid_username_password_enter_key(self):

        """
        This testcase validates login features with  invalid username and password
        1.Open browser
        2.Load the URL
        3.Enter the username and password
        4.Click the enter key
        :return:
        """
        driver=webdriver.Chrome()
        driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
        time.sleep(3)
        driver.find_element(By.ID, "email").send_keys("jeelan@gmail.com")
        time.sleep(3)

        driver.find_element(By.ID, "password").send_keys("jeelan123456")
        time.sleep(3)
        #driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
        action =ActionChains(driver)
        action.send_keys(Keys.ENTER).perform()
        time.sleep(4)

        driver.quit()

class TestKeyUPDown:
    def test_key_up_down_case(self):
        """
        This test case opens multiple links in new tabs using the Control key.
        """

        # Initialize WebDriver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://omayo.blogspot.com/")
        time.sleep(3)  # Wait for page to load

        # Find all links inside the LinkList1 div
        links = driver.find_elements(By.XPATH, "//div[@id='LinkList1']//a")

        # Open each link in a new tab
        for link in links:
            actions = ActionChains(driver)

            actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
            time.sleep(1)  # Small delay for stability

        time.sleep(5)  # Allow time to observe the opened tabs
        driver.quit()  # Close the browser

# Example execution
#if __name__ == "__main__":
    #test = TestKeyUPDown()
    #test.test_key_up_down_case()

class TestAutoSuggestDropDown:
    def test_auto_suggest_drop_down(self):
        """
        This is a test case for AutoSuggestDropDown

        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.makemytrip.com/")
        time.sleep(6)
        driver.find_element(By.ID,"fromCity").click()
        driver.find_element(By.XPATH,"//input[@placeholder='From']").send_keys("g")
        time.sleep(3)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER)
        time.sleep(3)
        driver.quit()

class TestResizing:
    def test_resizing_element(self):
        """
        This is a test case for resizing

        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://jqueryui.com/resizable/")

        frame_one = driver.find_element(By.CLASS_NAME,"demo-frame")
        driver.switch_to.frame(frame_one)
        actions = ActionChains(driver)
        dd = driver.find_element(By.CSS_SELECTOR,"div.ui-icon-gripsmall-diagonal-se")
        time.sleep(2)
        actions.drag_and_drop_by_offset(dd,70,120).perform()
        time.sleep(5)
        driver.quit()

class TestRightClickJquery:
    def test_right_click_jquery(self):
        """
        This is a test case for right click in JQuery

        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
        button =driver.find_element(By.XPATH,"//span[text()='right click me']")
        time.sleep(4)
        actions =ActionChains(driver)
        actions.context_click(button).perform()
        time.sleep(4)
        quit_option = driver.find_element(By.XPATH,"//li/span[text()='Quit']")
        actions.click(quit_option).perform()
        time.sleep(4)
        driver.quit()



class TestAddContactDetails:
    def test_add_contact_details(self):
        """
        This is a test case for right click in JQuery

        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://thinking-tester-contact-list.herokuapp.com/login")


        driver.find_element(By.ID, "email").send_keys("jeelan@gmail.com")
        driver.find_element(By.ID, "password").send_keys("jeelan123456")
        driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        add_contact_button = driver.find_element(By.ID, "add-contact")
        add_contact_button.click()
        driver.find_element(By.ID, "firstName").send_keys("Hmd")
        time.sleep(1)
        driver.find_element(By.ID, "lastName").send_keys("Jeelan")
        time.sleep(1)

        driver.find_element(By.ID, "birthdate").send_keys("1999-01-01")
        time.sleep(1)

        driver.find_element(By.ID, "email").send_keys("hmd@gmail.com")
        time.sleep(1)

        driver.find_element(By.ID, "phone").send_keys("9949127203")
        time.sleep(1)

        driver.find_element(By.ID, "street1").send_keys("Andhra")
        time.sleep(1)

        driver.find_element(By.ID, "street2").send_keys("Ap")
        time.sleep(1)

        driver.find_element(By.ID, "city").send_keys("Atp")
        time.sleep(1)

        driver.find_element(By.ID, "stateProvince").send_keys("Ap")
        time.sleep(1)

        driver.find_element(By.ID, "postalCode").send_keys("515001")
        time.sleep(1)

        driver.find_element(By.ID, "country").send_keys("515001")
        time.sleep(1)

        driver.find_element(By.ID, "submit").click()
        time.sleep(5)

class TestScreenShot:
    def test_screenshot(self):
        """
        This is a test case for right click in JQuery

        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
        #driver.save_screenshot("Homepage.png")

        driver.get_screenshot_as_file("Homepage1.png")
        driver.find_element(By.XPATH,"//button[@id='signup']").click()

        #driver.save_screenshot("signup.png")
        driver.get_screenshot_as_file("signup1.png")
        driver.quit()



class TestHandlingWindows:
    def test_handling_windows(self):
        """
        This is a test case for how to handle the windows

        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://omayo.blogspot.com/")

        parent_window_id = driver.current_window_handle
        driver.find_element(By.LINK_TEXT,"Open a popup window").click()
        time.sleep(5)

        windows = driver.window_handles

        for w in windows:
            driver.switch_to.window(w)
            if driver.title.__eq__("New Window"):
                new_pop_up = driver.find_element(By.CLASS_NAME,"example").text
                print(new_pop_up)
                driver.close()
                break

        driver.switch_to.window(parent_window_id)
        driver.find_element(By.ID,"ta1").send_keys("HMD JEELAN")
        time.sleep(5)
        driver.close()


class TestHandlingWindows1:
    def test_handling_windows1(self):
        """
        This is a test case for how to handle the windows

        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://omayo.blogspot.com/")

        parent_window_id = driver.current_window_handle
        driver.find_element(By.ID,"selenium143").click()
        time.sleep(5)

        windows = driver.window_handles

        for w in windows:
            driver.switch_to.window(w)
            if driver.title.__eq__("Selenium")
        driver.find_element(By.LINK_TEXT,"What should I know prior to learning Selenium?").click()

class TestHandlingWindows2:
    def test_handling_windows2(self):
        """
        This is a test case for how to handle the windows in the same window with multiple windows

        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://omayo.blogspot.com/")

        app_one_title = driver.title
        print("app_one_title")
        time.sleep(3)

        driver.switch_to.new_window('window')

        driver.get("https://selenium143.blogspot.com/")
        time.sleep(3)

        app_two_title = driver.title
        print("app_two_title")
        time.sleep(3)

        driver.quit()

class TestWait:
    def test_waits_implicit_explict(self):
        """
        This is a test case for how to handle the time by using waits in terms of implicit and explict

        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://omayo.blogspot.com/")

        driver.find_element(By.CLASS_NAME,"dropbtn").click()
        wait=WebDriverWait(driver,30)
        gmail_option = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"Gmail")))

        gmail_option.click()

        time.sleep(5)
        driver.quit()

class TestWaitHidden:
    def test_waits_implicit_explict_hidden_button(self):
        """
        This is a test case for how to handle the time by using waits in terms of implicit and explict

        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://omayo.blogspot.com/")

        wait = WebDriverWait(driver,30)
        hidden_button = wait.until(expected_conditions.presence_of_element_located((By.ID,"hbutton")))

        hidden_button_label = hidden_button.get_attribute("value")
        print(hidden_button_label)

        time.sleep(3)
        driver.quit() 


class TestWaitElementClickable:
    def test_waits_element_clickable(self):
        """
        This is a test case for how to handle the time by clicking on the element

        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://omayo.blogspot.com/")

        driver.find_element(By.XPATH,"//button[text()='Check this']").click()
        wait = WebDriverWait(driver,15)
        check_box = wait.until(expected_conditions.element_to_be_clickable((By.ID,"dte")))
        check_box.click()
        time.sleep(5)
        driver.quit()
'''

class TestWaitElementInvisible:
    def test_waits_element_invisible(self):
        """
        This is a test case for how to handle the time by invisible  on the element

        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

        driver.find_element(By.XPATH,"//button[text()='Start']").click()

        wait= WebDriverWait(driver,30)
        progress_section=wait.until(expected_conditions.invisibility_of_element_located((By.ID,"loading")))

        heading_text = driver.find_element(By.XPATH,"//div[@id='finish']/h4").text

        print(heading_text)
        driver.quit()
