import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    _base_url = ""

    def __init__(self, driver_basepage: WebDriver = None):
        if driver_basepage == None:
            self.driver = webdriver.Chrome()
            if self._base_url != "":
                self.driver.get(self._base_url)
            self.get_cookie()
            self.cookie_login()
        else:
            self.driver = driver_basepage
        self.driver.implicitly_wait(3)

    def get_cookie(self):
        time.sleep(15)
        cookies = self.driver.get_cookies()
        with open("cookies.json", "w") as f:
            json.dump(cookies, f)

    def cookie_login(self):
        cookies = json.load(open("cookies.json"))
        for cookie in cookies:
            # 解决selenium.common.exceptions.InvalidArgumentException: Message: invalid argument: invalid ‘expiry’
            if "expiry" in cookie:
                cookie["expiry"] = int(cookie["expiry"])
            self.driver.add_cookie(cookie)
        el = None
        for i in range(3):
            self.driver.refresh()
            try:
                el = self.wait_with_clickable(By.ID, "menu_index")
            except Exception:
                print(Exception)
                print("重试%d次" % (i + 1))
            if el is not None:
                break

    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)

    def finds(self, by, value):
        return self.driver.find_elements(by=by, value=value)

    def quit(self):
        return self.driver.quit()

    def wait_with_clickable(self, by, value):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((by, value)))

    def wait_with_visibility(self, by, value):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((by, value)))

    def waits_with_visibility(self, by, value):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((by, value)))
