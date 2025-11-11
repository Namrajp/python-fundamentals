import datetime

# times
# hour, minute, second
t = datetime.time(1, 25, 10)
t.hour # 1
t.microsecond # 0 

datetime.time.min # 00:00:00

today = datetime.date.today()
today.timetuple() #namedtuple with data about date
today.day