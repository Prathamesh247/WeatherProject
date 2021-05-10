f = open("timezones.txt", "w")
import pytz
for tz in pytz.all_timezones:
  f.write(tz +"\n")
f.close()