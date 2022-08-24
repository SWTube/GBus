from flask import Flask, render_template, Blueprint
from getInput import *
from timeconvert import *
import pickle
import time
app = Flask(__name__)

bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/')
def index():
    info_message = "정류장을 클릭하여 버스 도착 정보를 확인하세요."
    return render_template("buspage/bus_main.html", info_message=info_message,nowtime=time.strftime("%H시%M분",time.localtime(time.time())))



@bp.route('/busstop/sa/')
def sa():
    model = pickle.load(open('7000_regressor.pkl', 'rb'))
    # 인풋값 생성
    pBus=Bus(p7000)
    try:
        soup=pBus.repet()
        pBus.bus_time.append([soup.queryTime.text,pBus.current_buses()])
        data=pd.DataFrame(pBus.bus_time,columns=['시간','운행중인 다른 버스들의 위치'])
        inputVal=trim_data(data,7000)
        result7 = model.predict(inputVal)
    except requests.Timeout as err:
        result7=False
    except Exception as e:
        result7=False
    
    model = pickle.load(open('5100_regressor.pkl', 'rb'))
    # 인풋값 생성
    pBus=Bus(p5100)
    try:
        soup=pBus.repet()
        pBus.bus_time.append([soup.queryTime.text,pBus.current_buses()])
        data=pd.DataFrame(pBus.bus_time,columns=['시간','운행중인 다른 버스들의 위치'])
        inputVal=trim_data(data,5100)
        result5 = model.predict(inputVal)
    except requests.Timeout as err:
        result5=False
    except Exception as e:
        result5=False
    
    
    model = pickle.load(open('9_regressor.pkl', 'rb'))
    # 인풋값 생성
    pBus=Bus(p0009)
    try:
        soup=pBus.repet()
        pBus.bus_time.append([soup.queryTime.text,pBus.current_buses()])
        data=pd.DataFrame(pBus.bus_time,columns=['시간','운행중인 다른 버스들의 위치'])
        inputVal=trim_data(data,9)
        result0 = model.predict(inputVal)
    except requests.Timeout as err:
        result0=False
    except Exception as e:
        result0=False

    
    model = pickle.load(open('1112_regressor.pkl', 'rb'))
    # 인풋값 생성
    pBus=Bus(p1112)
    try:
        soup=pBus.repet()
        pBus.bus_time.append([soup.queryTime.text,pBus.current_buses()])
        data=pd.DataFrame(pBus.bus_time,columns=['시간','운행중인 다른 버스들의 위치'])
        inputVal=trim_data(data,1112)
        result1 = model.predict(inputVal)
    except requests.Timeout as err:
        result1=False
    except Exception as e:
        result1=False
    
    
    model = pickle.load(open('7000_regressor.pkl', 'rb'))
    # 인풋값 생성
    pBus=Bus(p7000)
    try:
        soup=pBus.repet()
        pBus.bus_time.append([soup.queryTime.text,pBus.current_buses()])
        data=pd.DataFrame(pBus.bus_time,columns=['시간','운행중인 다른 버스들의 위치'])
        inputVal=trim_data(data,7000)
        result7 = model.predict(inputVal)
    except requests.Timeout as err:
        result7=False
    except Exception as e:
        result7=False
    if(result7==False or result0==False or result5==False or result1==False):
        return render_template('buspage/bus_info/bus_error.html',info_message='다시 정류장을 클릭하세요',nowtime=time.strftime("%H시%M분",time.localtime(time.time())),
        infoTime7="에러 발생",
        infoTime5="에러 발생",
        infoTime1="에러 발생",
        infoTime0="에러 발생")
    else:
        return render_template('buspage/bus_info/bus_info.html', info_message='사색의 광장 정류장 도착시간 입니다.',nowtime=time.strftime("%H시%M분",time.localtime(time.time())),
        infoTime7=convertToStringTime(convertedHour(result7,time.time()),convertedMinute(result7,time.time())),
        infoTime5=convertToStringTime(convertedHour(result5,time.time()),convertedMinute(result5,time.time())),
        infoTime1=convertToStringTime(convertedHour(result1,time.time()),convertedMinute(result1,time.time())),
        infoTime0=convertToStringTime(convertedHour(result0,time.time()),convertedMinute(result0,time.time()))
        )



