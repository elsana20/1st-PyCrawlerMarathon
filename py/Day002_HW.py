#D2  Python 下載CSV檔案與解析
#--------------------------------------Day002_Sample---------------------------------------------------
#下載CSV檔案
import os, urllib.request

os.makedirs( './data', exist_ok=True )
res = "http://opendata.hccg.gov.tw/dataset/432257df-491f-4875-8b56-dd814aee5d7b/resource/de014c8b-9b75-4152-9fc6-f0d499cefbe4/download/20150305140446074.csv"
urllib.request.urlretrieve(res, './data/example.csv')

import os, sys
# 打开文件
dirs = os.listdir( './data' )

# 输出所有文件和文件夹
for file in dirs:
     print(file)

# File I/O
fh = open("./data/example.csv",encoding = 'utf-8-sig')
f = fh.read()
fh.close()
print(f)
#print(f.encode("utf8").decode("cp950", "ignore"))

# CSV Reader
import csv

# 開啟 CSV 檔案
with open('./data/example.csv', newline='',encoding = 'utf-8') as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    for row in rows:
        print(row)
#--------------------------------------Day002_HW---------------------------------------------------
"""
作業目標
比較一下範例檔案中的「File I/O」與「CSV Reader」讀出來的內容有什麼差異

根據範例檔案的結果：

取出班次一的每一個時間
將班次一的每一個時間用一種資料型態保存
將班次一到五與其所有時間用一種資料型態個別保存
"""

# 範例
# https://docs.python.org/3/library/csv.html
# 從csv文件讀取的每一行都作為字符串列表返回。除非QUOTE_NONNUMERIC指定了format選項，否則不會執行自動數據類型轉換（在這種情況下，未引用的字段將轉換為浮點數）。


# 1.下載cvs檔
import urllib.request
import os, sys

os.makedirs( './data', exist_ok=True )
res = "http://opendata.hccg.gov.tw/dataset/432257df-491f-4875-8b56-dd814aee5d7b/resource/de014c8b-9b75-4152-9fc6-f0d499cefbe4/download/20150305140446074.csv"
urllib.request.urlretrieve(res, './data/example.csv')

#urllib.request


# 2.打開文件
dirs = os.listdir( './data' )

# 輸出所有文件和文件夹
for file in dirs:
    print(file)

fh = open("./data/example.csv","rt",encoding = 'utf-8-sig')
f = fh.read()
print(f)
#print(f.encode("utf8").decode("cp950", "ignore"))
fh.close()


# 3.CSV Reader
import csv

# 開啟 CSV 檔案
with open('./data/example.csv', newline='',encoding = 'utf-8-sig') as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    for row in rows:
        print(row)  #ipynb檔可直接用此語法
        #print(row.encode("utf8").decode("cp950", "ignore"))
        #print(', '.join(row))


# 作業1. 取出班次一的每一個時間
# 開啟 CSV 檔案
with open('./data/example.csv', newline='',encoding = 'utf-8-sig') as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    for row in rows:
        print(row[5])

# 作業2. 將班次一的每一個時間用一種資料型態保存
# 儲存到一維陣列
import array
bus_1_time = []
with open('./data/example.csv', newline='',encoding = 'utf-8-sig') as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    for row in rows:      
        bus_1_time.append(row[5])
    print(bus_1_time)

# 作業3. 將班次一到五與其所有時間用一種資料型態個別保存
# 儲存到二維陣列
bus_time_list = [[0]*5 for i in range(100)]
with open('./data/example.csv', newline='',encoding = 'utf-8-sig') as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    i=0
    for row in rows:
        for j in range(5,10):
            bus_time_list[i][j-5]=row[j]     
        i=i+1
        
    for k in range(5):
        for s in range(i):
            print (bus_time_list[s][k])


#作業3：改以5個一維陣列存檔
d1 = []
d2 = []
d3 = []
d4 = []
d5 = []

with open('./data/example.csv', newline='',encoding = 'utf-8-sig') as csvfile:
  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)
  # 以迴圈輸出每一列
  for row in rows:
    d1.append(row[5])
    d2.append(row[6])
    d3.append(row[7])
    d4.append(row[8])
    d5.append(row[9])

data = {}
data[d1[0]] = d1[1:]
data[d2[0]] = d2[1:]
data[d3[0]] = d3[1:]
data[d4[0]] = d4[1:]
data[d5[0]] = d5[1:]

print(data)