from appium.webdriver.common.mobileby import MobileBy

from Appium企业微信实战2.pages.base_page import BasePage


class AddMemberManually(BasePage):
    _name_element=(MobileBy.XPATH,"//*[contains(@text,'姓名')]/following-sibling::android.widget.EditText[1]")
    _phone_element=(MobileBy.XPATH,"//*[@text='手机号']")

    def edit_name(self,name):
        self.find(self._name_element).send_keys(name)
        return self

    def edit_phonenum(self,phoneNo):
        self.find(self._phone_element).send_keys(phoneNo)
        return self

    def edit_identity(self):
        self.find_and_click((MobileBy.XPATH,"//*[@text='身份']"))
        self.find_and_click((MobileBy.XPATH,"//*[@text='上级']"))
        return self

    def click_save(self):
        from Appium企业微信实战2.pages.member_invite_page import MemberInvite
        self.find_and_click((MobileBy.XPATH,"//*[@text='保存']"))
        return MemberInvite(self._driver)