import datetime

#creating the function getDate to get the current date
def getDate():
    now = datetime.datetime.now
    return str(now().date())

#creating the function getTime to get the current time
def getTime():
    now = datetime.datetime.now
    return str(now().time())

