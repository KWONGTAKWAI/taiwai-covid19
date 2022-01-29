import requests 
import json
import datetime

# https://data.gov.tw/dataset/120711
response = requests.get("https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json")
jd = json.loads(response.text)

today = datetime.date.today().strftime("%Y/%m/%d")
yesterday = (datetime.date.today() + datetime.timedelta(-1)).strftime("%Y/%m/%d")

total = 0
local = 0
external = 0

for i in jd:
    total=total+int(i['確定病例數'])
    if (i['個案研判日']==today) or (i['個案研判日']==yesterday): 
        
        if i['是否為境外移入']=='是':
            external=external + int(i['確定病例數'])
            print("External:")
            print(i)
        else:
            local=local + int(i['確定病例數'])
            print("Local:")
            print(i)
     
print("日期: {} - {} ".format(yesterday,today))
print("最新確診資訊")
print("確診累計: {} 例".format(total))
print("共新增:{} 本土:{} 輸入: {}".format(local+external,local,external))
