# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions
import os
import my_db
import operations
from my_utility import *
from operations import MyWidget

from my_browser import MyBrowser

os.system('taskkill -F -IM chromedriver.exe')
os.system('taskkill -F -IM chromedriver2.37.exe')
os.system('taskkill -F -IM chromedriver2.35.exe')
os.system('taskkill -F -IM chromedriver2.34.exe')

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
# print db.query('select * from all_branchstore_details limit 1')

# 登陆
operations.login(browser, **login_info)
# ######################################################################################################################

# 进入网吧管理列表
operations.skip_to_bar_manage_list(browser)
# ######################################################################################################################

# 进入网吧管理
operations.skip_to_bar_manage(browser)
# ######################################################################################################################

from case import case_sys_setup

# # 进入设置页面 例如：系统设置-计费设置
# operations.skip_to_setting_page(browser, path=[u'系统设置', u'计费设置'])
# # ######################################################################################################################
#
# cmd = " select IntValue from branchstore_setupparam " + \
#       " where branchstore_no = " + login_info['branchstore_no'] + \
#       " and param_name = " + "'bk'"
#
# # 每办一张会员卡需交开卡费
# expected_result = {
#     'case_no': 0001,
#     'setup_key': 'bk',
#     'setup_value': random_int(1, 100),
#     'pre_setup_value': db.query(cmd)[0][0],
#     'left_desc': u'每办一张会员卡需交卡费：',
#     'right_desc': u'元',
# }
# widget = MyWidget(browser, **expected_result)
# actual_result = {
#     'pre_setup_value': widget.setup_value,
# }
# widget.set(expected_result['setup_value'])
# operations.save_settings(browser)
#
#
# # 收集结果
# def collect_result_info(widget, db):
#     actual_result = {
#         'setup_value': db.query(cmd)[0][0],
#         'left_desc': widget.left_desc,
#         'right_desc': widget.right_desc,
#     }
#     return actual_result
#
#
# from time import sleep
#
# sleep(1) # 等待数据写入数据库
# actual_result.update(collect_result_info(widget, db))
#
# # 检查结果
# print expected_result
# print actual_result
# from my_result_processor import check_result
#
# check_result(expected_result, actual_result)
#
# operations.skip_to_home(browser)

# ######################################################################################################################

# 会员上机时间不足限时不计费
#
# setup_key_01 = 'Less2m'
# setup_key_02 = 'FreeMin'
# setup_value_02 = '34'
#
# def operation():
#     check_elem = browser.find_element(By.ID, 'setup_'+setup_key_01)
#
#     ins_elem = check_elem.find_element(By.XPATH, 'following-sibling::ins[1]')
#     ins_elem.click()
#
#     parent_elem = check_elem.find_element(By.XPATH, '..')
#     left_text_elem = parent_elem.find_element(By.XPATH, 'following-sibling::span[1]')
#     # print left_text_elem.text
#
#     # 分钟
#     input_elem = browser.find_element(By.ID, 'setup_'+setup_key_02)
#     input_elem.clear()
#     input_elem.send_keys(setup_value_02)
#
#     parent_elem = input_elem.find_element(By.XPATH, '..')
#     mid_text_elem = parent_elem.find_element(By.XPATH, 'preceding-sibling::label[1]')
#     #print mid_text_elem.text
#
#     right_text_elem = input_elem.find_element(By.XPATH, 'following-sibling::div[1]')
#     # print right_text_elem.text
#
#     info = dict()
#
#     info['check'] = check_elem.is_selected()
#     info['left_text'] = left_text_elem.text
#     info['mid_text'] = mid_text_elem.text
#     info['right_text'] = right_text_elem.text
#
#     return info
#
# print MyBrowser.execute_twice_if_failed(browser, operation)

# ######################################################################################################################

raw_input('任意键结束')
browser.quit()

# setup_MemFreeUse
# setupForm > div > div > div:nth-child(1) > div.col-xs-12.col-md-5 > div.form-group.col-md-6.operation-left > div > label > div > ins
