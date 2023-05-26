from basicFunctions import *

# for key, value in gettingExcelData()[1].items():
#     if key in gettingExcelData()[0]:
#         openBrowser(value)
myWorkbook = openWorkbook('template')

sitesDict = gettingExcelData()


# # print(sitesDict.keys())
for row in myWorkbook:  
    siteName = row[3].value
    print(siteName)
#     if siteName in sitesDict.keys():
#         siteName = row[3].value
#         url = sitesDict[siteName]
#         print(siteName, '->', url)
#         # openBrowser(url)
#     if siteName not in sitesDict.keys():
#         if siteName != None:
#             print('\n'+siteName.upper() ,'-> BUSCAR NOVO SITE!!!\n' )


