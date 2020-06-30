import json
import time


class Utils():
    def get_cookie(self):
        time.sleep(15)
        cookies=self.driver.get_cookies()
        with open("cookies.json", "w") as f:
            json.dump(cookies, f)



