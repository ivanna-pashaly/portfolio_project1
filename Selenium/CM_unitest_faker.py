# Cross-browser UnitTest framework script for California Marketing page
# for Chrome, FireFox browser

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from faker import Faker
import unittest

class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


        # Methods in UnitTest should start from "test" keyword
    def test_chrome(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait(driver, 3)
        driver.delete_all_cookies()
        faker_class = Faker()

        # Print link(href) for header message "California Real Estate"
        # Print link(src) for first home image under "About us"
        print(driver.find_element(By.XPATH, "//p[@class='site-title']//*[@rel='home']").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//img[@class='wp-image-55 size-full']").get_attribute("src"))

        # Assert (compare) stored element value with required value
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        # Print website title
        print("Website title is:", driver.title)

        # Find "Send Us a Message" and verify it's present on the web page
        driver.find_element(By.XPATH, "//*[contains(text(),'Send Us a Message')]")

        # Fill out and send the message form
        driver.find_element(By.NAME, "g2-name").clear()
        driver.find_element(By.NAME, 'g2-name').send_keys(faker_class.name())
        time.sleep(2)
        driver.find_element(By.NAME, 'g2-email').clear()
        driver.find_element(By.NAME, 'g2-email').send_keys(faker_class.email())
        time.sleep(2)
        driver.find_element(By.ID, 'contact-form-comment-g2-message').clear()
        driver.find_element(By.ID, 'contact-form-comment-g2-message').send_keys(faker_class.text())
        time.sleep(2)

        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Submit')]"))).send_keys(Keys.PAGE_DOWN)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        # Find and print "type" for "Submit" button
        print(driver.find_element(By.XPATH, "//*[contains(text(),'Submit')]").get_attribute('type'))
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
        time.sleep(5)

        # Find "go back" button (link) and using one of the tags above click it to go back to the Main page
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'go back')]"))).click()
            print("California Real Estate Page is ready!")
            driver.get_screenshot_as_file('ScreenshotCalifornia_page.png')
        except TimeoutException:
            print("Can't find the page")
            driver.get_screenshot_as_file('California_page_loading_error.png')
        time.sleep(5)

        if "California Real Estate – QA at Silicon Valley Real Estate" == driver.title:
            print("Main Page Title is OK")
        else:
            print("Main Page Title is Different")
            driver.save_screenshot("WrongTitleOnTheMainPage.png")

        page = driver.find_element(By.TAG_NAME, 'html')
        page.send_keys(Keys.SPACE)
        page.send_keys(Keys.SPACE)
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-55 size-full"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34 size-full']")))
        page.send_keys(Keys.SPACE)
        page.send_keys(Keys.SPACE)
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56 size-full']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30 size-full']")))
    def test_chrome_1120x550(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
        driver.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait(driver, 3)
        driver.delete_all_cookies()
        faker_class = Faker()

        # Print link(href) for header message "California Real Estate"
        # Print link(src) for first home image under "About us"
        print(driver.find_element(By.XPATH, "//p[@class='site-title']//*[@rel='home']").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//img[@class='wp-image-55 size-full']").get_attribute("src"))

        # Assert (compare) stored element value with required value
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        # Print website title
        print("Website title is:", driver.title)

        # Find "Send Us a Message" and verify it's present on the web page
        driver.find_element(By.XPATH, "//*[contains(text(),'Send Us a Message')]")

        # Fill out and send the message form
        driver.find_element(By.NAME, "g2-name").clear()
        driver.find_element(By.NAME, 'g2-name').send_keys(faker_class.name())
        time.sleep(2)
        driver.find_element(By.NAME, 'g2-email').clear()
        driver.find_element(By.NAME, 'g2-email').send_keys(faker_class.email())
        time.sleep(2)
        driver.find_element(By.ID, 'contact-form-comment-g2-message').clear()
        driver.find_element(By.ID, 'contact-form-comment-g2-message').send_keys(faker_class.text())
        time.sleep(2)

        # "Submit" button
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Submit')]"))).send_keys(
            Keys.PAGE_DOWN)
        # Find and print "type" for "Submit" button
        print(driver.find_element(By.XPATH, "//*[contains(text(),'Submit')]").get_attribute('type'))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
        time.sleep(5)

        # Find "go back" button (link) and using one of the tags above click it to go back to the Main page
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'go back')]"))).click()
            print("California Real Estate Page is ready!")
            driver.get_screenshot_as_file('ScreenshotCalifornia_page.png')
        except TimeoutException:
            print("Can't find an element")
            driver.get_screenshot_as_file('California_page_loading_error.png')
        time.sleep(5)

        if "California Real Estate – QA at Silicon Valley Real Estate" == driver.title:
            print("Main Page Title is OK")
        else:
            print("Main Page Title is Different")
            driver.save_screenshot("WrongTitleOnTheMainPage.png")

        page = driver.find_element(By.TAG_NAME, 'html')
        page.send_keys(Keys.SPACE)
        page.send_keys(Keys.SPACE)
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-55 size-full"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34 size-full']")))
        page.send_keys(Keys.SPACE)
        page.send_keys(Keys.SPACE)
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56 size-full']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30 size-full']")))

    def tearDown(self):
        self.driver.quit()

