"""
學習目標:
1. 學習撰寫模組，在python，一個檔案或是一個資料夾都可被視為一個模組。
2. 用test_case來測試自己寫的東西對不對
核心概念:先畫靶再射箭，先設定好自己要的結果，再開始coding。
"""


def get_constellation(month, day):
    """
    根據生日回傳正確的星座
    牡羊座	3月21日～4月20日
    金牛座	4月21日～5月20日
    雙子座	5月21日～6月20日
    巨蟹座	6月21日～7月22日
    獅子座	7月23日～8月22日
    處女座	8月23日～9月22日
    天秤座	9月23日～10月22日
    天蠍座	10月23日～11月22日
    射手座	11月23日～12月22日
    魔羯座	12月23日～1月21日
    水瓶座	1月22日～2月19日
    雙魚座	2月20日～3月20日
    """
    if len(str(day)) == 1:
        day = "0" + str(day)
    else:
        day = str(day)
    md = int(str(month) + day)
    
    if (md <= 121) or (md >= 1223):
        stellation = "魔羯座"
    elif md <= 219:
        stellation = "水瓶座"
    elif md <= 320:
        stellation = "雙魚座"
    elif md <= 420:
        stellation = "牡羊座"
    elif md <= 520:
        stellation = "金牛座"
    elif md <= 620:
        stellation = "雙子座"
    elif md <= 722:
        stellation = "巨蟹座"
    elif md <= 822:
        stellation = "獅子座"
    elif md <= 922:
        stellation = "處女座"
    elif md <= 1022:
        stellation = "天秤座"
    elif md <= 1122:
        stellation = "天蠍座"
    elif md <= 1222:
        stellation = "射手座"
        
    return stellation


def get_each_number(number):
    """
    輸入一個正整數，然後將每一位數分開。
    ex get_each_number(1920) 
    return [1,9,2,0]
    """
    str_number = str(number)
    result = []
    for i in range(len(str_number)):  
        result.append(int(str_number[i]))

    return result


def get_life_number(year=1900, month=1, day=1):
    """
    會回傳一個生命靈數，生命靈數的計算方式是出生年月日的每一個數字的總和，不斷加總至個位數。
    ex 1995 12 13 -> 1+9+9+5+1+2+1+3 = 31 -> 3+1 =4
    這樣生命靈數就是4
    """
    total_num = 0
    life_num = 0
    
    while year != 0:
        total_num += year % 10
        year = year // 10
    
    while month != 0:
        total_num += month % 10
        month = month // 10
    while day != 0:
        total_num += day % 10
        day = day // 10
    
    while total_num != 0:
        life_num += total_num % 10
        total_num = total_num //10
        
    return life_num