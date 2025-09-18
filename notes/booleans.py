# AC 2nd Booleans Notes

import time
import datetime as date
over = False
print(over)

name = 0.0
print(bool(name))

current_time = time.time()
readable_time = time.ctime(current_time)
print(f"Current Time in seconds since January 1, 1970 (epoch time): {current_time}")
print(f"Current Time: {readable_time}")

now = date.datetime.now()
current_hour = now.strftime("%H")
# Month = %m or ( %b, %B )
# Day = %d
# Year = %Y, %y
# Hour = %H
# Minutes = %M
# Seconds = %S
print(f'Current time according to datetime: {now}')
print(f"Hour: {current_hour}")
print(f"My hour variable is a String: {isinstance(current_hour, str)}")
print(f"My hour variable is a Integer: {isinstance(current_hour, int)}")
print(f"My hour variable is a Float: {isinstance(current_hour, float)}")