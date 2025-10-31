#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 16:07:47 2025

@author: aakash-tiwari
"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=Service("/home/aakash-tiwari/Downloads/chromedriver-linux64/chromedriver"))
browser.get("https://www.seleniumhq.org")

elem = browser.find_element(By.LINK_TEXT,"Downloads")
elem.click()

search = browser.find_element(By.ID, 'docsearch-input')
search.send_keys("Download")