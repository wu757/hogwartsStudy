from selenium.webdriver.common.by import By

from 企业微信实战二.page.add_member_page import AddMember
from 企业微信实战二.page.base_page import BasePage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    """
    首页
    """
    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMember(self.driver)

    def goto_contact(self):
        pass

    def goto_import_contact(self):
        pass