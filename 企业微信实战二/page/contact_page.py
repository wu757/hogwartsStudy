from selenium.webdriver.common.by import By

from 企业微信实战二.page.base_page import BasePage


class Contact(BasePage):

    def get_member(self):
        """
        获取成员列表
        :return:
        """
        elements = self.finds(By.CSS_SELECTOR,
                              ".member_colRight_memberTable_td:nth-child(2)")
        name_list = [element.get_attribute("title") for element in elements]

        return name_list
