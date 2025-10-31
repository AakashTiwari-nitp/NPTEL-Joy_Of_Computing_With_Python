#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 16:07:47 2025

@author: aakash-tiwari
"""


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=Service("/home/aakash-tiwari/Downloads/chromedriver-linux64/chromedriver"))
browser.get("https://web.whatsapp.com/")

wait = WebDriverWait(browser, 600)
target = '"Name"' # Enter the target you want to send 
string = "Message sent from Browser Automation" # Enter the message you want to send

x_arg = '//span[contains(@title, '+ target + ')]'
target = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()


input_box = browser.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
for i in range(5):
    input_box.send_keys(string+Keys.ENTER)