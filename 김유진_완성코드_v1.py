import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import sklearn.preprocessing

bus_time=[]
serviceKey='Jw+++HTzL3V8lfZPcQPb5jB5Rae2NH3BYowjBY+cgMIA1yDcwJNfmtfO+E+O+whPsGCGbJmmpf/X904L4uwGIw=='
p5100 ={'serviceKey' :serviceKey,
             'routeId':'200000115','stationId':'228000703'}#5100 외대
p1112 ={'serviceKey' : serviceKey,
         'routeId':'234000016','stationId':'228000703'}#1112 외대

def repet(params): 
    url = 'http://apis.data.go.kr/6410000/busarrivalservice/getBusArrivalItem'
    response = requests.get(url, params=params);
    soup=BeautifulSoup(response.text,'xml')
    return soup

def current_buses(): # 사색의 광장에 버스가 도착했을 때, 운행중인 같은 노선의 버스들의 위치(정류장)를 수집  
    url = 'http://apis.data.go.kr/6410000/buslocationservice/getBusLocationList'
    params ={'serviceKey' : serviceKey,
              'routeId':p1112['routeId']}#1112번 노선id
    response=requests.get(url,params=params)
    soup=BeautifulSoup(response.text,'xml')
    locations=sorted([int(x.stationSeq.text) for x in soup.find_all('busLocationList')])
    return locations
  
def trim_data(df,FileName):
    df['시간'] = df['시간'].apply(pd.to_datetime) # string 값인 시간을 datetime객체로 바꾼다. 
    df['hour']=df['시간'].dt.hour
    df['minute']=df['시간'].dt.minute
    df['second']=df['시간'].dt.second
    df['day'] = df['시간'].dt.weekday #월요일 0 화요일 1

    # unpack list values
    mb = sklearn.preprocessing.MultiLabelBinarizer()
    if isinstance(df['운행중인 다른 버스들의 위치'].iloc[0], str):
        df['운행중인 다른 버스들의 위치'] = df['운행중인 다른 버스들의 위치'].apply(eval)
    entity = mb.fit_transform(df['운행중인 다른 버스들의 위치']) 
    lsts=pd.DataFrame(entity,columns=mb.classes_)
    lsts.columns=[f'station{x}' for x in lsts.columns]
    df=pd.concat([df,lsts],axis=1,sort=False).reset_index(drop=True)


    df=df.drop(["운행중인 다른 버스들의 위치"],axis=1)
    
    batch=df.index[df.arrived==1] # 마지막 row 값이 1일때 컷
    df=df.iloc[:batch[-1]+1,:]
    #7/12 -----------------------------------
    batch=df.index[df.arrived==1]
    temp=0
    for x in batch: # 4 12 27 ...
        for y in range(temp,x): #0-3
            df['arrived'][y]=(df['시간'][x]-df['시간'][y]).seconds
            temp=x+1
    for e in batch:
        df['arrived'][e]=0
    # 7/12 -----------------------------------

    df = df.set_index('시간')
    df.to_csv(f'./사색역데이터/{FileName}')
    return df
  
  
past=4
for x in range(200): # 10분간
    soup=repet(p1112)
    try:
        result=int(soup.resultCode.text)
        arrived=0
        if past!=result:
            if result==0:
                arrived=1
        bus_time.append([soup.queryTime.text,current_buses(),arrived])
        past=result
        print(x,"번째 시도: ",bus_time)
        time.sleep(60)
    except Exception as e:
        continue
df=pd.DataFrame(bus_time,columns=['시간','운행중인 다른 버스들의 위치','arrived'])
#df.to_csv('5100_total.csv',index=False)
mod_df=trim_data(df,'1200_1.csv')
mod_df
