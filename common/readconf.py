#读取配置文件
import os
import configparser
from common import getpath

path = getpath.getpath("config","myconfig.ini")
conf = configparser.ConfigParser()

conf.read(path, encoding="utf8")

url = conf.get("URL", "url")
timeout = int(conf.get("TIMEOUT","timeout"))
timepl = float(conf.get("TIMEPL","timepl"))
sysurl = conf.get("URL", "sysurl")




