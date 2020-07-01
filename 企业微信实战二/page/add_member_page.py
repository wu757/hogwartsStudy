import random
import time

from selenium.webdriver.common.by import By

from 企业微信实战二.page.base_page import BasePage
from 企业微信实战二.page.contact_page import Contact


class AddMember(BasePage):
    _username = "username"
    name = f"name{round(time.time())}"
    _account = f"account{round(time.time())}"
    _phone = "159%08d" % random.randint(0, 99999999)

    def add_member(self):
        """
        添加成员
        :return:
        """
        self.find(By.ID, self._username).send_keys(self.name)
        self.find(By.ID, "memberAdd_acctid").send_keys(self._account)
        self.find(By.ID, "memberAdd_phone").send_keys(self._phone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return Contact(self.driver)
