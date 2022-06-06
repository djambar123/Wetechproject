import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Web.Locators.UploadLocators import UploadLocators
import pyautogui
from selenium.webdriver.common.by import By

class UpLoadPage:

    def __init__(self,driver):
        self.driver = driver
        self.text = UploadLocators.text
        self.photo_or_video = UploadLocators.photo_or_video
        self.tag = UploadLocators.tag
        self.location = UploadLocators.location
        self.feelings = UploadLocators.feeling
        self.share_button = UploadLocators.share_button

    @allure.step
    def enterText(self, text):
        WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH,self.text)))
        self.driver.find_element(By.XPATH, self.text).clear()
        self.driver.find_element(By.XPATH, self.text).send_keys(text)
        time.sleep(5)

    @allure.step
    def image_selection(self):
        self.driver.find_element(By.XPATH, self.photo_or_video).click()
        path = r'\\Users\aviva\OneDrive\Pictures\Saved Pictures\IMG_3188.jpg'
        pyautogui.write(path, interval=0.25)
        pyautogui.press('enter')

    @allure.step
    def links_in_post(self):
        self.driver.find_element(By.XPATH,self.tag).click()
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.XPATH,self.tag)))
        self.driver.find_element(By.XPATH,self.location).click()
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.XPATH,self.location)))
        self.driver.find_element(By.XPATH,self.feelings).click()
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.XPATH,self.feelings)))

    @allure.step
    def share(self):
        self.driver.find_element(By.XPATH,self.share_button).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.share_button)))


    def validation(self, driver, locator, massage):
        driver = self.driver
        valid = driver.find_element(By.XPATH, locator).get_attribute("innerText")


        try:
            assert valid == massage
        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), driver.save_screenshot('upp.png'), attachment_type=AttachmentType.PNG)
