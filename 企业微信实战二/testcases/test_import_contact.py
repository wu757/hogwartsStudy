import time

from 企业微信实战二.page.main_page import MainPage


class TestImportContact():
    def setup_class(self):
        self.main = MainPage()

    def test_import_contact(self):
        assert "张三" in self.main.goto_import_contact().batch_import().get_member()

    def teardown_class(self):
        time.sleep(10)
        self.main.quit()
