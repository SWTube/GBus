from flask import Flask, render_template, url_for
from getInput import *
from timeconvert import *
import pickle
app = Flask(__name__)

@app.route('/')
def index():
    info_message = "정류장을 클릭하여 버스 도착 정보를 확인하세요."
    return render_template("buspage/bus_main.html", info_message=info_message)

@app.route('/busstop/<id>/')
def bus_stop(id):
    info_message = f"{id} 정류장 버스 도착 정보입니다."
    return render_template("bus_info.html", info_message=info_message)


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
        result7='errorRequestsTimeout'
    except Exception as e:
        result7='errorException'
    
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
        result5='errorRequestsTimeout'
    except Exception as e:
        result5='errorException'
    
    
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
        result0='errorRequestsTimeout'
    except Exception as e:
        result0='errorException'

    
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
        result1='errorRequestsTimeout'
    except Exception as e:
        result1='errorException'
    
    
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
        result7='errorRequestsTimeout'
    except Exception as e:
        result7='errorException'
    return render_template('buspage/bus_info/bus_infosa.html', info_message='사색의 광장 정류장 도착시간 입니다.',
    infoTime7=convertToStringTime(convertedHour(result7),convertedMinute(result7)),
    infoTime5=convertToStringTime(convertedHour(result5),convertedMinute(result5)),
    infoTime1=convertToStringTime(convertedHour(result1),convertedMinute(result1)),
    infoTime0=convertToStringTime(convertedHour(result0),convertedMinute(result0))
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
        result7='errorRequestsTimeout'
    except Exception as e:
        result7='errorException'
    
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
        result5='errorRequestsTimeout'
    except Exception as e:
        result5='errorException'
    
    
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
        result0='errorRequestsTimeout'
    except Exception as e:
        result0='errorException'

    
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
        result1='errorRequestsTimeout'
    except Exception as e:
        result1='errorException'
    
    
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
        result7='errorRequestsTimeout'
    except Exception as e:
        result7='errorException'
    return render_template('buspage/bus_info/bus_infope.html', info_message='체육대학외대 정류장 도착시간 입니다.',
    infoTime7=convertToStringTime(convertedHour2(result7),convertedMinute2(result7)),
    infoTime5=convertToStringTime(convertedHour2(result5),convertedMinute2(result5)),
    infoTime1=convertToStringTime(convertedHour2(result1),convertedMinute2(result1)),
    infoTime0=convertToStringTime(convertedHour2(result0),convertedMinute2(result0))
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
        result7='errorRequestsTimeout'
    except Exception as e:
        result7='errorException'
    
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
        result5='errorRequestsTimeout'
    except Exception as e:
        result5='errorException'
    
    
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
        result0='errorRequestsTimeout'
    except Exception as e:
        result0='errorException'

    
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
        result1='errorRequestsTimeout'
    except Exception as e:
        result1='errorException'
    
    
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
        result7='errorRequestsTimeout'
    except Exception as e:
        result7='errorException'
    return render_template('buspage/bus_info/bus_infobi.html', info_message='생명과학대 정류장 도착시간 입니다.',
    infoTime7=convertToStringTime(convertedHour1(result7),convertedMinute1(result7)),
    infoTime5=convertToStringTime(convertedHour1(result5),convertedMinute1(result5)),
    infoTime1=convertToStringTime(convertedHour1(result1),convertedMinute1(result1)),
    infoTime0=convertToStringTime(convertedHour1(result0),convertedMinute1(result0))
    )











if __name__ == "__main__":
    app.run(debug=True)