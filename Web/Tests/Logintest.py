from Web.Pages.LoginPage import LoginPage
from Web.Base.SetUp import SetUp
import pytest


@pytest.mark.usefixtures('setup')
@pytest.mark.parametrize("details",[True])

class TestLogin(SetUp):

    def test_account_login(self):
        driver = self.driver
        account = LoginPage(driver)
        account.log_into_account()
        account.enter_email("melakubetty@gmail.com")
        account.enter_password("123456")
        account.login_button()
