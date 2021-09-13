import requests
import json



################## 100대 지표 전체 추출 ############## 
file1 = open("EconIndex_100.json", 'a', encoding = "UTF-8")   # append

# API 연결
url = "http://ecos.bok.or.kr/api/KeyStatisticList/Z1846GHW4KP8V2BESGE5/json/kr/1/100"   # 100대 통계지표
response = requests.get(url)


# "row" 부분만 추출(필요 없는 header 제거)
a = response.json()
content = a['KeyStatisticList']['row'] 

content_str = json.dumps(content, ensure_ascii = False)   # dict -> string   (to apply ".write" ftn)

file1.write(content_str)
file1.close() 


# replace "][" with ","
start = open("EconIndex_100.json", "r", encoding="UTF-8")

for line in start:
    line = line.strip()
    changes = line.replace("][", ",")
start.close()

end = open("EconIndex_100.json", "w", encoding="UTF-8")
end.write(changes)
end.close()






################## 필요한 Index 추출 ###################
file2 = open("EconIndex_Key.json", 'a', encoding = "UTF-8")   # append


# API 연결
url = "http://ecos.bok.or.kr/api/KeyStatisticList/Z1846GHW4KP8V2BESGE5/json/kr/1/100"   # 100대 통계지표
response = requests.get(url)


# "row" 부분만 추출(필요 없는 header 제거)
b = response.json()
content = b['KeyStatisticList']['row']  


# 필요한 Index 정보만 추출
KeyIndex = []
Index_list = ["M1(협의통화, 평잔)", "M2(광의통화, 평잔)", "기준금리", "원/달러 환율(매매기준율)", 
              "원/위안 환율(매매기준율)", "원/엔(100엔) 환율", "원/유로 환율"]
for i in content:
    if i.get("KEYSTAT_NAME") in Index_list:
        KeyIndex.append(i)

KeyIndex_str = json.dumps(KeyIndex, ensure_ascii = False)   # dict -> string   (to apply ".write" ftn)

file2.write(KeyIndex_str)
file2.close() 



# replace "][" with "," 
start = open("EconIndex_Key.json", "r", encoding="UTF-8")

for line in start:
    line = line.strip()
    changes = line.replace("][", ",")
start.close()

end = open("EconIndex_Key.json", "w", encoding="UTF-8")
end.write(changes)
end.close()


