#write a python program to substract five days from current date
import datetime
now = datetime.date.today()
five_days_ago = now - datetime.timedelta(days = 5)
print("Five days ago: ", five_days_ago)