import datetime
data=datetime.datetime.now()
print(data)

print("Year:", data.year)
print("Month:",data.month)
print("Day:",data.day)
print("Hour:",data.hour)
print("Minute:",data.minute)
print("Second:",data.second)

formated=data.strftime("%d-%m-%Y")
print(formated)

date_string="25-12-2026"
date=datetime.datetime.strptime(date_string,"%d-%m-%Y")
print(date)


future_date=data+datetime.timedelta(days=10)
print("Today:",data)
print(future_date)

start_time="2026-08-01"
star=datetime.datetime.strptime(start_time,"%Y-%m-%d")
print("Start Time:",start_time)
end_time="2026-08-18"
end_=datetime.datetime.strptime(end_time,"%Y-%m-%d")
print("End Time:",end_time)
spend_time=end_-star
print(spend_time)

start=datetime.datetime.now()
print(start)
end="10-08-2026"
en=datetime.datetime.strptime(end,"%d-%m-%Y")
middle_time=start-en
print(middle_time)

