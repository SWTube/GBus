import requests
import schedule
import time
import pandas as pd

# 시간 정보 저장할 리스트 생성
bus_time = []

def find_period():
    # api 사용 url
    url = "http://apis.data.go.kr/6410000/busarrivalservice/getBusArrivalItem"

    bio = {"serviceKey" : "bwUUK6MEA6GnqDpo2ZS9ChN4VZ1nkUPXrryU80XxUcLqxB62pIGIPWXNdyzqgT20BHrw8zxWWk9rqiSQwTrbnQ==",
                "stationId" : "228000704", "routeId" : "200000115"}

    bio_res = requests.get(url, params=bio)

    # xml문서 string으로 변환
    station = str(bio_res.content, "utf-8")


    #버스 정보 존재 시 시간 입력
    if "정상적으로 처리되었습니다" in station:
        bus_time.append(time.ctime())
        print("there is info at :", time.ctime(), "(process :", round((count+1)/ 20, 2), "%)")
    else:
        print("there is no info now (process :", round((count+1)/ 20, 2), "%)")


# 1초마다 반복
schedule.every(1).seconds.do(find_period)

count = 0
# 2000초 동안 반복 실행
while count < 2000:
    schedule.run_pending()
    time.sleep(1)
    count += 1

# 엑셀파일로 데이터 저장
bus_time_data = {"time" : bus_time}

bus_time_data = pd.DataFrame(bus_time_data)
bus_time_data.to_excel(excel_writer="/Users/yang-jinyoung/Desktop/동아리 대항전/period_5100_5.xlsx")
print("complete!")