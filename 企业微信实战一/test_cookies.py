import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCookie():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    def teardown(self):
        self.driver.quit()
        
    # def test_get_cookie(self):
    #     time.sleep(15)
    #     cookies=self.driver.get_cookies()
    #     with open("cookies.json","w") as f:
    #         json.dump(cookies,f)

    def test_cookie_login(self):
        cookies=json.load(open("cookies.json"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # time.sleep(10)
        # self.driver.refresh()

        wait=WebDriverWait(self.driver, 5)
        while True:
            self.driver.refresh()
            el=wait.\
                until(expected_conditions.element_to_be_clickable((By.ID,"menu_index")))
            if el is not None:
                break
        wait.until(expected_conditions.element_to_be_clickable
                                             ((By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)")))
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        wait.until(
            expected_conditions.presence_of_element_located((By.ID, "js_upload_file_input")))
        # sendkeys需要使用绝对路径
        self.driver.find_element(By.ID, "js_upload_file_input"). \
            send_keys("D:\pythonProject\企业微信实战一\workbook.xlsx")

        assert_ele = wait.until(
            expected_conditions.presence_of_element_located((By.ID, "upload_file_name"))).text

        # assert_ele = self.find(By.ID, "upload_file_name").text
        print(assert_ele)
        assert assert_ele == "workbook.xlsx"



            