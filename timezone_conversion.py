import pytz
from datetime import datetime

def gmt_to_indian(unix_gmt):
    #Set timezone for the city
    indian = pytz.timezone('Asia/Kolkata')

    #Set GMT time for reference
    gmt = pytz.timezone('GMT')

    #Create a datetime object
    date = datetime.utcfromtimestamp(unix_gmt)

    # Associate the date with the GMT timezone.
    date = gmt.localize(date)

    #Convert date to our timezone
    indian_time = date.astimezone(indian)
    return indian_time

if __name__ == '__main__':
    for timezone in pytz.all_timezones:
        print(timezone)