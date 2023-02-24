from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("http://www.123formbuilder.com/form-5012215/online-order-form")
driver.maximize_window()
driver.delete_all_cookies()

# wait max 5 sec for page loading, then show "Load Error"
# implicitly_wait() is using for all other browsers
driver.implicitly_wait(5)

page123ExpectedTitle = "Online Order Form"
current_title = driver.title

if current_title == page123ExpectedTitle:
    print("Current title is", driver.title)
else:
    print("Wrong title")

driver.find_element(By.XPATH, "//h1[contains(text(),'Order Form')]")
driver.find_element(By.XPATH, "//p[contains(text(),'Use this fully-responsive order form template and ')]")
# Name
driver.find_element(By.ID, "name-00000008-acc")
driver.find_element(By.XPATH, "//input[@placeholder='First']").send_keys("Ana")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder='Last']").send_keys("Smith")
time.sleep(1)
# Email
driver.find_element(By.ID, "email0000000a-acc")
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("signup@gmail.com")
time.sleep(1)
# Phone
driver.find_element(By.ID, "phone-0000000c-acc")
driver.find_element(By.XPATH, "//input[@placeholder='### ### #### ']").send_keys("773 224 1212")
time.sleep(1)
# Choose preferred product: Product 3
driver.find_element(By.ID, "radio-0000000e-acc")
driver.find_element(By.ID, "0000000e_2").click()
time.sleep(1)
# Quantity: 2
driver.find_element(By.ID, "number-00000010-acc")
driver.find_element(By.XPATH, "//input[@type='number']").send_keys("2")
time.sleep(1)

# Delivery day 01/23/2023
driver.find_element(By.ID, "date-00000012-acc")
driver.find_element(By.XPATH, "//*[@data-type='date' and @data-role='i123-input']").send_keys("01\t23\t2023")
# driver.find_element(By.XPATH, "//div[@role='application']").click
time.sleep(1)
# driver.find_element(By.XPATH, "//div[@data-day='23']").click()
# time.sleep(1)

# Street address (line1, line 2)
driver.find_element(By.ID, "address-00000014-acc")
driver.find_element(By.XPATH, "//input[@placeholder='Street Address']").send_keys("123 E Roosevelt Rd")
driver.find_element(By.XPATH, "//input[@placeholder='Street Address Line 2']").send_keys("Apt 25")
time.sleep(1)

# City, Region, Zip
driver.find_element(By.XPATH, "//input[@placeholder='City']").send_keys("Chicago")
driver.find_element(By.XPATH, "//input[@placeholder='Region']").send_keys("IL")
driver.find_element(By.XPATH, "//input[@placeholder='Postal / Zip Code']").send_keys("60148")
time.sleep(1)

# Country
country = driver.find_element(By.XPATH, "//input[@placeholder='Country']")
country.send_keys("United States")
time.sleep(2)
country.send_keys("\n")
time.sleep(2)

# Dropdown: Choice2
driver.find_element(By.ID, "dropdown-00000016-acc")
driver.find_element(By.XPATH, "//div[@data-type='dropdown']//option[@value='Choice2']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@value='Choice2']").click()
time.sleep(2)

# Multiple choice: Choice 2
driver.find_element(By.ID, "checkbox-00000018-acc")
driver.find_element(By.XPATH, "//label[@for='00000018_1']").click()
time.sleep(2)

# I'm not a robot
driver.find_element(By.ID, "captcha-00000004-acc")
time.sleep(4)

# Submit order
# driver.find_element(By.XPATH, "//*[@data-role='submit']").send_keys("\n")
driver.find_element(By.XPATH, "//button[@type='submit']").submit()
time.sleep(3)

# New window ('Thank you')
# driver.find_element(By.ID, "id123-thankyou")

driver.close()

# multiple choice checkbox: Choice 1
# checkbox = driver.find_element(By.ID, "checkbox-00000018-0")
# actions = ActionChains(driver)
# actions.move_to_element(checkbox).perform()
# checkbox.click()
