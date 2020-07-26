import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver: WebDriver

    def __init__(self,driver:WebDriver=None):
        self._driver=driver

    def find(self, locator):
        return self._driver.find_element(*locator)

    def find_and_click(self, locator):
        return self.find(locator).click()

    def wait_with_visibility(self, locator):
        return WebDriverWait(self._driver, 5).until(EC.visibility_of_element_located((locator)))

    def wait_visibility_and_click(self, locator):
        return self.wait_with_visibility(locator).click()

    def back_to_mainpage(self):
        for i in range(4):
            try:
                #如果找到//*[@text='消息']则说明已返回至首页
                WebDriverWait(self._driver, 1).until(EC.visibility_of_element_located((MobileBy.XPATH, "//*[@text='消息']")))
            except TimeoutException:
                print("\n返回")
                self._driver.back()
            else:
                print("\n已返回至首页")
                break

    def quit_driver(self):
        time.sleep(2)
        self._driver.quit()

    def find_with_scroll(self,text):
        return self._driver.find_element_by_android_uiautomator(f'new UiScrollable(new UiSelector().scrollable(true)\
                                                        .instance(0)).scrollIntoView(new UiSelector()\
                                                        .text("{text}").instance(0));')

    def get_toast(self):
        return self.find((MobileBy.XPATH,"//*[@class='android.widget.Toast']")).text