# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 13:47:24 2025

@author: kun
"""


birthday = input("請輸入生日 YYYYMMDD:")
time = input("請輸入出生時間 hhmm:")
if (birthday.isdigit() and time.isdigit()):
    debugbirthday=int(birthday)
    debugtime=int(time)
    if debugbirthday > 99999999 :
        print("您的生日或出生時間有誤")
    elif debugbirthday < 10000 :
        print("您的生日或出生時間有誤")
    elif debugtime > 9999 :
        print("您的生日或出生時間有誤")
    else:
        ID=int(birthday[-4:])
        debugmonth=int(birthday[-4:-2])
        debugday=int(birthday[-2:])
        debugyear=int(birthday[-8:-4])
        debugyearU=debugyear%4
        debugyear100U=debugyear%100
        debugyear400U=debugyear%400
        debughour=int(time[-4:-2])
        debugminute=int(time[-2:])

        if debughour > 23 :
            print("您的生日或出生時間有誤")
        elif debugmonth == 0 :
             print("您的生日或出生時間有誤")
        elif debugminute > 59 :
            print("您的生日或出生時間有誤")
        elif debugmonth > 12 :
            print("您的生日或出生時間有誤")
        else:
            if debugmonth == 2:
                if debugyearU == 0:
                    if debugyear100U == 0:
                        if debugyear400U == 0:
                            if debugday>29:
                                print("您的生日或出生時間有誤")
                            else:
                                if ID >= 1222:
                                    constellation=1
                                    print("您的星座是魔羯座")
                                elif ID >= 1122:
                                    constellation=2
                                    print("您的星座是射手座")
                                elif ID >= 1023:
                                    constellation=3
                                    print("您的星座是天蠍座")
                                elif ID >= 923:
                                    constellation=4
                                    print("您的星座是天秤座")
                                elif ID >= 823:
                                    constellation=5
                                    print("您的星座是處女座")
                                elif ID >= 723:
                                    constellation=6
                                    print("您的星座是獅子座")
                                elif ID >= 621:
                                    constellation=7
                                    print("您的星座是巨蟹座")
                                elif ID >= 521:
                                    constellation=8
                                    print("您的星座是雙子座")
                                elif ID >= 420:
                                    constellation=9
                                    print("您的星座是金牛座")
                                elif ID >= 321:
                                    constellation=10
                                    print("您的星座是牡羊座")
                                elif ID >= 219:
                                    constellation=11
                                    print("您的星座是雙魚座")
                                elif ID >= 120:
                                    constellation=12
                                    print("您的星座是水瓶座")
                                else:
                                    constellation=1
                                    print("您的星座是魔羯座")
                                month=int(birthday[-4:-2])
                                if month==1:
                                    monthcode=640
                                elif month==2:
                                    monthcode=843
                                elif month==3:
                                    monthcode=1033
                                elif month==4:
                                    monthcode=1235
                                elif month==5:
                                    monthcode=1433
                                elif month==6:
                                    monthcode=1636
                                elif month==7:
                                    monthcode=1834
                                elif month==8:
                                    monthcode=2036
                                elif month==9:
                                    monthcode=2238
                                elif month==10:
                                    monthcode=37
                                elif month==11:
                                    monthcode=239
                                else:
                                    monthcode=437
                                day=int(birthday[-2:])
                                daycode=day*4
                                if daycode >= 120:
                                    newdaycode=daycode-120+200
                                elif daycode >= 60:
                                    newdaycode=daycode-60+100
                                else:
                                    newdaycode=daycode
                                A=newdaycode+monthcode
                                mathA=str(A)
                                newA=int(mathA[-2:])
                                if newA >= 60:
                                    newnewA=newA-60+100
                                else:
                                    newnewA=newA
                                if A >= 1000:
                                    Z=int(mathA[0:2])*100
                                else:
                                    Z=int(mathA[0:1])*100
                                finalA=Z+newnewA
                                timecode=int(time)
                                B=finalA+timecode
                                mathB=str(B)
                                newB=int(mathB[-2:])
                                if newB >= 60:
                                    newnewB=newB-60+100
                                else:
                                    newnewB=newB
                                if B >= 1000:
                                    C=int(mathB[0:2])*100
                                else:
                                    C=int(mathB[0:1])*100
                                    
                                D=C+newnewB
                                mathD=str(D)
                                if D >= 1000:
                                    titleD=int(mathD[0:2])
                                else:
                                    titleD=int(mathD[0:1])
                                E=titleD//24
                                F=(titleD-24*E)*100+newnewB
                                if F >= 2313:
                                    print("您的上升星座是巨蟹座")
                                elif F >= 2111:
                                    print("您的上升星座是雙子座")
                                elif F >= 1929:
                                    print("您的上升星座是金牛座")
                                elif F >= 1800:
                                    print("您的上升星座是牡羊座")
                                elif F >= 1630:
                                    print("您的上升星座是雙魚座")
                                elif F >= 1248:
                                    print("您的上升星座是水瓶座")
                                elif F >= 1246:
                                    print("您的上升星座是摩羯座")
                                elif F >= 1030:
                                    print("您的上升星座是射手座")
                                elif F >= 813:
                                    print("您的上升星座是天蠍座")
                                elif F >= 600:
                                    print("您的上升星座是天秤座")
                                elif F >= 346:
                                    print("您的上升星座是處女座")
                                elif F >= 129:
                                    print("您的上升星座是獅子座")
                                else:
                                    print("您的上升星座是巨蟹座")
                                if constellation==1:
                                    print("以下是您的特質:\n正面特質:領導組織、傳統、成熟穩重、目標遠大、堅持理想\n負面特質:工作狂、不知變通、老成世故、易孤獨、功利主義")
                                elif constellation==2:
                                    print("以下是您的特質:\n正面特質:大膽冒險、上進好學、樂觀、幽默風趣、好奇心強\n負面特質:不受拘束、害怕承諾、說話犀利、不穩重、不修邊幅")
                                elif constellation==3:
                                    print("以下是您的特質:\n正面特質:持續力強、權威、迎接挑戰、愛恨分明、敏感\n負面特質：多愁善感、隱藏、冷酷無情、毀滅、鑽牛角尖")
                                elif constellation==4:
                                    print("以下是您的特質:\n正面特質:機智、公平分析、優雅、具迷人魅力、美感與藝術稚子之心\n負面特質:猶豫不決、依賴、善辯、注重外在、懶惰散漫")
                                elif constellation==5:
                                    print("以下是您的特質:\n正面特質:組織分析、謹慎、穩定、負責、擅思考、注重養生\n負面特質:嘮叨、神經質、潔癖、狡猾、挑剔")
                                elif constellation==6:
                                    print("以下是您的特質:\n正面特質:自信、創造、領導、表演、熱心助人、表達\n負面特質:驕傲、奢侈、不喜被忽略、懶惰、無法認同他人")
                                elif constellation==7:
                                    print("以下是您的特質:\n正面特質:溫柔、感性、保護家人、收藏家、敏感、同情心\n負面特質:情緒化、沒安全感、自私、被動、沉溺回憶")
                                elif constellation==8:
                                    print("以下是您的特質:\n正面特質:聰明、反應快、擅溝通、博學、好奇心強、學習力強\n負面特質:不穩定、持續性不高、雙重表現")
                                elif constellation==9:
                                    print("以下是您的特質:\n正面特質:切合實際、確定務實、誠信有決心感官力強\n負面特質:易沒安全感、重視物質、固執倔強、緩慢")
                                elif constellation==10:
                                    print("以下是您的特質:\n正面特質:勇氣、面對挑戰、熱情活躍、好奇心強、具領導力、動作快\n負面特質:好戰、不服輸、沒耐性、自我")    
                                elif constellation==11:
                                    print("以下是您的特質:\n正面特質:想像力強、具有同情心、藝術特質、浪漫多情\n負面特質:不切實際、多愁善感、只說不做、易受傷、軟弱")       
                                else:
                                    print("以下是您的特質:\n正面特質:與眾不同、獨立、冷靜、好奇心強、聰明、人道主義\n負面特質:冷酷、不合群、孤僻、不穩定、變化大、無法捉摸")
                        else:
                            if debugday>28:
                                print("您的生日或出生時間有誤")
                            else:
                                if ID >= 1222:
                                    constellation=1
                                    print("您的星座是魔羯座")
                                elif ID >= 1122:
                                    constellation=2
                                    print("您的星座是射手座")
                                elif ID >= 1023:
                                    constellation=3
                                    print("您的星座是天蠍座")
                                elif ID >= 923:
                                    constellation=4
                                    print("您的星座是天秤座")
                                elif ID >= 823:
                                    constellation=5
                                    print("您的星座是處女座")
                                elif ID >= 723:
                                    constellation=6
                                    print("您的星座是獅子座")
                                elif ID >= 621:
                                    constellation=7
                                    print("您的星座是巨蟹座")
                                elif ID >= 521:
                                    constellation=8
                                    print("您的星座是雙子座")
                                elif ID >= 420:
                                    constellation=9
                                    print("您的星座是金牛座")
                                elif ID >= 321:
                                    constellation=10
                                    print("您的星座是牡羊座")
                                elif ID >= 219:
                                    constellation=11
                                    print("您的星座是雙魚座")
                                elif ID >= 120:
                                    constellation=12
                                    print("您的星座是水瓶座")
                                else:
                                    constellation=1
                                    print("您的星座是魔羯座")
                                month=int(birthday[-4:-2])
                                if month==1:
                                    monthcode=640
                                elif month==2:
                                    monthcode=843
                                elif month==3:
                                    monthcode=1033
                                elif month==4:
                                    monthcode=1235
                                elif month==5:
                                    monthcode=1433
                                elif month==6:
                                    monthcode=1636
                                elif month==7:
                                    monthcode=1834
                                elif month==8:
                                    monthcode=2036
                                elif month==9:
                                    monthcode=2238
                                elif month==10:
                                    monthcode=37
                                elif month==11:
                                    monthcode=239
                                else:
                                    monthcode=437
                                day=int(birthday[-2:])
                                daycode=day*4
                                if daycode >= 120:
                                    newdaycode=daycode-120+200
                                elif daycode >= 60:
                                    newdaycode=daycode-60+100
                                else:
                                    newdaycode=daycode
                                A=newdaycode+monthcode
                                mathA=str(A)
                                newA=int(mathA[-2:])
                                if newA >= 60:
                                    newnewA=newA-60+100
                                else:
                                    newnewA=newA
                                if A >= 1000:
                                    Z=int(mathA[0:2])*100
                                else:
                                    Z=int(mathA[0:1])*100
                                finalA=Z+newnewA
                                timecode=int(time)
                                B=finalA+timecode
                                mathB=str(B)
                                newB=int(mathB[-2:])
                                if newB >= 60:
                                    newnewB=newB-60+100
                                else:
                                    newnewB=newB
                                if B >= 1000:
                                    C=int(mathB[0:2])*100
                                else:
                                    C=int(mathB[0:1])*100
                                    
                                D=C+newnewB
                                mathD=str(D)
                                if D >= 1000:
                                    titleD=int(mathD[0:2])
                                else:
                                    titleD=int(mathD[0:1])
                                E=titleD//24
                                F=(titleD-24*E)*100+newnewB
                                if F >= 2313:
                                    print("您的上升星座是巨蟹座")
                                elif F >= 2111:
                                    print("您的上升星座是雙子座")
                                elif F >= 1929:
                                    print("您的上升星座是金牛座")
                                elif F >= 1800:
                                    print("您的上升星座是牡羊座")
                                elif F >= 1630:
                                    print("您的上升星座是雙魚座")
                                elif F >= 1248:
                                    print("您的上升星座是水瓶座")
                                elif F >= 1246:
                                    print("您的上升星座是摩羯座")
                                elif F >= 1030:
                                    print("您的上升星座是射手座")
                                elif F >= 813:
                                    print("您的上升星座是天蠍座")
                                elif F >= 600:
                                    print("您的上升星座是天秤座")
                                elif F >= 346:
                                    print("您的上升星座是處女座")
                                elif F >= 129:
                                    print("您的上升星座是獅子座")
                                else:
                                    print("您的上升星座是巨蟹座")
                                if constellation==1:
                                    print("以下是您的特質:\n正面特質:領導組織、傳統、成熟穩重、目標遠大、堅持理想\n負面特質:工作狂、不知變通、老成世故、易孤獨、功利主義")
                                elif constellation==2:
                                    print("以下是您的特質:\n正面特質:大膽冒險、上進好學、樂觀、幽默風趣、好奇心強\n負面特質:不受拘束、害怕承諾、說話犀利、不穩重、不修邊幅")
                                elif constellation==3:
                                    print("以下是您的特質:\n正面特質:持續力強、權威、迎接挑戰、愛恨分明、敏感\n負面特質：多愁善感、隱藏、冷酷無情、毀滅、鑽牛角尖")
                                elif constellation==4:
                                    print("以下是您的特質:\n正面特質:機智、公平分析、優雅、具迷人魅力、美感與藝術稚子之心\n負面特質:猶豫不決、依賴、善辯、注重外在、懶惰散漫")
                                elif constellation==5:
                                    print("以下是您的特質:\n正面特質:組織分析、謹慎、穩定、負責、擅思考、注重養生\n負面特質:嘮叨、神經質、潔癖、狡猾、挑剔")
                                elif constellation==6:
                                    print("以下是您的特質:\n正面特質:自信、創造、領導、表演、熱心助人、表達\n負面特質:驕傲、奢侈、不喜被忽略、懶惰、無法認同他人")
                                elif constellation==7:
                                    print("以下是您的特質:\n正面特質:溫柔、感性、保護家人、收藏家、敏感、同情心\n負面特質:情緒化、沒安全感、自私、被動、沉溺回憶")
                                elif constellation==8:
                                    print("以下是您的特質:\n正面特質:聰明、反應快、擅溝通、博學、好奇心強、學習力強\n負面特質:不穩定、持續性不高、雙重表現")
                                elif constellation==9:
                                    print("以下是您的特質:\n正面特質:切合實際、確定務實、誠信有決心感官力強\n負面特質:易沒安全感、重視物質、固執倔強、緩慢")
                                elif constellation==10:
                                    print("以下是您的特質:\n正面特質:勇氣、面對挑戰、熱情活躍、好奇心強、具領導力、動作快\n負面特質:好戰、不服輸、沒耐性、自我")    
                                elif constellation==11:
                                    print("以下是您的特質:\n正面特質:想像力強、具有同情心、藝術特質、浪漫多情\n負面特質:不切實際、多愁善感、只說不做、易受傷、軟弱")       
                                else:
                                    print("以下是您的特質:\n正面特質:與眾不同、獨立、冷靜、好奇心強、聰明、人道主義\n負面特質:冷酷、不合群、孤僻、不穩定、變化大、無法捉摸")  
                    else:
                        if debugday>29:
                            print("您的生日或出生時間有誤")
                        else:
                            if ID >= 1222:
                                constellation=1
                                print("您的星座是魔羯座")
                            elif ID >= 1122:
                                constellation=2
                                print("您的星座是射手座")
                            elif ID >= 1023:
                                constellation=3
                                print("您的星座是天蠍座")
                            elif ID >= 923:
                                constellation=4
                                print("您的星座是天秤座")
                            elif ID >= 823:
                                constellation=5
                                print("您的星座是處女座")
                            elif ID >= 723:
                                constellation=6
                                print("您的星座是獅子座")
                            elif ID >= 621:
                                constellation=7
                                print("您的星座是巨蟹座")
                            elif ID >= 521:
                                constellation=8
                                print("您的星座是雙子座")
                            elif ID >= 420:
                                constellation=9
                                print("您的星座是金牛座")
                            elif ID >= 321:
                                constellation=10
                                print("您的星座是牡羊座")
                            elif ID >= 219:
                                constellation=11
                                print("您的星座是雙魚座")
                            elif ID >= 120:
                                constellation=12
                                print("您的星座是水瓶座")
                            else:
                                constellation=1
                                print("您的星座是魔羯座")
                            month=int(birthday[-4:-2])
                            if month==1:
                                monthcode=640
                            elif month==2:
                                monthcode=843
                            elif month==3:
                                monthcode=1033
                            elif month==4:
                                monthcode=1235
                            elif month==5:
                                monthcode=1433
                            elif month==6:
                                monthcode=1636
                            elif month==7:
                                monthcode=1834
                            elif month==8:
                                monthcode=2036
                            elif month==9:
                                monthcode=2238
                            elif month==10:
                                monthcode=37
                            elif month==11:
                                monthcode=239
                            else:
                                monthcode=437
                            day=int(birthday[-2:])
                            daycode=day*4
                            if daycode >= 120:
                                newdaycode=daycode-120+200
                            elif daycode >= 60:
                                newdaycode=daycode-60+100
                            else:
                                newdaycode=daycode
                            A=newdaycode+monthcode
                            mathA=str(A)
                            newA=int(mathA[-2:])
                            if newA >= 60:
                                newnewA=newA-60+100
                            else:
                                newnewA=newA
                            if A >= 1000:
                                Z=int(mathA[0:2])*100
                            else:
                                Z=int(mathA[0:1])*100
                            finalA=Z+newnewA
                            timecode=int(time)
                            B=finalA+timecode
                            mathB=str(B)
                            newB=int(mathB[-2:])
                            if newB >= 60:
                                newnewB=newB-60+100
                            else:
                                newnewB=newB
                            if B >= 1000:
                                C=int(mathB[0:2])*100
                            else:
                                C=int(mathB[0:1])*100
                                
                            D=C+newnewB
                            mathD=str(D)
                            if D >= 1000:
                                titleD=int(mathD[0:2])
                            else:
                                titleD=int(mathD[0:1])
                            E=titleD//24
                            F=(titleD-24*E)*100+newnewB
                            if F >= 2313:
                                print("您的上升星座是巨蟹座")
                            elif F >= 2111:
                                print("您的上升星座是雙子座")
                            elif F >= 1929:
                                print("您的上升星座是金牛座")
                            elif F >= 1800:
                                print("您的上升星座是牡羊座")
                            elif F >= 1630:
                                print("您的上升星座是雙魚座")
                            elif F >= 1248:
                                print("您的上升星座是水瓶座")
                            elif F >= 1246:
                                print("您的上升星座是摩羯座")
                            elif F >= 1030:
                                print("您的上升星座是射手座")
                            elif F >= 813:
                                print("您的上升星座是天蠍座")
                            elif F >= 600:
                                print("您的上升星座是天秤座")
                            elif F >= 346:
                                print("您的上升星座是處女座")
                            elif F >= 129:
                                print("您的上升星座是獅子座")
                            else:
                                print("您的上升星座是巨蟹座")
                            if constellation==1:
                                print("以下是您的特質:\n正面特質:領導組織、傳統、成熟穩重、目標遠大、堅持理想\n負面特質:工作狂、不知變通、老成世故、易孤獨、功利主義")
                            elif constellation==2:
                                print("以下是您的特質:\n正面特質:大膽冒險、上進好學、樂觀、幽默風趣、好奇心強\n負面特質:不受拘束、害怕承諾、說話犀利、不穩重、不修邊幅")
                            elif constellation==3:
                                print("以下是您的特質:\n正面特質:持續力強、權威、迎接挑戰、愛恨分明、敏感\n負面特質：多愁善感、隱藏、冷酷無情、毀滅、鑽牛角尖")
                            elif constellation==4:
                                print("以下是您的特質:\n正面特質:機智、公平分析、優雅、具迷人魅力、美感與藝術稚子之心\n負面特質:猶豫不決、依賴、善辯、注重外在、懶惰散漫")
                            elif constellation==5:
                                print("以下是您的特質:\n正面特質:組織分析、謹慎、穩定、負責、擅思考、注重養生\n負面特質:嘮叨、神經質、潔癖、狡猾、挑剔")
                            elif constellation==6:
                                print("以下是您的特質:\n正面特質:自信、創造、領導、表演、熱心助人、表達\n負面特質:驕傲、奢侈、不喜被忽略、懶惰、無法認同他人")
                            elif constellation==7:
                                print("以下是您的特質:\n正面特質:溫柔、感性、保護家人、收藏家、敏感、同情心\n負面特質:情緒化、沒安全感、自私、被動、沉溺回憶")
                            elif constellation==8:
                                print("以下是您的特質:\n正面特質:聰明、反應快、擅溝通、博學、好奇心強、學習力強\n負面特質:不穩定、持續性不高、雙重表現")
                            elif constellation==9:
                                print("以下是您的特質:\n正面特質:切合實際、確定務實、誠信有決心感官力強\n負面特質:易沒安全感、重視物質、固執倔強、緩慢")
                            elif constellation==10:
                                print("以下是您的特質:\n正面特質:勇氣、面對挑戰、熱情活躍、好奇心強、具領導力、動作快\n負面特質:好戰、不服輸、沒耐性、自我")    
                            elif constellation==11:
                                print("以下是您的特質:\n正面特質:想像力強、具有同情心、藝術特質、浪漫多情\n負面特質:不切實際、多愁善感、只說不做、易受傷、軟弱")       
                            else:
                                print("以下是您的特質:\n正面特質:與眾不同、獨立、冷靜、好奇心強、聰明、人道主義\n負面特質:冷酷、不合群、孤僻、不穩定、變化大、無法捉摸")
                else:
                    if debugday>28:
                        print("您的生日或出生時間有誤")
                    else:
                        if ID >= 1222:
                            constellation=1
                            print("您的星座是魔羯座")
                        elif ID >= 1122:
                            constellation=2
                            print("您的星座是射手座")
                        elif ID >= 1023:
                            constellation=3
                            print("您的星座是天蠍座")
                        elif ID >= 923:
                            constellation=4
                            print("您的星座是天秤座")
                        elif ID >= 823:
                            constellation=5
                            print("您的星座是處女座")
                        elif ID >= 723:
                            constellation=6
                            print("您的星座是獅子座")
                        elif ID >= 621:
                            constellation=7
                            print("您的星座是巨蟹座")
                        elif ID >= 521:
                            constellation=8
                            print("您的星座是雙子座")
                        elif ID >= 420:
                            constellation=9
                            print("您的星座是金牛座")
                        elif ID >= 321:
                            constellation=10
                            print("您的星座是牡羊座")
                        elif ID >= 219:
                            constellation=11
                            print("您的星座是雙魚座")
                        elif ID >= 120:
                            constellation=12
                            print("您的星座是水瓶座")
                        else:
                            constellation=1
                            print("您的星座是魔羯座")
                        month=int(birthday[-4:-2])
                        if month==1:
                            monthcode=640
                        elif month==2:
                            monthcode=843
                        elif month==3:
                            monthcode=1033
                        elif month==4:
                            monthcode=1235
                        elif month==5:
                            monthcode=1433
                        elif month==6:
                            monthcode=1636
                        elif month==7:
                            monthcode=1834
                        elif month==8:
                            monthcode=2036
                        elif month==9:
                            monthcode=2238
                        elif month==10:
                            monthcode=37
                        elif month==11:
                            monthcode=239
                        else:
                            monthcode=437
                        day=int(birthday[-2:])
                        daycode=day*4
                        if daycode >= 120:
                            newdaycode=daycode-120+200
                        elif daycode >= 60:
                            newdaycode=daycode-60+100
                        else:
                            newdaycode=daycode
                        A=newdaycode+monthcode
                        mathA=str(A)
                        newA=int(mathA[-2:])
                        if newA >= 60:
                            newnewA=newA-60+100
                        else:
                            newnewA=newA
                        if A >= 1000:
                            Z=int(mathA[0:2])*100
                        else:
                            Z=int(mathA[0:1])*100
                        finalA=Z+newnewA
                        timecode=int(time)
                        B=finalA+timecode
                        mathB=str(B)
                        newB=int(mathB[-2:])
                        if newB >= 60:
                            newnewB=newB-60+100
                        else:
                            newnewB=newB
                        if B >= 1000:
                            C=int(mathB[0:2])*100
                        else:
                            C=int(mathB[0:1])*100
                            
                        D=C+newnewB
                        mathD=str(D)
                        if D >= 1000:
                            titleD=int(mathD[0:2])
                        else:
                            titleD=int(mathD[0:1])
                        E=titleD//24
                        F=(titleD-24*E)*100+newnewB
                        if F >= 2313:
                            print("您的上升星座是巨蟹座")
                        elif F >= 2111:
                            print("您的上升星座是雙子座")
                        elif F >= 1929:
                            print("您的上升星座是金牛座")
                        elif F >= 1800:
                            print("您的上升星座是牡羊座")
                        elif F >= 1630:
                            print("您的上升星座是雙魚座")
                        elif F >= 1248:
                            print("您的上升星座是水瓶座")
                        elif F >= 1246:
                            print("您的上升星座是摩羯座")
                        elif F >= 1030:
                            print("您的上升星座是射手座")
                        elif F >= 813:
                            print("您的上升星座是天蠍座")
                        elif F >= 600:
                            print("您的上升星座是天秤座")
                        elif F >= 346:
                            print("您的上升星座是處女座")
                        elif F >= 129:
                            print("您的上升星座是獅子座")
                        else:
                            print("您的上升星座是巨蟹座")
                        if constellation==1:
                            print("以下是您的特質:\n正面特質:領導組織、傳統、成熟穩重、目標遠大、堅持理想\n負面特質:工作狂、不知變通、老成世故、易孤獨、功利主義")
                        elif constellation==2:
                            print("以下是您的特質:\n正面特質:大膽冒險、上進好學、樂觀、幽默風趣、好奇心強\n負面特質:不受拘束、害怕承諾、說話犀利、不穩重、不修邊幅")
                        elif constellation==3:
                            print("以下是您的特質:\n正面特質:持續力強、權威、迎接挑戰、愛恨分明、敏感\n負面特質：多愁善感、隱藏、冷酷無情、毀滅、鑽牛角尖")
                        elif constellation==4:
                            print("以下是您的特質:\n正面特質:機智、公平分析、優雅、具迷人魅力、美感與藝術稚子之心\n負面特質:猶豫不決、依賴、善辯、注重外在、懶惰散漫")
                        elif constellation==5:
                            print("以下是您的特質:\n正面特質:組織分析、謹慎、穩定、負責、擅思考、注重養生\n負面特質:嘮叨、神經質、潔癖、狡猾、挑剔")
                        elif constellation==6:
                            print("以下是您的特質:\n正面特質:自信、創造、領導、表演、熱心助人、表達\n負面特質:驕傲、奢侈、不喜被忽略、懶惰、無法認同他人")
                        elif constellation==7:
                            print("以下是您的特質:\n正面特質:溫柔、感性、保護家人、收藏家、敏感、同情心\n負面特質:情緒化、沒安全感、自私、被動、沉溺回憶")
                        elif constellation==8:
                            print("以下是您的特質:\n正面特質:聰明、反應快、擅溝通、博學、好奇心強、學習力強\n負面特質:不穩定、持續性不高、雙重表現")
                        elif constellation==9:
                            print("以下是您的特質:\n正面特質:切合實際、確定務實、誠信有決心感官力強\n負面特質:易沒安全感、重視物質、固執倔強、緩慢")
                        elif constellation==10:
                            print("以下是您的特質:\n正面特質:勇氣、面對挑戰、熱情活躍、好奇心強、具領導力、動作快\n負面特質:好戰、不服輸、沒耐性、自我")    
                        elif constellation==11:
                            print("以下是您的特質:\n正面特質:想像力強、具有同情心、藝術特質、浪漫多情\n負面特質:不切實際、多愁善感、只說不做、易受傷、軟弱")       
                        else:
                            print("以下是您的特質:\n正面特質:與眾不同、獨立、冷靜、好奇心強、聰明、人道主義\n負面特質:冷酷、不合群、孤僻、不穩定、變化大、無法捉摸")  
            elif debugmonth in (1,3,5,7,8,10,12):
                if debugday>31:
                    print("您的生日或出生時間有誤")
                else:
                    if ID >= 1222:
                        constellation=1
                        print("您的星座是魔羯座")
                    elif ID >= 1122:
                        constellation=2
                        print("您的星座是射手座")
                    elif ID >= 1023:
                        constellation=3
                        print("您的星座是天蠍座")
                    elif ID >= 923:
                        constellation=4
                        print("您的星座是天秤座")
                    elif ID >= 823:
                        constellation=5
                        print("您的星座是處女座")
                    elif ID >= 723:
                        constellation=6
                        print("您的星座是獅子座")
                    elif ID >= 621:
                        constellation=7
                        print("您的星座是巨蟹座")
                    elif ID >= 521:
                        constellation=8
                        print("您的星座是雙子座")
                    elif ID >= 420:
                        constellation=9
                        print("您的星座是金牛座")
                    elif ID >= 321:
                        constellation=10
                        print("您的星座是牡羊座")
                    elif ID >= 219:
                        constellation=11
                        print("您的星座是雙魚座")
                    elif ID >= 120:
                        constellation=12
                        print("您的星座是水瓶座")
                    else:
                        constellation=1
                        print("您的星座是魔羯座")
                    month=int(birthday[-4:-2])
                    if month==1:
                        monthcode=640
                    elif month==2:
                        monthcode=843
                    elif month==3:
                        monthcode=1033
                    elif month==4:
                        monthcode=1235
                    elif month==5:
                        monthcode=1433
                    elif month==6:
                        monthcode=1636
                    elif month==7:
                        monthcode=1834
                    elif month==8:
                        monthcode=2036
                    elif month==9:
                        monthcode=2238
                    elif month==10:
                        monthcode=37
                    elif month==11:
                        monthcode=239
                    else:
                        monthcode=437
                    day=int(birthday[-2:])
                    daycode=day*4
                    if daycode >= 120:
                        newdaycode=daycode-120+200
                    elif daycode >= 60:
                        newdaycode=daycode-60+100
                    else:
                        newdaycode=daycode
                    A=newdaycode+monthcode
                    mathA=str(A)
                    newA=int(mathA[-2:])
                    if newA >= 60:
                        newnewA=newA-60+100
                    else:
                        newnewA=newA
                    if A >= 1000:
                        Z=int(mathA[0:2])*100
                    else:
                        Z=int(mathA[0:1])*100
                    finalA=Z+newnewA
                    timecode=int(time)
                    B=finalA+timecode
                    mathB=str(B)
                    newB=int(mathB[-2:])
                    if newB >= 60:
                        newnewB=newB-60+100
                    else:
                        newnewB=newB
                    if B >= 1000:
                        C=int(mathB[0:2])*100
                    else:
                        C=int(mathB[0:1])*100
                        
                    D=C+newnewB
                    mathD=str(D)
                    if D >= 1000:
                        titleD=int(mathD[0:2])
                    else:
                        titleD=int(mathD[0:1])
                    E=titleD//24
                    F=(titleD-24*E)*100+newnewB
                    if F >= 2313:
                        print("您的上升星座是巨蟹座")
                    elif F >= 2111:
                        print("您的上升星座是雙子座")
                    elif F >= 1929:
                        print("您的上升星座是金牛座")
                    elif F >= 1800:
                        print("您的上升星座是牡羊座")
                    elif F >= 1630:
                        print("您的上升星座是雙魚座")
                    elif F >= 1248:
                        print("您的上升星座是水瓶座")
                    elif F >= 1246:
                        print("您的上升星座是摩羯座")
                    elif F >= 1030:
                        print("您的上升星座是射手座")
                    elif F >= 813:
                        print("您的上升星座是天蠍座")
                    elif F >= 600:
                        print("您的上升星座是天秤座")
                    elif F >= 346:
                        print("您的上升星座是處女座")
                    elif F >= 129:
                        print("您的上升星座是獅子座")
                    else:
                        print("您的上升星座是巨蟹座")
                    if constellation==1:
                        print("以下是您的特質:\n正面特質:領導組織、傳統、成熟穩重、目標遠大、堅持理想\n負面特質:工作狂、不知變通、老成世故、易孤獨、功利主義")
                    elif constellation==2:
                        print("以下是您的特質:\n正面特質:大膽冒險、上進好學、樂觀、幽默風趣、好奇心強\n負面特質:不受拘束、害怕承諾、說話犀利、不穩重、不修邊幅")
                    elif constellation==3:
                        print("以下是您的特質:\n正面特質:持續力強、權威、迎接挑戰、愛恨分明、敏感\n負面特質：多愁善感、隱藏、冷酷無情、毀滅、鑽牛角尖")
                    elif constellation==4:
                        print("以下是您的特質:\n正面特質:機智、公平分析、優雅、具迷人魅力、美感與藝術稚子之心\n負面特質:猶豫不決、依賴、善辯、注重外在、懶惰散漫")
                    elif constellation==5:
                        print("以下是您的特質:\n正面特質:組織分析、謹慎、穩定、負責、擅思考、注重養生\n負面特質:嘮叨、神經質、潔癖、狡猾、挑剔")
                    elif constellation==6:
                        print("以下是您的特質:\n正面特質:自信、創造、領導、表演、熱心助人、表達\n負面特質:驕傲、奢侈、不喜被忽略、懶惰、無法認同他人")
                    elif constellation==7:
                        print("以下是您的特質:\n正面特質:溫柔、感性、保護家人、收藏家、敏感、同情心\n負面特質:情緒化、沒安全感、自私、被動、沉溺回憶")
                    elif constellation==8:
                        print("以下是您的特質:\n正面特質:聰明、反應快、擅溝通、博學、好奇心強、學習力強\n負面特質:不穩定、持續性不高、雙重表現")
                    elif constellation==9:
                        print("以下是您的特質:\n正面特質:切合實際、確定務實、誠信有決心感官力強\n負面特質:易沒安全感、重視物質、固執倔強、緩慢")
                    elif constellation==10:
                        print("以下是您的特質:\n正面特質:勇氣、面對挑戰、熱情活躍、好奇心強、具領導力、動作快\n負面特質:好戰、不服輸、沒耐性、自我")    
                    elif constellation==11:
                        print("以下是您的特質:\n正面特質:想像力強、具有同情心、藝術特質、浪漫多情\n負面特質:不切實際、多愁善感、只說不做、易受傷、軟弱")       
                    else:
                        print("以下是您的特質:\n正面特質:與眾不同、獨立、冷靜、好奇心強、聰明、人道主義\n負面特質:冷酷、不合群、孤僻、不穩定、變化大、無法捉摸")  
            else:
                if debugday>30:
                    print("您的生日或出生時間有誤")
                else:
                    if ID >= 1222:
                        constellation=1
                        print("您的星座是魔羯座")
                    elif ID >= 1122:
                        constellation=2
                        print("您的星座是射手座")
                    elif ID >= 1023:
                        constellation=3
                        print("您的星座是天蠍座")
                    elif ID >= 923:
                        constellation=4
                        print("您的星座是天秤座")
                    elif ID >= 823:
                        constellation=5
                        print("您的星座是處女座")
                    elif ID >= 723:
                        constellation=6
                        print("您的星座是獅子座")
                    elif ID >= 621:
                        constellation=7
                        print("您的星座是巨蟹座")
                    elif ID >= 521:
                        constellation=8
                        print("您的星座是雙子座")
                    elif ID >= 420:
                        constellation=9
                        print("您的星座是金牛座")
                    elif ID >= 321:
                        constellation=10
                        print("您的星座是牡羊座")
                    elif ID >= 219:
                        constellation=11
                        print("您的星座是雙魚座")
                    elif ID >= 120:
                        constellation=12
                        print("您的星座是水瓶座")
                    else:
                        constellation=1
                        print("您的星座是魔羯座")
                    month=int(birthday[-4:-2])
                    if month==1:
                        monthcode=640
                    elif month==2:
                        monthcode=843
                    elif month==3:
                        monthcode=1033
                    elif month==4:
                        monthcode=1235
                    elif month==5:
                        monthcode=1433
                    elif month==6:
                        monthcode=1636
                    elif month==7:
                        monthcode=1834
                    elif month==8:
                        monthcode=2036
                    elif month==9:
                        monthcode=2238
                    elif month==10:
                        monthcode=37
                    elif month==11:
                        monthcode=239
                    else:
                        monthcode=437
                    day=int(birthday[-2:])
                    daycode=day*4
                    if daycode >= 120:
                        newdaycode=daycode-120+200
                    elif daycode >= 60:
                        newdaycode=daycode-60+100
                    else:
                        newdaycode=daycode
                    A=newdaycode+monthcode
                    mathA=str(A)
                    newA=int(mathA[-2:])
                    if newA >= 60:
                        newnewA=newA-60+100
                    else:
                        newnewA=newA
                    if A >= 1000:
                        Z=int(mathA[0:2])*100
                    else:
                        Z=int(mathA[0:1])*100
                    finalA=Z+newnewA
                    timecode=int(time)
                    B=finalA+timecode
                    mathB=str(B)
                    newB=int(mathB[-2:])
                    if newB >= 60:
                        newnewB=newB-60+100
                    else:
                        newnewB=newB
                    if B >= 1000:
                        C=int(mathB[0:2])*100
                    else:
                        C=int(mathB[0:1])*100
                        
                    D=C+newnewB
                    mathD=str(D)
                    if D >= 1000:
                        titleD=int(mathD[0:2])
                    else:
                        titleD=int(mathD[0:1])
                    E=titleD//24
                    F=(titleD-24*E)*100+newnewB
                    if F >= 2313:
                        print("您的上升星座是巨蟹座")
                    elif F >= 2111:
                        print("您的上升星座是雙子座")
                    elif F >= 1929:
                        print("您的上升星座是金牛座")
                    elif F >= 1800:
                        print("您的上升星座是牡羊座")
                    elif F >= 1630:
                        print("您的上升星座是雙魚座")
                    elif F >= 1248:
                        print("您的上升星座是水瓶座")
                    elif F >= 1246:
                        print("您的上升星座是摩羯座")
                    elif F >= 1030:
                        print("您的上升星座是射手座")
                    elif F >= 813:
                        print("您的上升星座是天蠍座")
                    elif F >= 600:
                        print("您的上升星座是天秤座")
                    elif F >= 346:
                        print("您的上升星座是處女座")
                    elif F >= 129:
                        print("您的上升星座是獅子座")
                    else:
                        print("您的上升星座是巨蟹座")
                    if constellation==1:
                        print("以下是您的特質:\n正面特質:領導組織、傳統、成熟穩重、目標遠大、堅持理想\n負面特質:工作狂、不知變通、老成世故、易孤獨、功利主義")
                    elif constellation==2:
                        print("以下是您的特質:\n正面特質:大膽冒險、上進好學、樂觀、幽默風趣、好奇心強\n負面特質:不受拘束、害怕承諾、說話犀利、不穩重、不修邊幅")
                    elif constellation==3:
                        print("以下是您的特質:\n正面特質:持續力強、權威、迎接挑戰、愛恨分明、敏感\n負面特質：多愁善感、隱藏、冷酷無情、毀滅、鑽牛角尖")
                    elif constellation==4:
                        print("以下是您的特質:\n正面特質:機智、公平分析、優雅、具迷人魅力、美感與藝術稚子之心\n負面特質:猶豫不決、依賴、善辯、注重外在、懶惰散漫")
                    elif constellation==5:
                        print("以下是您的特質:\n正面特質:組織分析、謹慎、穩定、負責、擅思考、注重養生\n負面特質:嘮叨、神經質、潔癖、狡猾、挑剔")
                    elif constellation==6:
                        print("以下是您的特質:\n正面特質:自信、創造、領導、表演、熱心助人、表達\n負面特質:驕傲、奢侈、不喜被忽略、懶惰、無法認同他人")
                    elif constellation==7:
                        print("以下是您的特質:\n正面特質:溫柔、感性、保護家人、收藏家、敏感、同情心\n負面特質:情緒化、沒安全感、自私、被動、沉溺回憶")
                    elif constellation==8:
                        print("以下是您的特質:\n正面特質:聰明、反應快、擅溝通、博學、好奇心強、學習力強\n負面特質:不穩定、持續性不高、雙重表現")
                    elif constellation==9:
                        print("以下是您的特質:\n正面特質:切合實際、確定務實、誠信有決心感官力強\n負面特質:易沒安全感、重視物質、固執倔強、緩慢")
                    elif constellation==10:
                        print("以下是您的特質:\n正面特質:勇氣、面對挑戰、熱情活躍、好奇心強、具領導力、動作快\n負面特質:好戰、不服輸、沒耐性、自我")    
                    elif constellation==11:
                        print("以下是您的特質:\n正面特質:想像力強、具有同情心、藝術特質、浪漫多情\n負面特質:不切實際、多愁善感、只說不做、易受傷、軟弱")       
                    else:
                        print("以下是您的特質:\n正面特質:與眾不同、獨立、冷靜、好奇心強、聰明、人道主義\n負面特質:冷酷、不合群、孤僻、不穩定、變化大、無法捉摸")  
else:
    print("您的生日或出生時間有誤")
