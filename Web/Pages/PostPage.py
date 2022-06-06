import allure
from allure_commons.types import AttachmentType

from Web.Locators.PostLocators import PostLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui

class PostPage:

    def __init__(self,driver):
        self.driver = driver
        self.like_button = PostLocators.like_button
        self.input_comment = PostLocators.input_comment
        self.send_button = PostLocators.send_button
        self.see_comment_button = PostLocators.see_comment_button
        self.exit_comment = PostLocators.exit_comment
        self.edit_button = PostLocators.edit_button
        self.input_in_edit = PostLocators.input_in_edit
        self.save_button = PostLocators.save_button
        self.delete_button = PostLocators.delete_button

    @allure.step
    def post_unlike_or_like(self):
        WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH,self.like_button)))
        self.driver.find_element(By.XPATH,self.like_button).click()
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.XPATH,self.like_button)))

    @allure.step
    def comment_on_post(self,text):
        WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH,self.input_comment)))
        self.driver.find_element(By.XPATH, self.input_comment).clear()
        self.driver.find_element(By.XPATH,self.input_comment).send_keys(text)
        self.driver.find_element(By.XPATH,self.send_button).click()
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.XPATH,self.send_button)))

    @allure.step
    def see_comment(self):
        WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH,self.see_comment_button)))
        self.driver.find_element(By.XPATH,self.see_comment_button).click()
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.XPATH,self.see_comment_button)))
        self.driver.find_element(By.XPATH,self.exit_comment).click()

    @allure.step
    def edit_post(self,text):
        WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH,self.edit_button)))
        self.driver.find_element(By.XPATH,self.edit_button).click()
        self.driver.find_element(By.XPATH,self.input_in_edit).send_keys(text)
        WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH,self.save_button)))
        pyautogui.press('enter')

    @allure.step
    def delete_post(self):
        WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH,self.delete_button)))
        self.driver.find_element(By.XPATH,self.delete_button).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.delete_button)))

    def validation(self, driver, locator, massage):
        driver = self.driver
        valid = driver.find_element(By.XPATH, locator).get_attribute("textContent")

        try:
            assert valid == massage
        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), driver.save_screenshot('post.png'), attachment_type=AttachmentType.PNG)
