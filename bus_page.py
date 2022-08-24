from flask import Flask, render_template
from getInput import *
from timeconvert import *
import pickle
from pytz import timezone
app = Flask(__name__)


utc_now = datetime.datetime.utcnow()
kr_time = datetime.datetime.now(timezone('Asia/Seoul'))

nowtime = convertToStringTime(kr_time.hour, kr_time.minute)

def krtimeToMin():
    minute = (int(kr_time.hour) * 60) + int(kr_time.minute)
    return minute

@app.route('/')
def index():
    info_message = "정류장을 클릭하여 버스 도착 정보를 확인하세요."
    return render_template("buspage/bus_main.html", info_message=info_message, now_time=nowtime)

@app.route('/busstop/<id>/')
def bus_stop(id):
    info_message = f"{id} 정류장 버스 도착 정보입니다."
    return render_template("bus_info.html", info_message=info_message, now_time=nowtime)


@app.route('/busstop/사색의광장/')
def indexa():
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
    now_min = krtimeToMin()

    if(result7==False or result0==False or result5==False or result1==False):
        return render_template('buspage/bus_info/bus_except.html',info_message='다시 정류장을 클릭하세요',nowtime = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7="에러 발생",
        infoTime5="에러 발생",
        infoTime1="에러 발생",
        infoTime0="에러 발생")
    else:
        if (10 < now_min < 330):
            infoTime5 = "버스 없음"
        else:
            infoTime5 = convertToStringTime(convertedHour(result5,utc_now),convertedMinute(result5,utc_now)) + "<br>도착예정"
        if (279 < now_min < 1351):
            infoTime1 = convertToStringTime(convertedHour(result7,utc_now),convertedMinute(result7,utc_now)) + "<br>도착예정"
        else:
            infoTime1 = "버스 없음"
        if (0 < now_min < 330):
            infoTime7 = "버스 없음"
        else:
            infoTime7 = convertToStringTime(convertedHour(result7,utc_now),convertedMinute(result7,utc_now)) + "<br>도착예정"
        if (329 < now_min < 1381):
            infoTime0 = convertToStringTime(convertedHour(result0,utc_now),convertedMinute(result0,utc_now)) + "<br>도착예정"
        else:
            infoTime0 = "버스 없음"
        return render_template('buspage/bus_info/bus_info.html', info_message='사색의 광장 정류장 도착시간 입니다.',nowtime = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7=infoTime7,
        infoTime5=infoTime5,
        infoTime1=infoTime1,
        infoTime0=infoTime0
        )



@app.route('/busstop/체육대학외대/')
def indexaa():
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
    now_min = krtimeToMin()

    if(result7==False or result0==False or result5==False or result1==False):
        return render_template('buspage/bus_info/bus_except.html',info_message='다시 정류장을 클릭하세요',nowtime = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7="에러 발생",
        infoTime5="에러 발생",
        infoTime1="에러 발생",
        infoTime0="에러 발생")
    else:
        if (10 < now_min < 330):
            infoTime5 = "버스 없음"
        else:
            infoTime5 = convertToStringTime(convertedHour(result5,utc_now),convertedMinute(result5,utc_now)) + "<br>도착예정"
        if (279 < now_min < 1351):
            infoTime1 = convertToStringTime(convertedHour(result7,utc_now),convertedMinute(result7,utc_now)) + "<br>도착예정"
        else:
            infoTime1 = "버스 없음"
        if (0 < now_min < 330):
            infoTime7 = "버스 없음"
        else:
            infoTime7 = convertToStringTime(convertedHour(result7,utc_now),convertedMinute(result7,utc_now)) + "<br>도착예정"
        if (329 < now_min < 1381):
            infoTime0 = convertToStringTime(convertedHour(result0,utc_now),convertedMinute(result0,utc_now)) + "<br>도착예정"
        else:
            infoTime0 = "버스 없음"
        return render_template('buspage/bus_info/bus_info.html', info_message='체육대학외대 정류장 도착시간 입니다.',nowtime = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7=infoTime7,
        infoTime5=infoTime5,
        infoTime1=infoTime1,
        infoTime0=infoTime0
        )


@app.route('/busstop/생명과학대/')
def indexaaa():
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
    now_min = krtimeToMin()

    if(result7==False or result0==False or result5==False or result1==False):
        return render_template('buspage/bus_info/bus_except.html',info_message='다시 정류장을 클릭하세요',nowtime = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7="에러 발생",
        infoTime5="에러 발생",
        infoTime1="에러 발생",
        infoTime0="에러 발생")
    else:
        if (10 < now_min < 330):
            infoTime5 = "버스 없음"
        else:
            infoTime5 = convertToStringTime(convertedHour(result5,utc_now),convertedMinute(result5,utc_now)) + "<br>도착예정"
        if (279 < now_min < 1351):
            infoTime1 = convertToStringTime(convertedHour(result7,utc_now),convertedMinute(result7,utc_now)) + "<br>도착예정"
        else:
            infoTime1 = "버스 없음"
        if (0 < now_min < 330):
            infoTime7 = "버스 없음"
        else:
            infoTime7 = convertToStringTime(convertedHour(result7,utc_now),convertedMinute(result7,utc_now)) + "<br>도착예정"
        if (329 < now_min < 1381):
            infoTime0 = convertToStringTime(convertedHour(result0,utc_now),convertedMinute(result0,utc_now)) + "<br>도착예정"
        else:
            infoTime0 = "버스 없음"
        return render_template('buspage/bus_info/bus_info.html', info_message='생명과학대학 정류장 도착시간 입니다.',nowtime = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7=infoTime7,
        infoTime5=infoTime5,
        infoTime1=infoTime1,
        infoTime0=infoTime0
        )

if __name__ == '__main__':
    app.run(debug=True)