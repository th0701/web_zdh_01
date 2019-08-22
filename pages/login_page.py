# 二次封装selenium方法
from selenium import webdriver
from common import readconf
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as wdw


class Login():

    def __init__(self):
        self.d = webdriver.Chrome()
        self.d.get(readconf.sysurl)
        timeout = readconf.timeout
        self.d.implicitly_wait(timeout)
        self.d.maximize_window()
        self.wdw = wdw(self.d, timeout, readconf.timepl)

    def find_ele(self, tuples):
        return self.wdw.until(ec.presence_of_element_located(tuples))

    def send_key(self, obj, msg):
        return obj.send_keys(msg)

    def cli(self, obj):
        return obj.click()

    def quits(self):
        self.d.quit()

    def switch_frame(self, i):
        return self.d.switch_to_frame(i)




