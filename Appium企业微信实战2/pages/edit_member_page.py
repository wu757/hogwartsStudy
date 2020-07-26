
#编辑成员页面
from appium.webdriver.common.mobileby import MobileBy

from Appium企业微信实战2.pages.base_page import BasePage


class EditMember(BasePage):

    def del_member(self):
        self.find_and_click((MobileBy.XPATH,"//*[@text='删除成员']"))
        self.find_and_click((MobileBy.XPATH,"//*[@text='确定']"))

        from Appium企业微信实战2.pages.manage_addressbook_page import ManageAddressbook
        return ManageAddressbook(self._driver)