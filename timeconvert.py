import datetime
import pytz

kr = pytz.timezone('Asia/Seoul')


def convertedHour(infoBusNum,currentTime): #몇시 도착예정인지
    arriveSec = currentTime+ datetime.timedelta(seconds=int(infoBusNum))
    hour = arriveSec.hour
    return hour

def convertedMinute(infoBusNum,currentTime):#몇분 도착예정인지
    arriveSec = currentTime+ datetime.timedelta(seconds=int(infoBusNum))
    minute = arriveSec.minute
    return minute

def convertedHour1(infoBusNum,currentTime): #몇시 도착예정인지
    arriveSec = currentTime+ datetime.timedelta(seconds=(int(infoBusNum)+90))
    hour = arriveSec.hour
    return hour

def convertedMinute1(infoBusNum,currentTime):#몇분 도착예정인지
    arriveSec = currentTime+ datetime.timedelta(seconds=(int(infoBusNum)+90))
    minute = arriveSec.minute
    return minute

def convertedHour2(infoBusNum,currentTime): #몇시 도착예정인지
    arriveSec = currentTime+ datetime.timedelta(seconds=(int(infoBusNum)+120))
    hour = arriveSec.hour
    return hour

def convertedMinute2(infoBusNum,currentTime):#몇분 도착예정인지
    arriveSec = currentTime+ datetime.timedelta(seconds=(int(infoBusNum)+120))
    minute = arriveSec.minute
    return minute

def convertToStringTime(hour,min):
    stringTime = "{0}시{1}분".format(int(hour),int(min))
    return stringTime