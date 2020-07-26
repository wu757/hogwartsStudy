from appium.webdriver.common import mobileby
from appium.webdriver.common.mobileby import MobileBy

from Appium企业微信实战2.pages.base_page import BasePage
from Appium企业微信实战2.pages.manage_addressbook_page import ManageAddressbook
from Appium企业微信实战2.pages.member_invite_page import MemberInvite

class AddressList(BasePage):

    def goto_member_invite(self):
        self.find_with_scroll("添加成员").click()
        return MemberInvite(self._driver)

    def goto_manage_addressbook(self):
        self.find_and_click((MobileBy.ID,"com.tencent.wework:id/h9u"))
        return ManageAddressbook(self._driver)

    def get_page_source(self):
        return self._driver.page_source