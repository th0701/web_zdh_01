# 页面元素库
from pages.login_page import Login
import time
from common import log_conf
from common import getpath
import unittest

class Element(Login, unittest.TestCase):
    logs = log_conf.MyLog()
    sysusername = ("xpath", '//*[@id="txtName"]')
    syspossword = ("xpath", '//*[@id="txtPWD"]')
    lo = ("xpath", '/html/body/div/div[1]/div[2]/form/input')
    selectProduct = ("xpath", '/html/body/article/section/header/nav/ul/li[2]')
    addProduct = ("xpath", '/html/body/article/section/div[3]/table/tbody/tr/th[1]/button')
    productType = ("xpath", '//*[@id="tbcNameCategory"]/span[1]')
    enterType = ("xpath", '//*[@id="1"]/span')
    nextp = ('xpath', '//*[@id="next_Page"]')
    productName = ('xpath', '//*[@id="txtProductTitle"]')
    #商品促销语
    productlan = ("xpath", '//*[@id="txtIntroduction"]')
    productSelect = ("xpath", '//*[@id="txtKeyWords"]')

    def logings(self):
        try:
            time.sleep(1)
            self.send_key(self.find_ele(self.sysusername), "admin")
            time.sleep(0.5)
            self.send_key(self.find_ele(self.syspossword), "admin")
            self.cli(self.find_ele(self.lo))
            time.sleep(1)
            self.cli(self.find_ele(self.selectProduct))
            time.sleep(1)
            self.cli(self.find_ele(self.addProduct))
            time.sleep(1)
            self.cli(self.find_ele(self.productType))
            time.sleep(2)
            ii = self.d.find_elements_by_tag_name("iframe")[0]
            self.d.switch_to_frame(ii)
            self.cli(self.find_ele(self.enterType))
            time.sleep(1)
            self.cli(self.find_ele(self.nextp))
            time.sleep(1)
            self.send_key(self.find_ele(self.productName), "星空灰")
            time.sleep(1)
            self.send_key(self.find_ele(self.productlan), "谁用谁知道")
            time.sleep(1)
            self.send_key(self.find_ele(self.productSelect), "美瞳")
            time.sleep(1)





        except Exception as e:
            self.logs.error(e)
            getpath.jiutu(self.d)
            raise Exception("失败")







