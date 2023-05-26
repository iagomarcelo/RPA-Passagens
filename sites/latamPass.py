from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import time
import sys, os
sys.path.insert(1, 'c:/Users/Aluno/Documents/GitHub/RPA-Passagens')
from basicFunctions import *


# openBrowser('https://latampass.latam.com/pt_br/')
def searchTicket(browser = openBrowser('https://latampass.latam.com/pt_br/')):
    browser.find_element(By.XPATH, '/html/body/main/div/div[2]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/main/div/div[2]/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/span').click()
    