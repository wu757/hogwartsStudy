import time

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

with open("contact_data.yaml", 'rb') as f:
    contact_data = yaml.safe_load(f)

class TestWeChat:
    def setup_class(self):
        desire_cap = {}
        desire_cap["deviceName"] = "127.0.0.1:7555"
        desire_cap['platformVersion'] = '6.0.1'
        desire_cap["platformName"] = "Android"
        desire_cap["appPackage"] = "com.tencent.wework"
        desire_cap["appActivity"] = ".launch.LaunchSplashActivity"
        desire_cap["noReset"] = True
        desire_cap["skipDeviceInitialization"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 5)
        # 检查启动后是否出现“选择以下同事一起使用”的页面，有则点跳过
        try:
            self.wait.until(EC.visibility_of_element_located((MobileBy.XPATH,"//*[@text='选择以下同事一起使用']")))
        except TimeoutException:
            print("\n无\"选择以下同事一起使用\"页面")
        else:
            self.driver.find_element_by_xpath("//*[@text='跳过']").click()
    def setup(self):
        self.wait.until(EC.visibility_of_element_located((MobileBy.XPATH, "//*[@text='通讯录']"))).click()
        self.wait.until(EC.visibility_of_element_located((MobileBy.XPATH, "//*[@text='企业通讯录']")))
    def teardown(self):
        # 返回至首页
        for i in range(4):
            try:
                WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((MobileBy.XPATH, "//*[@text='消息']")))
            except TimeoutException:
                print("\n返回到至首页")
                self.driver.back()
            else:
                break

    def teardown_class(self):
        time.sleep(10000)
        self.driver.quit()

    @pytest.mark.dependency(name="addContact")
    @pytest.mark.parametrize("name,phoneNo",contact_data["add_contact"])
    @pytest.mark.run(order=1)
    def test_add_contact(self,name,phoneNo):
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).'
                                                        'instance(0)).scrollIntoView(new UiSelector().'
                                                        'text("添加成员").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='添加成员']").click()
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/following-sibling::android.widget.EditText[1]")\
            .send_keys(name)
        self.driver.find_element_by_xpath("//*[@text='手机号']").send_keys(phoneNo)
        self.driver.find_element_by_xpath("//*[@text='身份']").click()
        self.driver.find_element_by_xpath("//*[@text='上级']").click()
        self.driver.find_element_by_xpath("//*[@text='保存']").click()

        result=self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text
        assert result=="添加成功"

    @pytest.mark.dependency(depends=["addContact"])
    @pytest.mark.parametrize("name",contact_data["del_contact"])
    @pytest.mark.run(order=2)
    def test_del_contact(self,name):
        self.driver.find_element_by_id("com.tencent.wework:id/h9u").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).'
                                                        'instance(0)).scrollIntoView(new UiSelector().'
                                                        f'text("{name}").instance(0));').click()

        self.driver.find_element_by_xpath("//*[@text='删除成员']").click()
        self.driver.find_element_by_xpath("//*[@text='确定']").click()
        # "×"关闭按钮
        self.driver.find_element_by_id("com.tencent.wework:id/h9p").click()
        assert name not in self.driver.page_source

