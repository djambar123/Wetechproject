from Web.Pages.UpLoadPage import UpLoadPage
from Web.Base.SetUp import SetUp
import pytest
from Web.Locators.UploadLocators import UploadLocators
import allure


@pytest.mark.usefixtures('setUp')
@pytest.mark.parametrize("details",[True])

class TestUpLoad(SetUp):


    def test_upload_text(self):
        driver = self.driver
        upload = UpLoadPage(driver)
        upload.enterText("Have a nice day")
        upload.share()
        # upload.validation(driver,UploadLocators.when_upload,"just now")



    def test_upload_image(self):
        driver = self.driver
        upload = UpLoadPage(driver)
        upload.image_selection()
        upload.share()
        # upload.validation(driver,UploadLocators.when_upload,"just now")



    def test_upload_image_with_text(self):
        driver = self.driver
        upload = UpLoadPage(driver)
        upload.image_selection()
        upload.enterText("Today is Monday")
        upload.share()
        # upload.validation(driver,UploadLocators.when_upload,"just now")


    def test_upload_with_link(self):
        driver = self.driver
        link = UpLoadPage(driver)
        link.links_in_post()
        link.share()
        # link.validation(driver,UploadLocators.when_upload,"just now")

