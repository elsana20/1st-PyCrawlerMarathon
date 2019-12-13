# 根據需求引入正確的 Library

from urllib.request import urlretrieve
import os, sys

# 下載檔案到 Data 資料夾，存成檔名 Homework.txt
try:
    os.makedirs( './Data', exist_ok=True )
    urlretrieve ("https://www.w3.org/TR/PNG/iso_8859-1.txt", "./Data/Homework.txt")

except:
    print('發生錯誤！')


# 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案

files = []

dirs = os.listdir( './Data' )

# 顯示所有文件
for files in dirs:
    if 'Homework.txt' in files:
        print('[O] Data 資料夾中已有 Homework.txt 檔名之檔案，檔案下載成功。')
    else:
        print('[X]  Data 資料夾中沒有 Homework.txt 檔名之檔案，要重新下載。')



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
