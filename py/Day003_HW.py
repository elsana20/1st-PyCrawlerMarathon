#D3   Python 下載XML檔案與解析
#--------------------------------------Day003_Sample---------------------------------------------------
# 一. 存取 XML 的三種套件

# 1 用 xml.dom.minidom
import xml.dom.minidom

# 存取檔案
doc = xml.dom.minidom.parse("./Data/sample.xml")

# 存取我們的資訊
print(doc.getElementsByTagName("Title")[0].firstChild.nodeValue)

# 用迴圈存取我們的資訊
chapters = doc.getElementsByTagName("Chapter")
for chapter in chapters:
    print (chapter.getAttribute('name'), chapter.firstChild.nodeValue)


# 2 用xml.etree.ElementTree
import xml.etree.ElementTree as ET 

# 存取檔案
tree = ET.parse('./Data/sample.xml') 
root = tree.getroot()

# 存取我們的資訊
print(root[0].text)

# 用迴圈存取我們的資訊
chapters = root[2]
for chapter in chapters:
    print (chapter.attrib['name'], chapter.text)


# 3 用xmltodict
import xmltodict

# 存取檔案

with open('./Data/sample.xml',encoding = 'utf-8') as fd:
    doc = dict(xmltodict.parse(fd.read()))

# 存取我們的資訊
print(doc['CUPOY']['Title'])

# 用迴圈存取我們的資訊
chapters = doc['CUPOY']['Chapters']['Chapter']
for chapter in chapters:
    print (chapter['@name'], chapter['#text'])

#----------------------------------------------------------------------------------
# 下載檔案
import urllib.request
import zipfile

res = "http://opendata.cwb.gov.tw/govdownload?dataid=F-D0047-093&authorizationkey=rdec-key-123-45678-011121314"
urllib.request.urlretrieve(res, "./data/example.zip")
f = zipfile.ZipFile('./data/example.zip')
f.extractall('./data')

import os, sys
# 打开文件
dirs = os.listdir( './data' )

# 输出所有文件和文件夹
for file in dirs:
    print(file)

# File I/O
# 讀檔案
fh = open("./data/64_72hr_CH.xml", "r",encoding = 'utf-8')
xml = fh.read()
fh.close()
#print(xml) #太長，先不印出來

#-----------------------------------------------------------------------
# xmltodict解析檔案
# 解析檔案內容
import xmltodict
d = dict(xmltodict.parse(xml))

# 取出 datasetDescription
datasetDescription = d['cwbopendata']['dataset']['datasetInfo']['datasetDescription']
print(datasetDescription)

#--------------------------------------Day003_HW---------------------------------------------------
"""
比較一下範例檔案中的「File I/O」與「xmltodict」讀出來的內容有什麼差異
根據範例檔案的結果：
1. 請問高雄市有多少地區有溫度資料？
2. 請取出每一個地區所記錄的第一個時間點跟溫度
3. 請取出第一個地區所記錄的每一個時間點跟溫度
"""

# 1. 請問高雄市有多少地區有溫度資料？
import xmltodict
# 用xmltodict存取XML檔案
with open('./data/64_72hr_CH.xml',encoding = 'utf-8') as fd:
     doc = dict(xmltodict.parse(fd.read()))

# 存取高雄資訊
print(doc['cwbopendata']['dataset']['locations']['locationsName'])

# 用迴圈存取高雄區域的資訊
location_data = doc['cwbopendata']['dataset']['locations']['location']
#location_data是xmltodict parse XML檔案後的資料
#parse到location，所以不同的location視為一筆資料

for area_data in location_data:
    print (area_data['locationName'])
    # area_data為變數,代表location_data中的每一筆資料
    # 每一筆資料用不同的標籤名字識別，如locationName
        
print('高雄有', len(location_data), '個地區有溫度資料')
#用 len()計算location_data中共有幾筆資料

# 傳統程式寫法
# count_number = 0
# area_tempers = doc['cwbopendata']['dataset']['locations']['location']
# for area_temper in area_tempers:
#     for weatherElement in area_temper['weatherElement']:
#         if weatherElement['description'] == '溫度':
#             count_number += 1
# print('高雄有%s個地區有溫度資料' % count_number)

#--------------------------------------------------------------------------------

# 2. 請取出每一個地區所記錄的第一個時間點跟溫度

#location_data = doc['cwbopendata']['dataset']['locations']['location']
for area_data in location_data:
    print (area_data['locationName'],'第一個時間點是',area_data['weatherElement'][0]['time'][0]['dataTime'],'溫度',area_data['weatherElement'][0]['time'][0]['elementValue']['value'],'度')
    #print (area_data['locationName'])
    #print (area_data['weatherElement'][0]['time'][0]['dataTime'])
    #print (area_data['weatherElement'][0]['time'][0]['elementValue']['value'])
    #因為weatherElement、time在同一個結點中有多筆資料，所以要加上[index]
     
# 傳統程式寫法
# areas_temper = doc['cwbopendata']['dataset']['locations']['location']
# for area_temper in areas_temper:
#     for weatherElement in area_temper['weatherElement']:
#         if weatherElement['description'] == '溫度':
#             print(area_temper['locationName'], weatherElement['time'][0]['dataTime'], weatherElement['time'][0]['elementValue']['value'], weatherElement['time'][0]['elementValue']['measures'])

#--------------------------------------------------------------------------------

# 3. 請取出第一個地區所記錄的每一個時間點跟溫度

area_name = location_data[0]
#取出第一個區域的名稱
print (area_name['locationName'])

location_data2 = doc['cwbopendata']['dataset']['locations']['location'][0]['weatherElement'][0]['time']
for area_data2 in location_data2:
    print ('時間點：',area_data2['dataTime'],', 溫度：',area_data2['elementValue']['value'])

    
# 傳統程式寫法
# areas_temper = doc['cwbopendata']['dataset']['locations']['location']
# for area_temper in areas_temper:
#     if area_temper['locationName'] == '鹽埕區':
#         for weatherElement in area_temper['weatherElement']:
#             if weatherElement['description'] == '溫度':
#                 for time in weatherElement['time']:
#                     print(time['dataTime'], time['elementValue']['value'], time['elementValue']['measures'])