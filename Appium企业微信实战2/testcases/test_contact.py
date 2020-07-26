import pytest
import yaml
from appium.webdriver.common.mobileby import MobileBy

from Appium企业微信实战2.pages.app import App

with open("../datas/contact_data.yaml", 'rb') as f:
    contact_data = yaml.safe_load(f)
    add_contact=contact_data["add_contact"]
    del_contact=contact_data["del_contact"]

class TestWeChat:

    def setup_class(self):
        self.main=App().start()

    def setup(self):
        pass

    def teardown(self):
        #用例执行完，均退到首页
        self.main.back_to_mainpage()

    def teardown_class(self):
        self.main.quit_driver()

    @pytest.mark.dependency(name="addContact")
    @pytest.mark.parametrize("name,phoneNo",add_contact)
    @pytest.mark.run(order=1)
    def test_add_contact(self,name,phoneNo):
        result=self.main.goto_address_list().goto_member_invite().goto_add_member_manually().\
            edit_name(name).edit_phonenum(phoneNo).edit_identity().click_save().get_result()
        assert result=="添加成功"

    @pytest.mark.dependency(depends=["addContact"])
    @pytest.mark.parametrize("name", del_contact)
    @pytest.mark.run(order=2)
    def test_del_contact(self, name):
        page_source=self.main.goto_address_list().goto_manage_addressbook()\
            .choose_contacts(name).del_member().close_page()\
            .get_page_source()
        assert name not in page_source