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
#print(f)
print(f.encode("utf8").decode("cp950", "ignore"))
fh.close()



# 3.CSV Reader
import csv

# 開啟 CSV 檔案
with open('./data/example.csv', newline='') as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    for row in rows:
        #print(row)
          print(row.encode("utf8").decode("cp950", "ignore"))
        #print(', '.join(row))
