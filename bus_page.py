from flask import Flask, render_template
from getInput import *
from timeconvert import *
import pickle
from pytz import timezone
app = Flask(__name__)



def krtimeToMin():
    kr_time = datetime.datetime.now(timezone('Asia/Seoul'))
    minute = (int(kr_time.hour) * 60) + int(kr_time.minute)
    return minute

@app.route('/')
def index():
    kr_time = datetime.datetime.now(timezone('Asia/Seoul'))
    info_message = "정류장을 클릭하여 버스 도착 정보를 확인하세요."
    return render_template("buspage/bus_main.html", info_message=info_message, now_time=convertToStringTime(kr_time.hour, kr_time.minute))

@app.route('/busstop/<id>/')
def bus_stop(id):
    kr_time = datetime.datetime.now(timezone('Asia/Seoul'))
    info_message = f"{id} 정류장 버스 도착 정보입니다."
    return render_template("bus_info.html", info_message=info_message, now_time=convertToStringTime(kr_time.hour, kr_time.minute))


@app.route('/busstop/사색의광장/')
def indexa():
    kr_time = datetime.datetime.now(timezone('Asia/Seoul'))
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

    now_min = krtimeToMin()

    if(result7==False or result0==False or result5==False or result1==False):
        return render_template('buspage/bus_info/bus_except.html',info_message='다시 정류장을 클릭하세요',now_time =convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7="에러 발생",
        infoTime5="에러 발생",
        infoTime1="에러 발생",
        infoTime0="에러 발생")
    else:
        if (0 <= now_min < 11):
            return render_template('buspage/bus_info/bus_info5.html', info_message='사색의 광장 정류장 도착시간 입니다.',now_time =convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7="버스없음",
        infoTime5=convertToStringTime(convertedHour(result5,kr_time),convertedMinute(result5,kr_time)),
        infoTime1="버스없음",
        infoTime0="버스없음"
        )
        elif (10 < now_min < 280):
            return render_template('buspage/bus_info/bus_except.html', info_message='사색의 광장 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7="버스없음",
        infoTime5="버스없음",
        infoTime1="버스없음",
        infoTime0="버스없음"
        )
        elif (279 < now_min < 329):
            return render_template('buspage/bus_info/bus_info1.html', info_message='사색의 광장 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7="버스없음",
        infoTime5="버스없음",
        infoTime1=convertToStringTime(convertedHour(result1, kr_time),convertedMinute(result1,kr_time)),
        infoTime0="버스없음"
        )
        elif (329 < now_min < 1351):
            return render_template('buspage/bus_info/bus_info1579.html', info_message='사색의 광장 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7=convertToStringTime(convertedHour(result7,kr_time),convertedMinute(result7,kr_time)),
        infoTime5=convertToStringTime(convertedHour(result5,kr_time),convertedMinute(result5,kr_time)),
        infoTime1=convertToStringTime(convertedHour(result1,kr_time),convertedMinute(result1,kr_time)),
        infoTime0=convertToStringTime(convertedHour(result0,kr_time),convertedMinute(result0,kr_time))
        )
        elif (1350 < now_min < 1381):
            return render_template('buspage/bus_info/bus_info579.html', info_message='사색의 광장 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7=convertToStringTime(convertedHour(result7,kr_time),convertedMinute(result7,kr_time)),
        infoTime5=convertToStringTime(convertedHour(result5,kr_time),convertedMinute(result5,kr_time)),
        infoTime1="버스없음",
        infoTime0=convertToStringTime(convertedHour(result0,kr_time),convertedMinute(result0,kr_time))
        )
        elif (1380 < now_min < 1440):
            return render_template('buspage/bus_info/bus_info79.html', info_message='사색의 광장 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7=convertToStringTime(convertedHour(result7,kr_time),convertedMinute(result7,kr_time)),
        infoTime5=convertToStringTime(convertedHour(result5,kr_time),convertedMinute(result5,kr_time)),
        infoTime1="버스없음",
        infoTime0="버스없음"
        )
        else:
            return render_template('buspage/bus_info/bus_except.html', info_message='사색의 광장 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
            infoTime7="버스없음",
            infoTime5="버스없음",
            infoTime1="버스없음",
            infoTime0="버스없음"
            )



