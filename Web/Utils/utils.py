from Web.Pages.RegisterPage import RegisterPage
from Web.Pages.LoginPage import LoginPage



def new_user_defualt(driver):
    user = RegisterPage(driver)
    user.enter_name("Aviva")
    user.enter_last_name("Ayasso")
    user.enter_pic_url("C:/Users/aviva/OneDrive/Pictures/Saved Pictures/log.jpg")
    user.enter_cover_pic_url("C:/Users/aviva/OneDrive/Pictures/Saved Pictures/log.jpg")
    user.enter_email("avivaaayasso0@gmail.com")
    user.enter_country("Israel")
    user.enter_city("Yavne")
    user.enter_password(123456)
    user.enter_password_confirm(123456)
    user.sigh_button()

def login_user(driver):
    user = LoginPage(driver)
    user.log_into_account()
    user.enter_email("avivaaayasso0@gmail.com")
    user.enter_email(123456)
    user.login_button




# def validation(driver,locator, massage):
#     user = RegisterPage(driver)
#     valid = driver.find_element(By.XPATH, locator).get_attribute("validationMessage")
#
#     try:
#         assert valid == massage
#     except Exception as e:
#
#         driver.get_screenshot_as_png()
#         driver.save_screenshot("lklk.png")

