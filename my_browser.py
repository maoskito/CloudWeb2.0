# -*- coding: UTF-8 -*-
import traceback
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from my_log import *
import my_db


class MyBrowser(object):
    @classmethod
    def execute_twice_if_failed(cls, browser, opertion):
        for i in range(2):  # 如果元素被刷新了就再加载执行一次
            try:
                return opertion()
            except exceptions.StaleElementReferenceException:
                pass

TIME_TO_WAIT = 10  # in seconds
homepage = "http://192.168.172.23:9999/CloudCenter/login/toLogin"
login_info = {'boss_number': '1948',
              'branchstore_no': '1948',
              'cloud_account': 'admin',
              'cloud_password': '123123',
              'captcha': 'whatever'
              }

db_config = {
    'host': '192.168.172.7',
    'port': 3306,
    'user': 'rwy',
    'passwd': 'rwy123',
    'db': 'Cloudy_DB',
    'charset': "utf8"
}

dirver_path = r'driver\chromedriver2.37.exe'

browser = webdriver.Chrome(executable_path=dirver_path)
browser.implicitly_wait(TIME_TO_WAIT)
browser.get(homepage)

db = my_db.CloudDB(**db_config)

if __name__ == '__main__':
    pass