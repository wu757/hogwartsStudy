import time

from 企业微信实战二.page.add_member_page import AddMember
from 企业微信实战二.page.main_page import MainPage


class TestAddMember():
    def setup_class(self):
        self.main = MainPage()

    def setup(self):
        self.main.goto_main_page()

    def test_add_member(self):
        assert AddMember.name in self.main.goto_add_member().add_member().get_member()

    def test_del_member(self):
        assert AddMember.name not in self.main.goto_contact().del_member(AddMember.name).get_member()

    def teardown_class(self):
        time.sleep(10)
        self.main.quit()
