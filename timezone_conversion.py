import pytz
from datetime import datetime

def gmt_to_indian(unix_gmt):
    indian = pytz.timezone('Asia/Kolkata')
    gmt = pytz.timezone('GMT')
    date = datetime.utcfromtimestamp(unix_gmt)
    date = gmt.localize(date)
    indian_time = date.astimezone(indian)
    return indian_time

if __name__ == '__main__':
    for timezone in pytz.all_timezones:
        print(timezone)