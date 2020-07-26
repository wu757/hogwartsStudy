from appium.webdriver.common.mobileby import MobileBy

from Appium企业微信实战2.pages.address_list_page import AddressList
from Appium企业微信实战2.pages.base_page import BasePage


class MainPage(BasePage):
    _addresslist=(MobileBy.XPATH, "//*[@text='通讯录']")
    _corporate_addressbook=(MobileBy.XPATH, "//*[@text='企业通讯录']")

    def goto_address_list(self):
        self.wait_visibility_and_click(self._addresslist)
        self.wait_with_visibility(self._corporate_addressbook)
        return AddressList(self._driver)