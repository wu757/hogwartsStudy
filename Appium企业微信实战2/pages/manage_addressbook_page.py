from appium.webdriver.common.mobileby import MobileBy

from Appium企业微信实战2.pages.base_page import BasePage
from Appium企业微信实战2.pages.edit_member_page import EditMember

#管理通讯录页面
class ManageAddressbook(BasePage):

    def choose_contacts(self,name):
        self.wait_with_visibility((MobileBy.XPATH, "//*[@text='管理通讯录']"))
        self.find_with_scroll(name).click()
        return EditMember(self._driver)

    def close_page(self):
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/h9p"))

        from Appium企业微信实战2.pages.address_list_page import AddressList
        return AddressList(self._driver)

