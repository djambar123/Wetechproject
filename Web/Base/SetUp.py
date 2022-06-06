from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from Web.Pages.LoginPage import LoginPage


class SetUp:

    @pytest.fixture(autouse=True)
    def setUp(self,details):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://wetechsocial.herokuapp.com")

        if details == True:
            account = LoginPage(self.driver)
            account.log_into_account()
            account.enter_email("melakubetty@gmail.com")
            account.enter_password("123456")
            account.login_button()
            self.driver.refresh()

        elif details ==False:
            pass


        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()

