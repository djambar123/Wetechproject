import time
import allure
from allure_commons.types import AttachmentType

from Locators.LoginLocators import LoginLocators
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.account_login = LoginLocators.account_login
        self.email = LoginLocators.email
        self.password = LoginLocators.password
        self.log_button = LoginLocators.log_button

    @allure.step
    def log_into_account(self):
        self.driver.find_element(By.XPATH,self.account_login).click()

    @allure.step
    def enter_email(self, text):
        self.driver.find_element(By.XPATH, self.email).clear()
        self.driver.find_element(By.XPATH,self.email).send_keys(text)

    @allure.step
    def enter_password(self,text):
        self.driver.find_element(By.XPATH, self.password).clear()
        self.driver.find_element(By.XPATH,self.password).send_keys(text)

    @allure.step
    def login_button(self):
        self.driver.find_element(By.XPATH,self.log_button).click()
        time.sleep(2)
        self.driver.refresh()

    def validation(self,driver, locator, massage):
        driver = self.driver
        valid = driver.find_element(By.XPATH, locator).get_attribute("placeholder")

        try:
            assert valid == massage
        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), driver.save_screenshot('login.png'), attachment_type=AttachmentType.PNG)
