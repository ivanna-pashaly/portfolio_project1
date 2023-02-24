from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import random
import unittest
import time
from selenium.webdriver.common.keys import Keys


# driver sleep from 2 to 3 seconds
def delay():
    time.sleep(random.randint(2, 3))

class ChromeSearch(unittest.TestCase):
    def setUp(self):
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()

    def test_wordpress_chrome(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com/')

        wait = WebDriverWait(driver, 5)
        # Do assertion for driver title
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("Page title in Chrome is:", driver.title)
        wait = WebDriverWait(driver, 5)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        time.sleep(2)

        driver.find_element(By.ID, "g2 - name").clear()
        time.sleep(2)
        driver.find_element(By.ID, 'g2-email').clear()
        time.sleep(2)
        driver.find_element(By.NAME, 'g2-message').clear()
        time.sleep(2)

        driver.find_element(By.ID, "g2 - name").send_keys("Ana Green")

        driver.find_element(By.ID, 'g2-email').send_keys('dog3@gmail.com')

        driver.find_element(By.NAME, 'g2-message').send_keys('Hi. How are you!')

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        delay()

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("Page title in Chrome is:", driver.title)

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Go back')]")))
            print("Go back button is visible")
        except TimeoutException:
            print("Loading took too much time!")

        driver.find_element(By.XPATH, "//a[contains(text(), 'Go back')]").click()
        delay()

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

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("Page has", driver.title + ", as Page title")


    def test_wordpress_chrome_1120x550(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
        driver.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait(driver, 3)

        # Do assertion for driver title
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("Page title in Chrome is:", driver.title)
        wait = WebDriverWait(driver, 3)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        time.sleep(2)

        driver.find_element(By.ID, "g2 - name").clear()
        time.sleep(2)
        driver.find_element(By.ID, 'g2-email').clear()
        time.sleep(2)
        driver.find_element(By.NAME, 'g2-message').clear()
        time.sleep(2)

        driver.find_element(By.ID, "g2 - name").send_keys("Ana Green")

        driver.find_element(By.ID, 'g2-email').send_keys('dog3@gmail.com')

        driver.find_element(By.NAME, 'g2-message').send_keys('Hi. How are you!')

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        delay()

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("Page title in Chrome is:", driver.title)

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Go back')]")))
            print("Go back button is visible")
        except TimeoutException:
            print("Loading took too much time!")

        driver.find_element(By.XPATH, "//a[contains(text(), 'Go back')]").click()
        delay()

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

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("Page has", driver.title + ", as Page title")


    def tearDown(self):
        self.driver.quit()

class FirefoxSearch(unittest.TestCase):

    def setUp(self):
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()

     # As per unittest module, individual test should start with test_
    def test_wordpress_firefox(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com/')

        wait = WebDriverWait(driver, 5)
        # Do assertion for driver title
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("Page title in Chrome is:", driver.title)
        wait = WebDriverWait(driver, 5)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        delay()

        driver.find_element(By.ID, "g2 - name").clear()
        time.sleep(2)
        driver.find_element(By.ID, 'g2-email').clear()
        time.sleep(2)
        driver.find_element(By.NAME, 'g2-message').clear()
        time.sleep(2)

        driver.find_element(By.ID, "g2 - name").send_keys("Ana Green")

        driver.find_element(By.ID, 'g2-email').send_keys('dog3@gmail.com')

        driver.find_element(By.NAME, 'g2-message').send_keys('Hi. How are you!')

        wait.until(EC.visibility_of_element_located((By.ID, 'contact-form-comment-g2-message')))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        delay()

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("Page title in Chrome is:", driver.title)

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Go back')]")))
            print("Go back button is visible")
        except TimeoutException:
            print("Loading took too much time!")

        driver.find_element(By.XPATH, "//a[contains(text(), 'Go back')]").click()
        delay()

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

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("Page has", driver.title + ", as Page title")

    def test_word_firefox_1250x850(self):
        driver = self.driver
        driver.set_window_size(1250, 850)
        driver.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait(driver, 5)

        # Do assertion for driver title
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("Page title in Chrome is:", driver.title)
        wait = WebDriverWait(driver, 5)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        time.sleep(2)

        driver.find_element(By.ID, "g2 - name").clear()
        time.sleep(2)
        driver.find_element(By.ID, 'g2-email').clear()
        time.sleep(2)
        driver.find_element(By.NAME, 'g2-message').clear()
        time.sleep(2)

        driver.find_element(By.ID, "g2 - name").send_keys("Ana Green")

        driver.find_element(By.ID, 'g2-email').send_keys('dog3@gmail.com')

        driver.find_element(By.NAME, 'g2-message').send_keys('Hi. How are you!')

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        delay()

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("Page title in Chrome is:", driver.title)

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Go back')]")))
            print("Go back button is visible")
        except TimeoutException:
            print("Loading took too much time!")

        driver.find_element(By.XPATH, "//a[contains(text(), 'Go back')]").click()
        delay()

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

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("Page has", driver.title + ", as Page title")

    def tearDown(self):
        self.driver.quit()