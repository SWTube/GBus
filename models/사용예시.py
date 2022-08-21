from getInput import *
import pickle

# (예시)1112번 버스 도착 시간을 예측할때

#모델 로드
model = pickle.load(open('1112_regressor.pkl', 'rb'))
# 인풋값 생성
pBus=Bus(p1112)
try:
    soup=pBus.repet()
    pBus.bus_time.append([soup.queryTime.text,pBus.current_buses()])
    data=pd.DataFrame(pBus.bus_time,columns=['시간','운행중인 다른 버스들의 위치'])
    inputVal=trim_data(data,1112)
    result = model.predict(inputVal)
except requests.Timeout as err:
    result='error'
except Exception as e:
    result='error'

print(result)
# 예측값은 float
# line 7,9,14는 버스 번호에 맞게 바뀌어야됨
# 사용자가 버스 버튼을 누를때마다 위 과정을 시행하지 말고
# (여러 사용자가 동시에 요청하게 되면 api호출시 에러 날수 있으므로)
# 1분마다 서버가 위 과정을 반복해서 화면에 업데이트되게 해주세요.