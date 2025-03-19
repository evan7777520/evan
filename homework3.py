# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 13:42:21 2025

@author: kun
"""

name=input("請輸入姓名:")
ID=input("請輸入學號:")
academicyear=int(input("請輸入當前學年度:"))
math=int(input("請輸入數學成績:"))
mathcredit=int(input("請輸入數學學分數:"))
chinese=int(input("請輸入中文成績:"))
chinesecredit=int(input("請輸入中文學分數:"))
english=int(input("請輸入英文成績:"))
englishcredit=int(input("請輸入英文學分數:"))
program=int(input("請輸入程式設計成績:"))
programcredit=int(input("請輸入程式設計學分數:"))
average=(math+chinese+english+program)/4
admissionyear=ID[0:3]
graduationdate=(int(ID[0:3]))+4
currentgrade=int(academicyear)-int(admissionyear)+1
departmentcode=ID[3:5]
classcode=ID[5]
seatnumber=ID[6:8]
weightedaverage=(math*mathcredit+chinese*chinesecredit+english*englishcredit+program*programcredit)/(mathcredit+chinesecredit+englishcredit+programcredit)
standarddeviation=((((math)**2+(chinese)**2+(english)**2+(program)**2)-(4*(average)**2))/4)**(1/2)
numberofvariations=standarddeviation**2
geometricmean=(math*chinese*program*english)**(1/4)
harmonicmean=4/((1/math)+(1/chinese)+(1/english)+(1/program))

print(f'''
您的入學年度為{admissionyear}年
您預計的畢業時間為{graduationdate}年6月
您目前大學{currentgrade}年級
您的系所代碼為{departmentcode}
您的班級代碼為{classcode}
您的座號為{seatnumber}號
您的平均分數為:{average:.2f}分
您的加權分數為{weightedaverage:.2f}分
您的成績標準差為{standarddeviation:.3f}
您的成績變異數為{numberofvariations:.3f}
您的成績幾何平均為{geometricmean:.2f}
您的成績調和平均為{harmonicmean:.2f}
''')










