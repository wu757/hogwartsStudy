from appium.webdriver.common.mobileby import MobileBy

from Appium企业微信实战2.pages.add_member_manually_page import AddMemberManually
from Appium企业微信实战2.pages.base_page import BasePage


class MemberInvite(BasePage):

    def goto_add_member_manually(self):
        self.find_and_click((MobileBy.XPATH,"//*[@text='手动输入添加']"))
        return AddMemberManually(self._driver)

    def get_result(self):
        return self.get_toast()