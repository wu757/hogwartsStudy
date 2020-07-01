from selenium.webdriver.common.by import By

from 企业微信实战二.page.add_member_page import AddMember
from 企业微信实战二.page.base_page import BasePage
from 企业微信实战二.page.contact_page import Contact


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    """
    首页
    """

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        return AddMember(self.driver)

    def goto_main_page(self):
        self.find(By.CSS_SELECTOR, "#menu_index > span").click()

    def goto_contact(self):
        self.find(By.CSS_SELECTOR, "#menu_contacts > span").click()
        return Contact(self.driver)

    def goto_import_contact(self):
        self.find(By.CSS_SELECTOR, ".ww_indexImg_Import").click()
        return Contact(self.driver)
