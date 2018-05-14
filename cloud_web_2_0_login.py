#-*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

from my_common import *

browser = webdriver.Chrome(executable_path=r'.\source\driver\chromedriver')
browser.implicitly_wait(10)
browser.get("http://192.168.172.23:9999/CloudCenter/login/toLogin")

# 登陆
elem = browser.find_element(By.NAME, 'bossNumber')
elem.send_keys('pcy_test_uncloud1948')

elem = browser.find_element(By.NAME, 'userInfo.accountNumber')
elem.send_keys('10000')

elem = browser.find_element(By.NAME, 'userInfo.password')
elem.send_keys('123123')

elem = browser.find_element(By.NAME, 'captcha')
elem.send_keys('bypass')

elem = browser.find_element(By.ID, 'submitBtn')
elem.click()

# 进入网吧管理
browser.switch_to.frame(0)
# elem = browser.find_element(By.CLASS_NAME, 'inner')
elem = browser.find_element(By.PARTIAL_LINK_TEXT, u'管理')
elem.click()

# 进入网吧设置
elem = browser.find_element(By.XPATH, '//*[@id="barListTable"]/tbody/tr/td[7]/div/button')
elem.click()
##########################################
elem = browser.find_element(By.CSS_SELECTOR, '[for="setup_bk"]')
print elem.text


# 切换到功能设置
elem = browser.find_element(By.XPATH, '/html/body/div/aside/section/ul/li[2]/ul/li[2]/a')
print elem.text
elem.click()

# 输入
# elem = driver.find_element(By.ID, 'setup_bk')
# elem.clear()
# elem.send_keys(random_int(1, 10))

# 勾选
elem = browser.find_element(By.XPATH, '//*[@id="setupForm"]/div/div/div[1]/div[1]/div[2]/div[3]/label/div/ins')
elem.click()

# 选择
elem = browser.find_element(By.XPATH, '//*[@id="setupForm"]/div/div/div[1]/div[2]/div[2]/div[1]/select/option[3]')
elem.click()

# 计费模式
fmt = '//*[@id="setupForm"]/div/div/div[1]/div[1]/div[2]/div[{pos}]/label/div/ins'
for i in range(3):
    pos = i + 1
    print fmt.format(pos=pos)

# 客户端重启设置
fmt = '//*[@id="setupForm"]/div/div/div[1]/div[2]/div[2]/div[1]/select/option[{pos}]'
for i in range(3):
    pos = i + 1
    print fmt.format(pos=pos)


############################################
# 点击保存
elem = browser.find_element(By.XPATH, '//*[@id="mainContent"]/section[2]/div/div/button')
elem.click()

# 确定保存
browser.switch_to.parent_frame()
wait = WebDriverWait(browser, 10)
elem = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="myConfirmModal"]/div/div/div[3]/button[1]')))
elem.click()

# driver.switch_to.frame(0)
# elem = driver.find_element(By.XPATH, '/html/body/div/aside/section/ul/li[2]/ul/li[2]/a')
# elem.click()

# driver.switch_to.frame(0)
wait = WebDriverWait(browser, 10)
elem = wait.until(EC.visibility_of_element_located((By.ID, 'myAlertModal')))
elem.click()
wait.until(EC.invisibility_of_element_located((By.ID, 'myAlertModal')))

browser.switch_to.frame(0)
# elem = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="setupForm"]/div/div/div[2]/div/div/div[1]/label/div/ins')))
# elem = wait.until(EC.presence_of_element_located((By.ID, 'setup_CheckOutActive')))
# elem = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="setupForm"]/div/div/div[2]/div/div/div[1]/label/div')))

elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                  'input#setup_CheckOutActive + ins')))
elem.click()
#setupForm > div > div > div:nth-child(1) > div:nth-child(1) > div > div > input[type="hidden"]:nth-child(1)
time.sleep(10)
browser.quit()