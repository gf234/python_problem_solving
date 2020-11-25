import datetime

t = datetime.time(9, 30, 45, 100000)
print(t)  # 09:30:45.100000
print(t.hour)  # 9

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt)  # 2016-07-26 12:30:45.100000
print(dt.time())  # 12:30:45.100000
print(dt.year)  # 2016

tdelta = datetime.timedelta(days=7)

print(dt+tdelta)  # 7일 더하기

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)
# 2020-11-16 23:24:18.263634
# 2020-11-16 23: 24: 18.263633
# 2020-11-16 14: 24: 18.263633
