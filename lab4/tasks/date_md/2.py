#write a python program to print yesterday, today, tomorrow
import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print("Today: ", today)
print("Yesterday: ", yesterday)
print("Tomorrow: ", tomorrow)