from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://www.radiustheme.com/demo/wordpress/themes/zilly/")
    wait = WebDriverWait(driver, 10)

    # Option 1: Wait for the element to be clickable
    see_more_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "See More"))
    )

    # Option 2: Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", see_more_link)

    # Option 3: Wait for potential overlays to disappear if needed
    # Uncomment and update selector if there is an overlay element causing issues.
    # wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".overlay-selector")))

    # Option 4: Use JavaScript click as a fallback
    try:
        see_more_link.click()
    except Exception as e:
        driver.execute_script("arguments[0].click();", see_more_link)

    wait.until(EC.url_contains("/shop/"))
    print("Successfully navigated to:", driver.current_url)

finally:
    driver.quit()
