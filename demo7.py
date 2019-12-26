import time;
import calendar;

ticks = time.time()
print (ticks)

localtime = time.localtime(time.time())
print localtime

localtimes = time.asctime(time.localtime(time.time()))
print localtimes


print time.strftime('%Y-%m-%d',time.localtime())
print time.strftime('%Y-%m',time.localtime())

print time.strftime('%Y-%m-%d %H:%M',time.localtime())


cal = calendar.month(2020,1)
print cal