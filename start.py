from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as browser_wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup as soup
import csv
import os
import time


options = Options()
options.add_argument("-window-size=1920,1080")
driver = webdriver.Chrome(options=options)

with open('trippyape_0-10.csv') as file:
    for line in file:
        driver.get(line)
        folder = driver.find_element_by_xpath("//button[@class='UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0 btgkrL Toolbar--tool']//i[@value='refresh']")
        time.sleep(1)
        folder.click()

