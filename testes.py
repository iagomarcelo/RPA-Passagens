# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from openpyxl import load_workbook
# import time
# import os
# from basicFunctions import *

# templatePath = os.getcwd()+"\\"+ 'template' +".xlsx"
# workbook = load_workbook(templatePath)
# workbookPage = workbook.active


# for row in workbookPage:
#     sitesList = gettingExcelData()[0]
#     sitesDict = gettingExcelData()[1]

#     if row[3].value in sitesList:
#         siteName = row[3].value
#         url = sitesDict[siteName]
#         openBrowser(url)

''''''
#DATA VALIDATION EXCEL
#1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;

# for i in range(7,21):      
#     cellValue = workbookPage.cell(row = i, column = 4).value
#     sitesList.append(cellValue)
# print (sitesList)