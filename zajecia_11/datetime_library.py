import datetime

subscription_time = 30

print(datetime.datetime.now().year)
print(type(datetime.datetime.now()))
print(datetime.datetime.now())
data_format = "%Y/%d/%m %H:%M:%S"
print(data_format)
#my_format = datetime.datetime.strftime(data_format)
#print(my_format)
print(datetime.datetime.now().strftime(data_format))

time = "2024/10/06 18:00:00"
print(type(time))
date_from_time = datetime.datetime.strptime(time, data_format)
print(date_from_time)
print(type(date_from_time))

if datetime.datetime.now() < date_from_time + datetime.timedelta(days=subscription_time):
    print(f"Mozesz uzywac netflixa. Twoja subskrypcja wygasa: {date_from_time + datetime.timedelta(days=subscription_time)}")
else:
    print(f"Musisz odnowić subskrypcję! Twoja subskrypcja wygasła: {date_from_time + datetime.timedelta(days=subscription_time)}")
    print("Nie mozesz uzywac netflixa")