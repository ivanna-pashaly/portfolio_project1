import time
from selenium import webdriver
import requests
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException as WDE
import unittest
import random

from selenium.webdriver.common.action_chains import ActionChains

class Chrome_Bread(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


        # Methods in UnitTest should start from "test" keyword
    def test_chrome(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org/')
        wait = WebDriverWait(driver, 3)
        driver.delete_all_cookies()

        # URL verification
        wiki_url = "https://www.wikipedia.org/"
        assert wiki_url == driver.current_url
        print(wiki_url)

        if wiki_url != driver.current_url:
            print("Current 'Wikipedia' URL is different than expected URL", driver.current_url)
        else:
            print("Current 'Wikipedia' URL is : ", driver.current_url)

        print("Wikipedia Url has", requests.get("https://www.wikipedia.org").status_code, "as status Code")


        # Title verification
        assert "Wikipedia" in driver.title
        print("Page title is:", driver.title)
        time.sleep(2)

        if "Wikipedia" not in driver.title:
            raise Exception("Unable to load Wikipedia page!")


        # Verification of the page
        print(driver.find_element(By.XPATH, "//img[@class='central-featured-logo']").get_attribute("src"))
        time.sleep(3)

        driver.find_element(By.XPATH, "//span[@class='central-textlogo__image sprite svg-Wikipedia_wordmark']")
        driver.find_element(By.XPATH, "//strong[contains(text(),'The Free Encyclopedia')]")
        time.sleep(2)

        # API response Status code check
        codeWiki = requests.get("https://www.wikipedia.org").status_code
        if codeWiki == 200:
            print("Wikipedia Url has correct", requests.get("https://www.wikipedia.org").status_code, " as status Code")
        else:
            print("Wikipedia Url has incorrect", requests.get("https://www.wikipedia.org").status_code,
                  "as status Code")

        # Search button
        search = driver.find_element(By.ID, "searchInput")
        search.clear()
        search.send_keys("Coffee")
        search.submit()
        driver.back()
        driver.implicitly_wait(4)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

        # New ("Coffee") page title verification
        self.assertIn("Coffee - Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")
        if "Coffee" not in driver.title:
            raise Exception("Wikipedia Coffee page Title is wrong!")
        time.sleep(3)

        # Coffee - logo
        wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//caption[@class='infobox-title fn ingredient']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='image']//img[@alt='Latte and dark coffee.jpg']")))

        # Image
        try:
            wait.until( EC.presence_of_element_located((By.XPATH, "//a[@href='/wiki/File:Latte_and_dark_coffee.jpg']")))
            print("File:Latte and dark coffee.jpg - Wikipedia is ready!")
            driver.get_screenshot_as_file('coffee.png')
        except TimeoutException:
            print("Can't find Element by href='/wiki/File:Latte_and_dark_coffee.jpg")
            driver.get_screenshot_as_file('coffee_page_loading_error.png')
        driver.implicitly_wait(10)

        driver.find_element(By.XPATH, "//a[@class='image']//img[@alt='Latte and dark coffee.jpg']").click()
        time.sleep(4)

        # Title verification (new page)
        if "Latte and dark coffee - Coffee - Wikipedia" in driver.title:
            print("Page has", driver.title + " as Page title")
        else:
            print("Current page is different")
            driver.get_screenshot_as_file('coffee1.png')
        time.sleep(2)

        # Button " > " and " X"
        driver.find_element(By.XPATH, "//button[@title='Show next image']")
        driver.find_element(By.XPATH, "//button[@class='mw-mmv-close']").click()
        time.sleep(2)

        # Title verification
        assert "Coffee - Wikipedia" in driver.title
        print("Current title is", driver.title)

        # First paragraph
        driver.find_element(By.XPATH, "//*[contains(text(), ' is a drink prepared from roasted')]")
        time.sleep(1)

        # Go  on mane page
        driver.find_element(By.XPATH, "//*[@class='mw-logo']").click()

        # Title verification on the main page
        if "Wikipedia, the free encyclopedia" not in driver.title:
            raise Exception("Wikipedia Coffee page Title is wrong!")
        driver.get_screenshot_as_file('coffee2.png')
        print("Page title is:", driver.title)

        # Correct page verification
        driver.find_element(By.ID, "Welcome_to_Wikipedia")
        print("Enjoy your morning Coffee!")

    def tearDown(self):
        self.driver.quit()

class Firefox_Bread(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()


        # Methods in UnitTest should start from "test" keyword
    def test_firefox(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org/')
        wait = WebDriverWait(driver, 3)
        driver.delete_all_cookies()

        # URL verification
        wiki_url = "https://www.wikipedia.org/"
        assert wiki_url == driver.current_url
        print(wiki_url)

        if wiki_url != driver.current_url:
            print("Current 'Wikipedia' URL is different than expected URL", driver.current_url)
        else:
            print("Current 'Wikipedia' URL is : ", driver.current_url)

        print("Wikipedia Url has", requests.get("https://www.wikipedia.org").status_code, "as status Code")


        # Title verification
        assert "Wikipedia" in driver.title
        print("Page title is:", driver.title)
        time.sleep(2)

        if "Wikipedia" not in driver.title:
            raise Exception("Unable to load Wikipedia page!")


        # Verification of the page
        print(driver.find_element(By.XPATH, "//img[@class='central-featured-logo']").get_attribute("src"))
        time.sleep(3)

        driver.find_element(By.XPATH, "//span[@class='central-textlogo__image sprite svg-Wikipedia_wordmark']")
        driver.find_element(By.XPATH, "//strong[contains(text(),'The Free Encyclopedia')]")
        time.sleep(2)

        # API response Status code check
        codeWiki = requests.get("https://www.wikipedia.org").status_code
        if codeWiki == 200:
            print("Wikipedia Url has correct", requests.get("https://www.wikipedia.org").status_code, " as status Code")
        else:
            print("Wikipedia Url has incorrect", requests.get("https://www.wikipedia.org").status_code,
                  "as status Code")

        # Search button
        search = driver.find_element(By.ID, "searchInput")
        search.clear()
        search.send_keys("Coffee")
        search.submit()
        driver.back()
        driver.implicitly_wait(4)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

        # New ("Coffee") page title verification
        self.assertIn("Coffee - Wikipedia", driver.title)
        print("Page has", driver.title + " as Page title")
        if "Coffee" not in driver.title:
            raise Exception("Wikipedia Coffee page Title is wrong!")
        time.sleep(3)

        # Coffee - logo
        wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//caption[@class='infobox-title fn ingredient']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='image']//img[@alt='Latte and dark coffee.jpg']")))

        # Image
        try:
            wait.until( EC.presence_of_element_located((By.XPATH, "//a[@href='/wiki/File:Latte_and_dark_coffee.jpg']")))
            print("File:Latte and dark coffee.jpg - Wikipedia is ready!")
            driver.get_screenshot_as_file('coffee.png')
        except TimeoutException:
            print("Can't find Element by href='/wiki/File:Latte_and_dark_coffee.jpg")
            driver.get_screenshot_as_file('coffee_page_loading_error.png')
        driver.implicitly_wait(10)

        driver.find_element(By.XPATH, "//a[@class='image']//img[@alt='Latte and dark coffee.jpg']").click()
        time.sleep(4)

        # Title verification (new page)
        if "Latte and dark coffee - Coffee - Wikipedia" in driver.title:
            print("Page has", driver.title + " as Page title")
        else:
            print("Current page is different")
            driver.get_screenshot_as_file('coffee1.png')
        time.sleep(2)

        # Button " > " and " X"
        driver.find_element(By.XPATH, "//button[@title='Show next image']")
        driver.find_element(By.XPATH, "//button[@class='mw-mmv-close']").click()
        time.sleep(2)

        # Title verification
        assert "Coffee - Wikipedia" in driver.title
        print("Current title is", driver.title)

        # First paragraph
        driver.find_element(By.XPATH, "//*[contains(text(), ' is a drink prepared from roasted')]")
        time.sleep(1)

        # Go  on mane page
        driver.find_element(By.XPATH, "//*[@class='mw-logo']").click()

        # Title verification on the main page
        if "Wikipedia, the free encyclopedia" not in driver.title:
            raise Exception("Wikipedia Coffee page Title is wrong!")
        driver.get_screenshot_as_file('coffee2.png')
        print("Page title is:", driver.title)

        # Correct page verification
        driver.find_element(By.ID, "Welcome_to_Wikipedia")
        print("Enjoy your morning Coffee!")

    def tearDown(self):
        self.driver.quit()