import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import warnings
import time
import sklearn.preprocessing

warnings.filterwarnings(action='ignore')

serviceKey='Jw+++HTzL3V8lfZPcQPb5jB5Rae2NH3BYowjBY+cgMIA1yDcwJNfmtfO+E+O+whPsGCGbJmmpf/X904L4uwGIw=='
p5100 ={'serviceKey' :serviceKey,
             'routeId':'200000115','stationId':'228000703'}
p1112 ={'serviceKey' : serviceKey,
         'routeId':'234000016','stationId':'228000703'}
p0009 ={'serviceKey' :serviceKey,
             'routeId':'200000103','stationId':'228000703'}
p7000 ={'serviceKey' :serviceKey,
             'routeId':'200000112','stationId':'228000703'}
class Bus():
    def __init__(self,params):
        self.params=params
        self.bus_time=[]
        
    def repet(self):
        url = 'http://apis.data.go.kr/6410000/busarrivalservice/getBusArrivalItem'
        response = requests.get(url, params=self.params)
        soup=BeautifulSoup(response.text,'xml')
        return soup

        
    def current_buses(self):  
        url = 'http://apis.data.go.kr/6410000/buslocationservice/getBusLocationList'
        mod_params ={'serviceKey' : self.params['serviceKey'],
                  'routeId':self.params['routeId']}

        response=requests.get(url,params=mod_params)
        soup=BeautifulSoup(response.text,'xml')
        locations=sorted([int(x.stationSeq.text) for x in soup.find_all('busLocationList')])
        return locations

def trim_data(data,busNum):

    df=data.copy() # localbounderror 해결
    
    df['시간'] = df['시간'].apply(pd.to_datetime) 
    df['hour']=df['시간'].dt.hour
    df['minute']=df['시간'].dt.minute
    df['day'] = df['시간'].dt.weekday 

    mb = sklearn.preprocessing.MultiLabelBinarizer()
    if isinstance(df['운행중인 다른 버스들의 위치'].iloc[0], str):
        df['운행중인 다른 버스들의 위치'] = df['운행중인 다른 버스들의 위치'].apply(eval)
    
    if busNum==1112:
        lst=list(range(2,69))
    elif busNum==5100:
        lst=list(range(1,55))
    elif busNum==9:
        lst=list(range(1,87))
    elif busNum==7000:
        lst=list(range(1,80))
        
    mb.fit([lst])
    entity=mb.transform(df['운행중인 다른 버스들의 위치'])
    lsts=pd.DataFrame(entity,columns=mb.classes_)
    lsts.columns=[f'station{x}' for x in lsts.columns]
    df=pd.concat([df,lsts],axis=1,sort=False).reset_index(drop=True)


    df=df.drop(["운행중인 다른 버스들의 위치"],axis=1)
    df = df.set_index('시간')

    
    return df
