#-*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import sys

sys.path.append('F:\\temp\\web自动化\\case')
from case.case_sys_setup import Test

capital = 840000.0
rate = 0.049
rate_per_month = rate/12.0

print capital/360
print capital/360.0*359.0*rate_per_month

