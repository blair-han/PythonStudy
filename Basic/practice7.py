'''
# method 1 
import theater_module

theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)
'''

'''
# method 2
import theater_module as mv

mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)
'''

'''
# method 3
from theater_module import *

price(3)
price_morning(4)
price_soldier(5)
'''

'''
# method 4
from theater_module import price, price_morning

price(3)
price_morning(4)
price_soldier(5) # error
'''

# method 5
from theater_module import price_soldier as price
price(5) ## soldier price 

'''
내장함수
Built-in Functions
'''

# input : 사용자 입력을 받는 함수
# language = input("Which language do you like?")
# print("{}는 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
import random # 외장함수
print(dir())
print(dir(random))
lst = [1,2,3]
print(dir(lst))


# modules

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일 

# os : 운영체제에서 제공하는 기본 기능
'''
import os
print(os.getcwd()) # current working directory

folder = 'sample_dir'

if os.path.exists(folder):
    print("The flder already exists")
    os.rmdir(folder)
    prinf(folder, "Folder has been removed")
else:
    os.makedirs(folder) # create folder
    print(folder, "Folder has been created.")

print(os.listdir())
'''
# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())


#timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후 


## Quiz 10
import byme
byme.sign()