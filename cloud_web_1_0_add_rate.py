#-*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://192.168.172.6/Root/Login/Login_Login")

elem = driver.find_element(By.NAME, 'loginDTO.chain_no')
elem.send_keys("1943")

elem = driver.find_element(By.NAME, 'loginDTO.chain_user_id')
elem.send_keys("10000")

elem = driver.find_element(By.ID, 'Chain_user_password')
elem.send_keys("111111")

elem = driver.find_element(By.ID, 'chain-submit')
elem.click()

driver.switch_to.frame('mainWorkArea')

elem = driver.find_element(By.XPATH, '//*[@id="dgDataGrid"]/tbody/tr[5]/td/a[1]')
elem.click()

elem = driver.find_element(By.XPATH, '//*[@id="dgDataGrid"]/tbody/tr[1]/td/input')
elem.click()

elem = driver.find_element(By.XPATH, '//*[@id="pricetableOne0"]')
target = driver.find_element(By.XPATH, '//*[@id="pricetableOne126"]')

from selenium.webdriver.common.action_chains import ActionChains

ActionChains(driver).drag_and_drop(elem, target).perform()

# elem = wait.until(EC.alert_is_present())
# elem.accept()











