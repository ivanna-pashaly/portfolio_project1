import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from faker import Faker
from selenium.webdriver.common.action_chains import ActionChains

faker_class = Faker()
class ChromeQuiz(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_chrome_quiz(self):
        driver = self.driver
        url_quiz = "https://form.123formbuilder.com/5012206"
        driver.get(url_quiz)
        driver.delete_all_cookies()
        time.sleep(2)

        # URL verification
        url_quiz = "https://form.123formbuilder.com/5012206"
        assert driver.current_url == url_quiz
        current_url = driver.current_url
        if current_url == url_quiz:
            print("Current URL is: ", driver.current_url)
        else:
            print("Current URL is different than Expected URL", driver.current_url)
        time.sleep(3)

        # Title verification
        if "Online Quiz" in driver.title:
            print("Current page title is:", driver.title)
        else:
            print("'Online Quiz' is not in", driver.title)
            driver.get_screenshot_as_file('onlineQuiz_page.png')
        time.sleep(3)

        # Page verification
        driver.find_element(By.XPATH, "//h1[contains(text(),'Online Quiz')]")
        driver.find_element(By.XPATH, "//p[contains(text(),'Please answer the Online Quiz below. You will rece')]")
        time.sleep(3)

        # Radio button
        driver.find_element(By.ID, "radio-00000008-acc")
        driver.find_element(By.ID, "00000008_0").click()
        time.sleep(3)

        # Longest river
        driver.find_element(By.ID, "radio-0000000a-acc")
        driver.find_element(By.ID, "0000000a_0").click()
        time.sleep(2)

        # Which of the following inventions occured in the 17th century?
        driver.find_element(By.ID, "checkbox-0000000c-acc")
        driver.find_element(By.ID, "checkbox-0000000c-0").click()
        driver.find_element(By.ID, "checkbox-0000000c-1").click()
        time.sleep(3)

        # What name is given to the programs ran by a computer, as opposed to the hardware ?
        driver.find_element(By.ID, "checkbox-0000000e-acc")
        time.sleep(2)
        softCheckBox = driver.find_element(By.ID, "checkbox-0000000e-0")
        actions = ActionChains(driver)
        actions.move_to_element(softCheckBox).perform()
        time.sleep(1)
        actions.click(softCheckBox)
        time.sleep(3)

        # What food group has the highest level of protein?
        driver.find_element(By.ID, "radio-00000010-acc")

        # Refer to "ActionChains" description: https://selenium-python.readthedocs.io/api.html
        meatCheckBox = driver.find_element(By.XPATH,"//label[@id='radio-000000102']")
        actions = ActionChains(driver)
        actions.move_to_element(meatCheckBox).perform()
        time.sleep(1)
        actions.click(meatCheckBox)
        time.sleep(3)

        # Your email
        driver.find_element(By.ID, "email00000018-acc")
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys(faker_class.email())
        time.sleep(3)

        # Get score
        WebDriverWait(driver, 4)
        try:
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver.save_screenshot('page_loading_error.png')

        driver.find_element(By.XPATH, "//button[@type='submit']").submit()

        # New page title verification
        assert "Online Quiz" in driver.title
        print("New page title is:", driver.title)
        time.sleep(2)

        # Thank you
        driver.find_element(By.XPATH, "//div[@class='selector-off']")
        time.sleep(2)

        driver.back()

        # Title verification
        self.assertIn("Online Quiz", driver.title)
        print("Page has", driver.title + " as Page title")
        time.sleep(3)

    def test_chrome_quiz_1120x550(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
        url_quiz = "https://form.123formbuilder.com/5012206"
        driver.get(url_quiz)
        driver.delete_all_cookies()
        time.sleep(2)

        # URL verification
        url_quiz = "https://form.123formbuilder.com/5012206"
        assert driver.current_url == url_quiz
        current_url = driver.current_url
        if current_url == url_quiz:
            print("Current URL is: ", driver.current_url)
        else:
            print("Current URL is different than Expected URL", driver.current_url)
        time.sleep(3)

        # Title verification
        if "Online Quiz" in driver.title:
            print("Current page title is:", driver.title)
        else:
            print("'Online Quiz' is not in", driver.title)
            driver.get_screenshot_as_file('onlineQuiz_page.png')
        time.sleep(3)

        # Page verification
        driver.find_element(By.XPATH, "//h1[contains(text(),'Online Quiz')]")
        driver.find_element(By.XPATH, "//p[contains(text(),'Please answer the Online Quiz below. You will rece')]")
        time.sleep(3)

        # Radio button
        driver.find_element(By.ID, "radio-00000008-acc")
        driver.find_element(By.ID, "00000008_0").click()
        time.sleep(3)

        # Longest river
        driver.find_element(By.ID, "radio-0000000a-acc")
        driver.find_element(By.ID, "0000000a_0").click()
        time.sleep(2)

        # Which of the following inventions occured in the 17th century?
        driver.find_element(By.ID, "checkbox-0000000c-acc")

        inventionCheckBox = driver.find_element(By.ID, "checkbox-0000000c-0")
        actions = ActionChains(driver)
        actions.move_to_element(inventionCheckBox).perform()
        time.sleep(1)
        actions.click(inventionCheckBox)
        time.sleep(3)
        # driver.find_element(By.ID, "checkbox-0000000c-0").click()
        invention1CheckBox = driver.find_element(By.ID, "checkbox-0000000c-1")
        actions = ActionChains(driver)
        actions.move_to_element(invention1CheckBox).perform()
        time.sleep(1)
        actions.click(invention1CheckBox)
        # driver.find_element(By.ID, "checkbox-0000000c-1").click()
        time.sleep(3)

        # What name is given to the programs ran by a computer, as opposed to the hardware ?
        driver.find_element(By.ID, "checkbox-0000000e-acc")
        time.sleep(2)
        softCheckBox = driver.find_element(By.ID, "checkbox-0000000e-0")
        actions = ActionChains(driver)
        actions.move_to_element(softCheckBox).perform()
        time.sleep(1)
        actions.click(softCheckBox)
        time.sleep(3)

        # What food group has the highest level of protein?
        driver.find_element(By.ID, "radio-00000010-acc")

        # Refer to "ActionChains" description: https://selenium-python.readthedocs.io/api.html
        meatCheckBox = driver.find_element(By.XPATH,"//label[@id='radio-000000102']")
        actions = ActionChains(driver)
        actions.move_to_element(meatCheckBox).perform()
        time.sleep(1)
        actions.click(meatCheckBox)
        time.sleep(3)

        # Your email
        driver.find_element(By.ID, "email00000018-acc")
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys(faker_class.email())
        time.sleep(3)

        # Get score
        WebDriverWait(driver, 4)
        try:
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver.save_screenshot('page_loading_error.png')

        driver.find_element(By.XPATH, "//button[@type='submit']").submit()

        # New page title verification
        assert "Online Quiz" in driver.title
        print("New page title is:", driver.title)
        time.sleep(2)

        # Thank you
        driver.find_element(By.XPATH, "//div[@class='selector-off']")
        time.sleep(2)

        driver.back()

        # Title verification
        self.assertIn("Online Quiz", driver.title)
        print("Page has", driver.title + " as Page title")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


class FirefoxQuiz(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_firefox_quiz(self):
        driver = self.driver
        url_quiz = "https://form.123formbuilder.com/5012206"
        driver.get(url_quiz)
        driver.delete_all_cookies()
        time.sleep(2)

        # URL verification
        url_quiz = "https://form.123formbuilder.com/5012206"
        assert driver.current_url == url_quiz
        current_url = driver.current_url
        if current_url == url_quiz:
            print("Current URL is: ", driver.current_url)
        else:
            print("Current URL is different than Expected URL", driver.current_url)
        time.sleep(3)

        # Title verification
        if "Online Quiz" in driver.title:
            print("Current page title is:", driver.title)
        else:
            print("'Online Quiz' is not in", driver.title)
            driver.get_screenshot_as_file('onlineQuiz_page.png')
        time.sleep(3)

        # Page verification
        driver.find_element(By.XPATH, "//h1[contains(text(),'Online Quiz')]")
        driver.find_element(By.XPATH, "//p[contains(text(),'Please answer the Online Quiz below. You will rece')]")
        time.sleep(3)

        # Radio button
        driver.find_element(By.ID, "radio-00000008-acc")
        driver.find_element(By.ID, "00000008_0").click()
        time.sleep(3)

        # Longest river
        driver.find_element(By.ID, "radio-0000000a-acc")
        driver.find_element(By.ID, "0000000a_0").click()
        time.sleep(2)

        # Which of the following inventions occured in the 17th century?
        driver.find_element(By.ID, "checkbox-0000000c-acc")
        driver.find_element(By.ID, "checkbox-0000000c-0").click()
        driver.find_element(By.ID, "checkbox-0000000c-1").click()
        time.sleep(3)

        # What name is given to the programs ran by a computer, as opposed to the hardware ?
        driver.find_element(By.ID, "checkbox-0000000e-acc")
        time.sleep(2)
        softCheckBox = driver.find_element(By.ID, "checkbox-0000000e-0")
        actions = ActionChains(driver)
        actions.move_to_element(softCheckBox).perform()
        time.sleep(1)
        actions.click(softCheckBox)
        time.sleep(3)

        # What food group has the highest level of protein?
        driver.find_element(By.ID, "radio-00000010-acc")

        # Refer to "ActionChains" description: https://selenium-python.readthedocs.io/api.html
        meatCheckBox = driver.find_element(By.XPATH,"//label[@id='radio-000000102']")
        actions = ActionChains(driver)
        actions.move_to_element(meatCheckBox).perform()
        time.sleep(1)
        actions.click(meatCheckBox)
        time.sleep(3)

        # Your email
        driver.find_element(By.ID, "email00000018-acc")
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys(faker_class.email())
        time.sleep(3)

        # Get score
        WebDriverWait(driver, 4)
        try:
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver.save_screenshot('page_loading_error.png')

        driver.find_element(By.XPATH, "//button[@type='submit']").submit()

        # New page title verification
        assert "Online Quiz" in driver.title
        print("New page title is:", driver.title)
        time.sleep(2)

        # Thank you
        driver.find_element(By.XPATH, "//div[@class='selector-off']")
        time.sleep(2)

        driver.back()

        # Title verification
        self.assertIn("Online Quiz", driver.title)
        print("Page has", driver.title + " as Page title")
        time.sleep(3)

    def test_firefox_quiz_1120x550(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
        url_quiz = "https://form.123formbuilder.com/5012206"
        driver.get(url_quiz)
        driver.delete_all_cookies()
        time.sleep(2)

        # URL verification
        url_quiz = "https://form.123formbuilder.com/5012206"
        assert driver.current_url == url_quiz
        current_url = driver.current_url
        if current_url == url_quiz:
            print("Current URL is: ", driver.current_url)
        else:
            print("Current URL is different than Expected URL", driver.current_url)
        time.sleep(3)

        # Title verification
        if "Online Quiz" in driver.title:
            print("Current page title is:", driver.title)
        else:
            print("'Online Quiz' is not in", driver.title)
            driver.get_screenshot_as_file('onlineQuiz_page.png')
        time.sleep(3)

        # Page verification
        driver.find_element(By.XPATH, "//h1[contains(text(),'Online Quiz')]")
        driver.find_element(By.XPATH, "//p[contains(text(),'Please answer the Online Quiz below. You will rece')]")
        time.sleep(3)

        # Radio button
        driver.find_element(By.ID, "radio-00000008-acc")
        driver.find_element(By.ID, "00000008_0").click()
        time.sleep(3)

        # Longest river
        driver.find_element(By.ID, "radio-0000000a-acc")
        driver.find_element(By.ID, "0000000a_0").click()
        time.sleep(2)

        # Which of the following inventions occured in the 17th century?
        driver.find_element(By.ID, "checkbox-0000000c-acc")

        inventionCheckBox = driver.find_element(By.ID, "checkbox-0000000c-0")
        actions = ActionChains(driver)
        actions.move_to_element(inventionCheckBox).perform()
        time.sleep(1)
        actions.click(inventionCheckBox)
        time.sleep(3)
        # driver.find_element(By.ID, "checkbox-0000000c-0").click()
        invention1CheckBox = driver.find_element(By.ID, "checkbox-0000000c-1")
        actions = ActionChains(driver)
        actions.move_to_element(invention1CheckBox).perform()
        time.sleep(1)
        actions.click(invention1CheckBox)
        # driver.find_element(By.ID, "checkbox-0000000c-1").click()
        time.sleep(3)

        # What name is given to the programs ran by a computer, as opposed to the hardware ?
        driver.find_element(By.ID, "checkbox-0000000e-acc")
        time.sleep(2)
        softCheckBox = driver.find_element(By.ID, "checkbox-0000000e-0")
        actions = ActionChains(driver)
        actions.move_to_element(softCheckBox).perform()
        time.sleep(1)
        actions.click(softCheckBox)
        time.sleep(3)

        # What food group has the highest level of protein?
        driver.find_element(By.ID, "radio-00000010-acc")

        # Refer to "ActionChains" description: https://selenium-python.readthedocs.io/api.html
        meatCheckBox = driver.find_element(By.XPATH,"//label[@id='radio-000000102']")
        actions = ActionChains(driver)
        actions.move_to_element(meatCheckBox).perform()
        time.sleep(1)
        actions.click(meatCheckBox)
        time.sleep(3)

        # Your email
        driver.find_element(By.ID, "email00000018-acc")
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys(faker_class.email())
        time.sleep(3)

        # Get score
        WebDriverWait(driver, 4)
        try:
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver.save_screenshot('page_loading_error.png')

        driver.find_element(By.XPATH, "//button[@type='submit']").submit()

        # New page title verification
        assert "Online Quiz" in driver.title
        print("New page title is:", driver.title)
        time.sleep(2)

        # Thank you
        driver.find_element(By.XPATH, "//div[@class='selector-off']")
        time.sleep(2)

        driver.back()

        # Title verification
        self.assertIn("Online Quiz", driver.title)
        print("Page has", driver.title + " as Page title")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()