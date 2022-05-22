from Pages.PostPage import PostPage
from Base.SetUp import SetUp
import pytest


@pytest.mark.usefixtures('setUp')
@pytest.mark.parametrize("details",[True])

class TestPost(SetUp):

    def test_like_unlike_post(self):
        driver = self.driver
        liking = PostPage(driver)
        liking.post_unlike_or_like()


    def test_comment_on_post_view(self):
        driver = self.driver
        comment = PostPage(driver)
        comment.comment_on_post("You too")
        comment.see_comment()


    def test_post_edit(self):
        driver = self.driver
        ed = PostPage(driver)
        ed.edit_post("New post")


    def test_delete(self):
        driver = self.driver
        delete = PostPage(driver)
        delete.delete_post()