@app.route('/busstop/체육대학외대/')
def indexaa():
    kr_time = datetime.datetime.utcnow()
    kr_time = datetime.datetime.now(timezone('Asia/Seoul'))
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

    now_min = krtimeToMin()

    if(result7==False or result0==False or result5==False or result1==False):
        return render_template('buspage/bus_info/bus_except.html',info_message='다시 정류장을 클릭하세요',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7="에러 발생",
        infoTime5="에러 발생",
        infoTime1="에러 발생",
        infoTime0="에러 발생")
    else:
        if (0 <= now_min < 11):
            return render_template('buspage/bus_info/bus_info5.html', info_message='체육대학.외대 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7="버스없음",
        infoTime5=convertToStringTime(convertedHour2(result5,kr_time),convertedMinute2(result5,kr_time)),
        infoTime1="버스없음",
        infoTime0="버스없음"
        )
        elif (10 < now_min < 280):
            return render_template('buspage/bus_info/bus_except.html', info_message='체육대학.외대 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7="버스없음",
        infoTime5="버스없음",
        infoTime1="버스없음",
        infoTime0="버스없음"
        )
        elif (279 < now_min < 329):
            return render_template('buspage/bus_info/bus_info1.html', info_message='체육대학.외대 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7="버스없음",
        infoTime5="버스없음",
        infoTime1=convertToStringTime(convertedHour2(result1,kr_time),convertedMinute2(result1,kr_time)),
        infoTime0="버스없음"
        )
        elif (329 < now_min < 1351):
            return render_template('buspage/bus_info/bus_info1579.html', info_message='체육대학.외대 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7=convertToStringTime(convertedHour2(result7,kr_time),convertedMinute2(result7,kr_time)),
        infoTime5=convertToStringTime(convertedHour2(result5,kr_time),convertedMinute2(result5,kr_time)),
        infoTime1=convertToStringTime(convertedHour2(result1,kr_time),convertedMinute2(result1,kr_time)),
        infoTime0=convertToStringTime(convertedHour2(result0,kr_time),convertedMinute2(result0,kr_time))
        )
        elif (1350 < now_min < 1381):
            return render_template('buspage/bus_info/bus_info579.html', info_message='체육대학.외대 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7=convertToStringTime(convertedHour2(result7,kr_time),convertedMinute2(result7,kr_time)),
        infoTime5=convertToStringTime(convertedHour2(result5,kr_time),convertedMinute2(result5,kr_time)),
        infoTime1="버스없음",
        infoTime0=convertToStringTime(convertedHour2(result0,kr_time),convertedMinute2(result0,kr_time))
        )
        elif (1380 < now_min < 1440):
            return render_template('buspage/bus_info/bus_info79.html', info_message='체육대학.외대 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7=convertToStringTime(convertedHour2(result7,kr_time),convertedMinute2(result7,kr_time)),
        infoTime5=convertToStringTime(convertedHour2(result5,kr_time),convertedMinute2(result5,kr_time)),
        infoTime1="버스없음",
        infoTime0="버스없음"
        )
        else:
            return render_template('buspage/bus_info/bus_except.html', info_message='체육대학.외대 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
            infoTime7="버스없음",
            infoTime5="버스없음",
            infoTime1="버스없음",
            infoTime0="버스없음"
            )


@app.route('/busstop/생명과학대/')
def indexaaa():
    kr_time = datetime.datetime.utcnow()
    kr_time = datetime.datetime.now(timezone('Asia/Seoul'))
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

    now_min = krtimeToMin()

    if(result7==False or result0==False or result5==False or result1==False):
        return render_template('buspage/bus_info/bus_except.html',info_message='다시 정류장을 클릭하세요',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7="에러 발생",
        infoTime5="에러 발생",
        infoTime1="에러 발생",
        infoTime0="에러 발생")
    else:
        if (0 <= now_min < 11):
            return render_template('buspage/bus_info/bus_info5.html', info_message='생명과학대 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7="버스없음",
        infoTime5=convertToStringTime(convertedHour1(result5,kr_time),convertedMinute1(result5,kr_time)),
        infoTime1="버스없음",
        infoTime0="버스없음"
        )
        elif (10 < now_min < 280):
            return render_template('buspage/bus_info/bus_except.html', info_message='생명과학대 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7="버스없음",
        infoTime5="버스없음",
        infoTime1="버스없음",
        infoTime0="버스없음"
        )
        elif (279 < now_min < 329):
            return render_template('buspage/bus_info/bus_info1.html', info_message='생명과학외대 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7="버스없음",
        infoTime5="버스없음",
        infoTime1=convertToStringTime(convertedHour1(result1,kr_time),convertedMinute1(result1,kr_time)),
        infoTime0="버스없음"
        )
        elif (329 < now_min < 1351):
            return render_template('buspage/bus_info/bus_info1579.html', info_message='생명과학대 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7=convertToStringTime(convertedHour1(result7,kr_time),convertedMinute1(result7,kr_time)),
        infoTime5=convertToStringTime(convertedHour1(result5,kr_time),convertedMinute1(result5,kr_time)),
        infoTime1=convertToStringTime(convertedHour1(result1,kr_time),convertedMinute1(result1,kr_time)),
        infoTime0=convertToStringTime(convertedHour1(result0,kr_time),convertedMinute1(result0,kr_time))
        )
        elif (1350 < now_min < 1381):
            return render_template('buspage/bus_info/bus_info579.html', info_message='생명과학대 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7=convertToStringTime(convertedHour1(result7,kr_time),convertedMinute1(result7,kr_time)),
        infoTime5=convertToStringTime(convertedHour1(result5,kr_time),convertedMinute1(result5,kr_time)),
        infoTime1="버스없음",
        infoTime0=convertToStringTime(convertedHour1(result0,kr_time),convertedMinute1(result0,kr_time))
        )
        elif (1380 < now_min < 1440):
            return render_template('buspage/bus_info/bus_info79.html', info_message='생명과학대 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
        infoTime7=convertToStringTime(convertedHour1(result7,kr_time),convertedMinute1(result7,kr_time)),
        infoTime5=convertToStringTime(convertedHour1(result5,kr_time),convertedMinute1(result5,kr_time)),
        infoTime1="버스없음",
        infoTime0="버스없음"
        )
        else:
            return render_template('buspage/bus_info/bus_except.html', info_message='체육대학.외대 정류장 도착시간 입니다.',now_time = convertToStringTime(kr_time.hour, kr_time.minute),
            infoTime7="버스없음",
            infoTime5="버스없음",
            infoTime1="버스없음",
            infoTime0="버스없음"
            )

if __name__ == '__main__':
    app.run(debug=True)