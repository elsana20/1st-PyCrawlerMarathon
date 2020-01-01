#D1 資料來源與檔案存取
#--------------------------------------Day001_Sample---------------------------------------------------

"""
#1. 利用 Python 下載檔案#
from urllib.request import urlretrieve

urlretrieve ("https://www.w3.org/TR/PNG/iso_8859-1.txt", "./1.txt")
urlretrieve ("https://www.w3.org/TR/PNG/iso_8859-1.txt", "./data/2.txt")


#打開文件（預設位置會是跟 .ipynb 程式相同的目錄）
import os, sys
dirs = os.listdir( './' )

# 顯示所有文件
for file in dirs:
    print(file)


#2. 利用 Python 存取檔案
fh = open("example.txt", "w")
f = fh.write("To write or not to write\nthat is the question!\n")
fh.close()
print(f)

fh = open("example.txt", "r")
f = fh.read()
fh.close()
print(f)

with open("example-with.txt", "w") as fh:
    f = fh.write("To write or not to write\nthat is the question!\n")
    print(f)
    
with open("example-with.txt", "r") as fh:
    f = fh.read()
    print(f)

import os, sys
# 打開文件
dirs = os.listdir( './' )

# 顯示所有文件
for file in dirs:
    print(file)


#3. 編碼判讀
import chardet
f = open('example1.txt', 'rb')
data = f.read()
print(chardet.detect(data))


import chardet
 f = open('example2.csv', 'rb')
data = f.read()
print(chardet.detect(data))

"""

#---------------------------------Day001_HW--------------------------------------------------#
"""
1.（簡答題）檔案、API、爬蟲三種取得資料方式有什麼不同？
2.（實作）完成一個程式，需滿足下列需求：
下載指定檔案到 Data 資料夾，存成檔名 Homework.txt
檢查 Data 資料夾是否有 Homework.txt 檔名之檔案
將「Hello World」字串覆寫到 Homework.txt 檔案
檢查 Homework.txt 檔案字數是否符合 Hello World 字數
"""

# 根據需求引入正確的 Library
from urllib.request import urlretrieve
import os, sys

# 下載檔案到 Data 資料夾，存成檔名 Homework.txt
try:
    os.makedirs( './Data', exist_ok=True )
    urlretrieve ("https://www.w3.org/TR/PNG/iso_8859-1.txt", "./Data/Homework.txt")
except:
    print('發生錯誤！')

#-------------------------------------------------------------------------------------------------------

# 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案
files = []
dirs = os.listdir( './Data' )
# 顯示所有文件
for files in dirs:
    if 'Homework.txt' in files:
        print('[O] Data 資料夾中已有 Homework.txt 檔名之檔案，檔案下載成功。')
    else:
        print('[X]  Data 資料夾中沒有 Homework.txt 檔名之檔案，要重新下載。')

#可簡化為
#files = os.listdir('./Data')
#if 'Homework.txt' in files:
#    print('[O] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')
#else:
#    print('[X] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')

#-------------------------------------------------------------------------------------------------------

# 將「Hello World」字串覆寫到 Homework.txt 檔案
f = ''
with open("./Data/Homework.txt", "w") as fh:
    f = fh.write("Hello World")
try:
    with open("./Data/Homework.txt", "r") as fh:
        f = fh.read()
        print(f)
except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
    pass    

# 檢查 Homework.txt 檔案字數是否符合 Hello World 字數
if len('Hello World') == len(f):
    print('[O] Homework.txt 檔案字數符合 Hello World 字數。Well done。')
else:
    print('[X]  Homework.txt 檔案字數不符合 Hello World 字數。字串覆寫失敗。')