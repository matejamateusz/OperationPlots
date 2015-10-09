__author__ = 'mmateja'
import time
import datetime
xlist={}
ylist=[(2015, 6, 3, 10, 41, 3), (2015, 6, 3, 20, 32, 21)]
xlist['time']=ylist
print xlist
def funkcja(xdict):
    return {"time": map(lambda k: time.mktime(datetime.datetime(*k).timetuple()), xdict["time"])}


d=funkcja(xlist)
print d

# d = datetime(ylist[0][0], ylist[0][1], ylist[0][2], ylist[0][3], ylist[0][4], ylist[0][5])
# timestamp2 = time.mktime(d.timetuple())
# datetime.fromtimestamp(timestamp2)
# print timestamp2