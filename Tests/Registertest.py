from Base.SetUp import SetUp
from Pages.RegisterPage import RegisterPage
from Locators.RegisterLocators import RegisterLocators
import pytest



@pytest.mark.usefixtures('setUp')
@pytest.mark.parametrize("details",[False])
class TestPost(SetUp):


    def test_register_correctly(self):
        driver = self.driver
        user = RegisterPage(driver)
        user.sigh_button()
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
        user.validation(self.driver,RegisterLocators.logout,"What's in your mind Aviva?")

    def test_register_whit_null_user_name(self):
        driver = self.driver
        user = RegisterPage(driver)
        user.enter_name("")
        user.enter_last_name("Ayasso")
        user.enter_pic_url("C:/Users/aviva/OneDrive/Pictures/Saved Pictures/log.jpg")
        user.enter_cover_pic_url("C:/Users/aviva/OneDrive/Pictures/Saved Pictures/log.jpg")
        user.enter_email("avivaaayasso0@gmail.com")
        user.enter_country("Israel")
        user.enter_city("Yavne")
        user.enter_password(123456)
        user.enter_password_confirm(123456)
        user.sigh_button()
        user.validation(driver,RegisterLocators.user_name, "Please fill out this fie.")


