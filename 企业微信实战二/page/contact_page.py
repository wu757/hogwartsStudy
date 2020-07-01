import os
import time

from selenium.webdriver.common.by import By

from 企业微信实战二.page.base_page import BasePage


class Contact(BasePage):
    #待导入的表格文件的绝对路径
    _contact_sheet = os.path.join(os.getcwd(), "contact.xlsx")

    def get_member(self):
        """
        获取成员列表
        :return:
        """
        time.sleep(5)
        elements = self.finds(By.CSS_SELECTOR,
                              ".member_colRight_memberTable_td:nth-child(2)")
        name_list = [element.get_attribute("title") for element in elements]

        return name_list

    def del_member(self, name):
        #点击name，这条数据，并删除ta
        #显性等待后再做点击操作
        self.wait_with_visibility(By.XPATH, f"//*[@title='{name}']/../td[1]/input").click()
        self.wait_with_visibility(By.XPATH, "//div[@class='ww_operationBar']//*[text()='删除']").click()
        self.wait_with_visibility(By.XPATH, "//*[text()='确认']").click()
        return Contact(self.driver)

    def batch_import(self):
        self.find(By.ID, "js_upload_file_input").send_keys(self._contact_sheet)
        self.wait_with_visibility(By.XPATH, "//*[text()='contact.xlsx']")
        self.find(By.ID, "submit_csv").click()
        self.wait_with_visibility(By.ID, "reloadContact").click()
        return Contact(self.driver)
