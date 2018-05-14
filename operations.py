# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from my_browser import MyBrowser


# 登陆
def login(browser, **kwargs):
    elem = browser.find_element(By.NAME, 'bossNumber')
    elem.send_keys(kwargs['boss_number'])

    elem = browser.find_element(By.NAME, 'userInfo.accountNumber')
    elem.send_keys(kwargs['cloud_account'])

    elem = browser.find_element(By.NAME, 'userInfo.password')
    elem.send_keys(kwargs['cloud_password'])

    elem = browser.find_element(By.NAME, 'captcha')
    elem.send_keys(kwargs['captcha'])

    elem = browser.find_element(By.ID, 'submitBtn')
    elem.click()

# 主页
def skip_to_home(browser, **kwargs):
    wait = WebDriverWait(browser, 10)
    elem = wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[3]/header/nav/div/a/div/span')))
    print elem
    import time
    # time.sleep(1)
    # elem = wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[3]/header/nav/div/a/div/span')))
    # print elem

    elem.click()

def skip_to_bar_manage_list(browser, **kwargs):
    """
    进入网吧管理列表
    :param browser:
    :param kwargs:
    :return:
    """
    browser.switch_to.frame(0)
    elem = browser.find_element(By.PARTIAL_LINK_TEXT, u'管理')
    elem.click()

def skip_to_bar_manage(browser, **kwargs):
    """
    进入网吧管理
    :param browser:
    :param kwargs:
    :return:
    """
    elem = browser.find_element(By.XPATH, '//*[@id="barListTable"]/tbody')
    elems = elem.find_elements(By.TAG_NAME, 'tr')
    for elem in elems:
        elem
    elem = browser.find_element(By.XPATH, '//*[@id="barListTable"]/tbody/tr/td[7]/div/button[2]')
    elem.click()


def skip_to_setting_page(browser, **kwargs):
    """
    进入设置页面 例如：系统设置-计费设置
    :param browser:
    :param kwargs: path=[u'系统设置', u'计费设置']
    :return:
    """
    path = kwargs['path']

    elem_0 = browser.find_element(By.LINK_TEXT, path[0])
    elem_1 = browser.find_element(By.LINK_TEXT, path[1])
    if elem_1.is_displayed():
        return
    else:
        wait = WebDriverWait(browser, 10)
        elem = wait.until(ec.visibility_of_element_located((By.LINK_TEXT, path[0])))
        elem.click()

class MyWidget(object):
    def __init__(self, browser, **kwargs):
        self.browser = browser
        self.setup_key = kwargs['setup_key']

        self.elem = self.browser.find_element(By.ID, 'setup_' + self.setup_key)
        self.setup_value = self.elem.get_attribute('value')

        elem = self.elem.find_element(By.XPATH, '..')
        left_elem = elem.find_element(By.XPATH, 'preceding-sibling::label[1]')
        right_elem = elem.find_element(By.XPATH, 'following-sibling::label[1]')

        self.left_desc = left_elem.text
        self.right_desc = right_elem.text

    def set(self, value):
        def operation():
            self.elem.clear()
            self.elem.send_keys(value)

        MyBrowser.execute_twice_if_failed(self.browser, operation)



def set_text_value_01(browser, **kwargs):
    """
    适用控件：每办一张会员卡需交卡费：☐元
    :param browser:
    :param kwargs:
    :return:
    """
    setup_key = kwargs['setup_key']
    setup_value = kwargs['setup_value']

    def operation():
        elem = browser.find_element(By.ID, 'setup_' + setup_key)
        elem.clear()
        elem.send_keys(setup_value)

        elem = elem.find_element(By.XPATH, '..')
        left_elem = elem.find_element(By.XPATH, 'preceding-sibling::label[1]')
        right_elem = elem.find_element(By.XPATH, 'following-sibling::label[1]')

        info = dict()
        info['left_text'] = left_elem.text
        info['right_text'] = right_elem.text
        info['input_value'] = setup_value

        return info

    return MyBrowser.execute_twice_if_failed(browser, operation)


def set_text_value_02(browser, **kwargs):
    """
    适用控件：☑ 会员上机时间不足限时不计费 限时设置：☐分钟
    :param browser:
    :param kwargs:
    :return:
    """
    setup_key = kwargs['setup_key']
    setup_value = kwargs['setup_value']

    def operation():
        org_elem = browser.find_element(By.ID, 'setup_'+setup_key)
        print org_elem.is_selected()
        ins_elem = org_elem.find_element(By.XPATH, 'following-sibling::ins[1]')
        ins_elem.click()

        parent_elem = org_elem.find_element(By.XPATH, '..')

        span_elem = parent_elem.find_element(By.XPATH, 'following-sibling::span[1]')
        print span_elem.text

        # 分钟
        org_elem = browser.find_element(By.ID, 'setup_MemFreeUse_val')
        org_elem.clear()
        org_elem.send_keys('30')

        parent_elem = org_elem.find_element(By.XPATH, '..')
        label_elem = parent_elem.find_element(By.XPATH, 'preceding-sibling::label[1]')
        print label_elem.text

        div_elem = org_elem.find_element(By.XPATH, 'following-sibling::div[1]')
        print div_elem.text

        return 0

    return MyBrowser.execute_twice_if_failed(browser, operation)

def save_settings(browser):
    # 点击保存
    elem = browser.find_element(By.CLASS_NAME, 'btn-info')
    elem.click()

    # 确定保存
    browser.switch_to.parent_frame()
    wait = WebDriverWait(browser, 10)
    elem = wait.until(
        ec.visibility_of_element_located((By.XPATH, '//*[@id="myConfirmModal"]/div/div/div[3]/button[1]')))
    elem.click()

    # 等待提示
    wait.until(
        ec.visibility_of_element_located((By.XPATH, '//*[@id="myAlertModal"]'))
    )
    wait.until(
        ec.invisibility_of_element_located((By.XPATH, '//*[@id="myAlertModal"]'))
    )







