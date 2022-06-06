import allure
from allure_commons.types import AttachmentType

from Web.Locators.RegisterLocators import RegisterLocators
from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self,driver):
        self.driver =driver
        self.user_name = RegisterLocators.user_name
        self.user_last_name = RegisterLocators.user_last_name
        self.user_profile_picture = RegisterLocators.user_profile_picture
        self.cover_picture = RegisterLocators.cover_picture
        self.email = RegisterLocators.email
        self.country = RegisterLocators.country
        self.city = RegisterLocators.city
        self.password = RegisterLocators.password
        self.password_confirm = RegisterLocators.password_confirm
        self.sigh_up_button = RegisterLocators.sigh_up_button
        self.box = RegisterLocators.box

    @allure.step
    def enter_name(self,text):
        self.driver.find_element(By.XPATH,self.user_name).send_keys(text)

    @allure.step
    def enter_last_name(self, text):
        self.driver.find_element(By.XPATH,self.user_last_name).send_keys(text)

    @allure.step
    def enter_pic_url(self, text):
        self.driver.find_element(By.XPATH,self.user_profile_picture).send_keys(text)

    @allure.step
    def enter_cover_pic_url(self, text):
        self.driver.find_element(By.XPATH,self.cover_picture).send_keys(text)


    @allure.step
    def enter_email(self, text):
        self.driver.find_element(By.XPATH,self.email).send_keys(text)

    @allure.step
    def enter_country(self, text):
        self.driver.find_element(By.XPATH,self.country).send_keys(text)

    @allure.step
    def enter_city(self, text):
        self.driver.find_element(By.XPATH,self.city).send_keys(text)

    def enter_password(self, text):
        self.driver.find_element(By.XPATH,self.password).send_keys(text)

    @allure.step
    def enter_password_confirm(self, text):
        self.driver.find_element(By.XPATH,self.password_confirm).send_keys(text)

    @allure.step
    def sigh_button(self):
        self.driver.find_element(By.XPATH,self.sigh_up_button).click()




    def validation(self,driver, locator, massage):
        driver = self.driver
        valid = driver.find_element(By.XPATH, locator).get_attribute("validationMessage")

        try:
            assert valid == massage
        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), driver.save_screenshot('ava.png'), attachment_type=AttachmentType.PNG)
