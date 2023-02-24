from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()

# wait max 5 sec for page loading, then show "Load Error"
# implicitly_wait() is using for all other browsers
driver.implicitly_wait(5)

# this method is depreciated in Selenium4
# driver.find_element_by_name("q").send_keys("abc")
driver.find_element(By.NAME, "q").send_keys("abc")

print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))  # Google logo image
# Same code, but with XPath locator
# print(driver.find_element(By.ID, 'hplogo').get_attribute("src"))  # Google logo image
print(driver.find_element(By.XPATH, '//*[@alt="Seasonal Holidays 2022"]').get_attribute("src"))  # Google logo image

print(driver.find_element(By.NAME, "btnK").get_attribute("value"))  # Google button value
print(driver.find_element(By.NAME, "btnI").get_attribute("value"))  # Google second button value

# Find element value, then store this value to variable "btnk"
btnk = driver.find_element(By.NAME, "btnK").get_attribute("value")

# Assert (compare) stored element value with required value
assert btnk == "Google Search"

# Same element verification for "Google Search" button
if btnk is not None:
    print("Google Search button is OK")
else:
    print("NO Google Search button")

driver.find_element(By.NAME, "btnK").click()
driver.back()
time.sleep(3)
driver.find_element(By.NAME, "q").send_keys("abc")
# or just hit Enter on the Keyboard, code is below:
driver.find_element(By.NAME, "btnK").submit()

# Find and click on the ABC link
driver.find_element(By.PARTIAL_LINK_TEXT, "ABC Home Page").click()
time.sleep(2)
assert "ABC Home Page - ABC.com" in driver.title
print("ABC Page Title is: ", driver.title)
if "ABC Home Page - ABC.com" not in driver.title:
    raise Exception("Title for ABC page is wrong!")

# wait max 5 sec for page loading, then show "Load Error"
# set_page_load_timeout() is using for Chrome and FireFox mostly
driver.set_page_load_timeout(5)
driver.find_element(By.LINK_TEXT, "Browse").click()
time.sleep(3)
driver.find_element(By.XPATH, "//img[@alt='search for a show']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@class='Input Searchlist__input']").send_keys('American Idol')
driver.find_element(By.XPATH, "//img[@alt='search for a show']").submit()
driver.find_element(By.XPATH, "//span[contains(text(),'American Idol')]").click()
time.sleep(4)
assert "Watch American Idol TV Show - ABC.com" in driver.title
driver.find_element(By.XPATH, '//*[@title="American Idol"]')
print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("title"))
print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("src"))

# Find element value, then store this value to variable "dancePageLogo"
IdolPageLogo = driver.find_element(By.XPATH, '//*[@title="American Idol"]').get_attribute("title")

# Assert (compare) stored element value with required value
assert IdolPageLogo == "American Idol"
assert IdolPageLogo in driver.page_source

IdolShowURL = "https://abc.com/shows/american-idol"
assert IdolShowURL == driver.current_url
if IdolShowURL != driver.current_url:
    print("Current American Idol URL is different and it is: ", driver.current_url)
else:
    print("Current Dance Show URL is OK: ", driver.current_url)

# Same element verification for "American Idol Page Logo"
if IdolPageLogo:
    print("American Idol Show Page Logo is OK")
else:
    print("NO American Idol Show Page Logo")

page = driver.find_element(By.TAG_NAME, 'html')
page.send_keys(Keys.SPACE)
page.send_keys(Keys.SPACE)
page.send_keys(Keys.SPACE)
time.sleep(3)

driver.find_element(By.LINK_TEXT, 'AUDITION NOW').click()
time.sleep(3)

driver.back()

# quit from browser
driver.quit()
