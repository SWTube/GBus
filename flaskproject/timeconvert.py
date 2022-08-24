import time



def convertedHour(infoBusNum,currentTime=time.time()): #몇시 도착예정인지
    arriveSec=currentTime+int(infoBusNum)
    arriveHour = time.strftime("%H",time.localtime(arriveSec))
    return arriveHour
    
def convertedMinute(infoBusNum,currentTime=time.time()):#몇분 도착예정인지
    arriveSec = currentTime+int(infoBusNum)
    arriveMin = time.strftime("%M",time.localtime(arriveSec))
    return arriveMin

def convertedHour1(infoBusNum,currentTime=time.time()): #몇시 도착예정인지
    arriveSec=currentTime+int(infoBusNum)+90
    arriveHour = time.strftime("%H",time.localtime(arriveSec))
    return arriveHour
    
def convertedMinute1(infoBusNum,currentTime=time.time()):#몇분 도착예정인지
    arriveSec = currentTime+int(infoBusNum)+90
    arriveMin = time.strftime("%M",time.localtime(arriveSec))
    return arriveMin

def convertedHour2(infoBusNum,currentTime=time.time()): #몇시 도착예정인지
    arriveSec=currentTime+int(infoBusNum)+120
    arriveHour = time.strftime("%H",time.localtime(arriveSec))
    return arriveHour
    
def convertedMinute2(infoBusNum,currentTime=time.time()):#몇분 도착예정인지
    arriveSec = currentTime+int(infoBusNum)+120
    arriveMin = time.strftime("%M",time.localtime(arriveSec))
    return arriveMin



def convertToStringTime(hour,min):
    stringTime = "{0}시{1}분".format(int(hour),int(min))
    return stringTime
