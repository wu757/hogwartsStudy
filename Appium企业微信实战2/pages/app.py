from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException

from Appium企业微信实战2.pages.base_page import BasePage
from Appium企业微信实战2.pages.main_page import MainPage


class App(BasePage):
    _choose_colleague=(MobileBy.XPATH, "//*[@text='选择以下同事一起使用']")
    _skip=(MobileBy.XPATH, "//*[@text='跳过']")
    def start(self):
        if self._driver==None:
            desire_cap = {}
            desire_cap["deviceName"] = "127.0.0.1:7555"
            desire_cap['platformVersion'] = '6.0.1'
            desire_cap["platformName"] = "Android"
            desire_cap["appPackage"] = "com.tencent.wework"
            desire_cap["appActivity"] = ".launch.LaunchSplashActivity"
            desire_cap["noReset"] = True
            desire_cap["skipDeviceInitialization"] = True
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(5)
        # 检查启动后是否出现“选择以下同事一起使用”的页面，有则点跳过
        try:
            self.wait_with_visibility(self._choose_colleague)
        except TimeoutException:
            print("\n无\"选择以下同事一起使用\"页面")
        else:
            self.find_and_click(self._skip)

        return MainPage(self._driver)