@bp.route('/busstop/pe/')
def pe():
    model = pickle.load(open('7000_regressor.pkl', 'rb'))
    # 인풋값 생성
    pBus=Bus(p7000)
    try:
        soup=pBus.repet()
        pBus.bus_time.append([soup.queryTime.text,pBus.current_buses()])
        data=pd.DataFrame(pBus.bus_time,columns=['시간','운행중인 다른 버스들의 위치'])
        inputVal=trim_data(data,7000)
        result7 = model.predict(inputVal)
    except requests.Timeout as err:
        result7=False
    except Exception as e:
        result7=False
    
    model = pickle.load(open('5100_regressor.pkl', 'rb'))
    # 인풋값 생성
    pBus=Bus(p5100)
    try:
        soup=pBus.repet()
        pBus.bus_time.append([soup.queryTime.text,pBus.current_buses()])
        data=pd.DataFrame(pBus.bus_time,columns=['시간','운행중인 다른 버스들의 위치'])
        inputVal=trim_data(data,5100)
        result5 = model.predict(inputVal)
    except requests.Timeout as err:
        result5=False
    except Exception as e:
        result5=False
    
    
    model = pickle.load(open('9_regressor.pkl', 'rb'))
    # 인풋값 생성
    pBus=Bus(p0009)
    try:
        soup=pBus.repet()
        pBus.bus_time.append([soup.queryTime.text,pBus.current_buses()])
        data=pd.DataFrame(pBus.bus_time,columns=['시간','운행중인 다른 버스들의 위치'])
        inputVal=trim_data(data,9)
        result0 = model.predict(inputVal)
    except requests.Timeout as err:
        result0=False
    except Exception as e:
        result0=False

    
    model = pickle.load(open('1112_regressor.pkl', 'rb'))
    # 인풋값 생성
    pBus=Bus(p1112)
    try:
        soup=pBus.repet()
        pBus.bus_time.append([soup.queryTime.text,pBus.current_buses()])
        data=pd.DataFrame(pBus.bus_time,columns=['시간','운행중인 다른 버스들의 위치'])
        inputVal=trim_data(data,1112)
        result1 = model.predict(inputVal)
    except requests.Timeout as err:
        result1=False
    except Exception as e:
        result1=False
    
    
    model = pickle.load(open('7000_regressor.pkl', 'rb'))
    # 인풋값 생성
    pBus=Bus(p7000)
    try:
        soup=pBus.repet()
        pBus.bus_time.append([soup.queryTime.text,pBus.current_buses()])
        data=pd.DataFrame(pBus.bus_time,columns=['시간','운행중인 다른 버스들의 위치'])
        inputVal=trim_data(data,7000)
        result7 = model.predict(inputVal)
        
    except requests.Timeout as err:
        result7=False
    except Exception as e:
        result7=False
    if(result7==False or result0==False or result5==False or result1==False):
        return render_template('buspage/bus_info/bus_error.html',info_message='다시 정류장을 클릭하세요',nowtime=time.strftime("%H시%M분",time.localtime(time.time())),
        infoTime7="에러 발생",
        infoTime5="에러 발생",
        infoTime1="에러 발생",
        infoTime0="에러 발생")
    else:
        return render_template('buspage/bus_info/bus_info.html', info_message='체육대학외대 정류장 도착시간 입니다.',nowtime=time.strftime("%H시%M분",time.localtime(time.time())),
        infoTime7=convertToStringTime(convertedHour2(result7,time.time()),convertedMinute2(result7,time.time())),
        infoTime5=convertToStringTime(convertedHour2(result5,time.time()),convertedMinute2(result5,time.time())),
        infoTime1=convertToStringTime(convertedHour2(result1,time.time()),convertedMinute2(result1,time.time())),
        infoTime0=convertToStringTime(convertedHour2(result0,time.time()),convertedMinute2(result0,time.time()))
        )

