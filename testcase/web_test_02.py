from common import log_conf
from pages import elements
import unittest


class Mytestcase(unittest.TestCase):

    logs = log_conf.MyLog()
    def setUp(self):
        self.ele = elements.Element()

    def tearDown(self):
        self.ele.quits()

    def test_01(self):
        self.ele.logings()