class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()


        # Methods in UnitTest should start from "test" keyword
    def test_firefox(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait(driver, 5)
        driver.delete_all_cookies()
        faker_class = Faker()

        # Print link(href) for header message "California Real Estate"
        # Print link(src) for first home image under "About us"
        print(driver.find_element(By.XPATH, "//p[@class='site-title']//*[@rel='home']").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//img[@class='wp-image-55 size-full']").get_attribute("src"))

        # Assert (compare) stored element value with required value
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        # Print website title
        print("Website title is:", driver.title)

        # Find "Send Us a Message" and verify it's present on the web page
        driver.find_element(By.XPATH, "//*[contains(text(),'Send Us a Message')]")

        # Fill out and send the message form
        driver.find_element(By.NAME, "g2-name").clear()
        driver.find_element(By.NAME, 'g2-name').send_keys(faker_class.name())
        time.sleep(2)
        driver.find_element(By.NAME, 'g2-email').clear()
        driver.find_element(By.NAME, 'g2-email').send_keys(faker_class.email())
        time.sleep(2)
        driver.find_element(By.ID, 'contact-form-comment-g2-message').clear()
        driver.find_element(By.ID, 'contact-form-comment-g2-message').send_keys(faker_class.text())
        time.sleep(2)

        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Submit')]"))).send_keys(Keys.PAGE_DOWN)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        # Find and print "type" for "Submit" button
        print(driver.find_element(By.XPATH, "//*[contains(text(),'Submit')]").get_attribute('type'))
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
        time.sleep(5)

        # Find "go back" button (link) and using one of the tags above click it to go back to the Main page
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'go back')]"))).click()
            print("California Real Estate Page is ready!")
            driver.get_screenshot_as_file('ScreenshotCalifornia_page.png')
        except TimeoutException:
            print("Can't find the page")
            driver.get_screenshot_as_file('California_page_loading_error.png')
        time.sleep(5)

        if "California Real Estate – QA at Silicon Valley Real Estate" == driver.title:
            print("Main Page Title is OK")
        else:
            print("Main Page Title is Different")
            driver.save_screenshot("WrongTitleOnTheMainPage.png")

        page = driver.find_element(By.TAG_NAME, 'html')
        page.send_keys(Keys.SPACE)
        page.send_keys(Keys.SPACE)
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-55 size-full"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34 size-full']")))
        page.send_keys(Keys.SPACE)
        page.send_keys(Keys.SPACE)
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56 size-full']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30 size-full']")))

    def test_firefox_1250x850(self):
        driver = self.driver
        driver.set_window_size(1250, 850)
        driver.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait(driver, 5)
        driver.delete_all_cookies()
        faker_class = Faker()

        # Print link(href) for header message "California Real Estate"
        # Print link(src) for first home image under "About us"
        print(driver.find_element(By.XPATH, "//p[@class='site-title']//*[@rel='home']").get_attribute("href"))
        print(driver.find_element(By.XPATH, "//img[@class='wp-image-55 size-full']").get_attribute("src"))

        # Assert (compare) stored element value with required value
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        # Print website title
        print("Website title is:", driver.title)

        # Find "Send Us a Message" and verify it's present on the web page
        driver.find_element(By.ID, "contact-form-comment-g2-message")

        # Fill out and send the message form
        driver.find_element(By.NAME, "g2-name").clear()
        driver.find_element(By.NAME, 'g2-name').send_keys(faker_class.name())
        time.sleep(2)
        driver.find_element(By.NAME, 'g2-email').clear()
        driver.find_element(By.NAME, 'g2-email').send_keys(faker_class.email())
        time.sleep(2)
        driver.find_element(By.ID, 'contact-form-comment-g2-message').clear()
        driver.find_element(By.ID, 'contact-form-comment-g2-message').send_keys(faker_class.text())
        time.sleep(2)

        # "Submit" button
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Submit')]"))).send_keys(
            Keys.PAGE_DOWN)
        # Find and print "type" for "Submit" button
        print(driver.find_element(By.XPATH, "//*[contains(text(),'Submit')]").get_attribute('type'))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
        time.sleep(5)

        # Find "go back" button (link) and using one of the tags above click it to go back to the Main page
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'go back')]"))).click()
            print("California Real Estate Page is ready!")
            driver.get_screenshot_as_file('ScreenshotCalifornia_page.png')
        except TimeoutException:
            print("Can't find an element")
            driver.get_screenshot_as_file('California_page_loading_error.png')
        time.sleep(5)

        if "California Real Estate – QA at Silicon Valley Real Estate" == driver.title:
            print("Main Page Title is OK")
        else:
            print("Main Page Title is Different")
            driver.save_screenshot("WrongTitleOnTheMainPage.png")

        page = driver.find_element(By.TAG_NAME, 'html')
        page.send_keys(Keys.SPACE)
        page.send_keys(Keys.SPACE)
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-55 size-full"]')))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34 size-full']")))
        page.send_keys(Keys.SPACE)
        page.send_keys(Keys.SPACE)
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56 size-full']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30 size-full']")))

    def tearDown(self):
        self.driver.quit()