@bp.route('/busstop/bio/')
def bio():
    model = pickle.load(open('7000_regressor.pkl', 'rb'))
    # 인풋값 생성
    pBus=Bus(p7000)
    try:
        soup=pBus.repet()
        pBus.bus_time.append([soup.queryTime.text,pBus.current_buses()])
        data=pd.DataFrame(pBus.bus_time,columns=['시간','운행중인 다른 버스들의 위치'])
        inputVal=trim_data(data,7000)
        result7 = model.predict(inputVal)
    except requests.Timeout as err:
        result7=False
    except Exception as e:
        result7=False
    
    model = pickle.load(open('5100_regressor.pkl', 'rb'))
    # 인풋값 생성
    pBus=Bus(p5100)
    try:
        soup=pBus.repet()
        pBus.bus_time.append([soup.queryTime.text,pBus.current_buses()])
        data=pd.DataFrame(pBus.bus_time,columns=['시간','운행중인 다른 버스들의 위치'])
        inputVal=trim_data(data,5100)
        result5 = model.predict(inputVal)
    except requests.Timeout as err:
        result5=False
    except Exception as e:
        result5=False
    
    
    model = pickle.load(open('9_regressor.pkl', 'rb'))
    # 인풋값 생성
    pBus=Bus(p0009)
    try:
        soup=pBus.repet()
        pBus.bus_time.append([soup.queryTime.text,pBus.current_buses()])
        data=pd.DataFrame(pBus.bus_time,columns=['시간','운행중인 다른 버스들의 위치'])
        inputVal=trim_data(data,9)
        result0 = model.predict(inputVal)
    except requests.Timeout as err:
        result0=False
    except Exception as e:
        result0=False

    
    model = pickle.load(open('1112_regressor.pkl', 'rb'))
    # 인풋값 생성
    pBus=Bus(p1112)
    try:
        soup=pBus.repet()
        pBus.bus_time.append([soup.queryTime.text,pBus.current_buses()])
        data=pd.DataFrame(pBus.bus_time,columns=['시간','운행중인 다른 버스들의 위치'])
        inputVal=trim_data(data,1112)
        result1 = model.predict(inputVal)
    except requests.Timeout as err:
        result1=False
    except Exception as e:
        result1=False
    
    
    model = pickle.load(open('7000_regressor.pkl', 'rb'))
    # 인풋값 생성
    pBus=Bus(p7000)
    try:
        soup=pBus.repet()
        pBus.bus_time.append([soup.queryTime.text,pBus.current_buses()])
        data=pd.DataFrame(pBus.bus_time,columns=['시간','운행중인 다른 버스들의 위치'])
        inputVal=trim_data(data,7000)
        result7 = model.predict(inputVal)
    except requests.Timeout as err:
        result7=False
    except Exception as e:
        result7=False
    if(result7==False or result0==False or result5==False or result1==False):
        return render_template('buspage/bus_info/bus_error.html',info_message='다시 정류장을 클릭하세요',nowtime=time.strftime("%H시%M분",time.localtime(time.time())),
        infoTime7="에러 발생",
        infoTime5="에러 발생",
        infoTime1="에러 발생",
        infoTime0="에러 발생")
    else:
        return render_template('buspage/bus_info/bus_info.html', info_message='생명과학대학 정류장 도착시간 입니다.',nowtime=time.strftime("%H시%M분",time.localtime(time.time())),
        infoTime7=convertToStringTime(convertedHour1(result7,time.time()),convertedMinute1(result7,time.time())),
        infoTime5=convertToStringTime(convertedHour1(result5,time.time()),convertedMinute1(result5,time.time())),
        infoTime1=convertToStringTime(convertedHour1(result1,time.time()),convertedMinute1(result1,time.time())),
        infoTime0=convertToStringTime(convertedHour1(result0,time.time()),convertedMinute1(result0,time.time()))

        )








