#write a python program to drop microseconds from datetime
import datetime
today = datetime.datetime.now()
print(today.strftime("%d"'.'"%m"'.'"%Y"' ' "%H"'.'"%M"'.'"%S"))