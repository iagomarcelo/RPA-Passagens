from basicFunctions import *
from sites import latamPass
# for key, value in gettingExcelData()[1].items():
#     if key in gettingExcelData()[0]:
#         openBrowser(value)
myWorkbook = openWorkbook('template')

sitesDict = gettingExcelData()['sitesDict']

i = 0
# # print(sitesDict.keys())
for row in myWorkbook:  
    siteName = str(row[2].value)
    i += 1
    if siteName in sitesDict.keys():
        siteName = row[2].value
        url = sitesDict[siteName]
        print(siteName, '->', url)
        openBrowser(url)
        latamPass.searchTicket()
    if siteName not in sitesDict.keys():
        if siteName != None:
            print(siteName.upper() ,'-> BUSCAR NOVO SITE!!!' )


