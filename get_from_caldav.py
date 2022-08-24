import caldav
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

url = os.getenv('url')
username = os.getenv('username')
password = os.getenv('password')

client = caldav.DAVClient(url=url, username=username, password=password)
principal = client.principal()
calendars = principal.calendars()
    
today = datetime.datetime.now()
schedules = []
for calendar in calendars:
        try:
            events = calendar.date_search(start=today, end=today+datetime.timedelta(days=1), expand=True)
            for event in events:
                d = {}
                for event_data in event.data.splitlines():
                    pair = event_data.split(":")
                    d[pair[0]] = pair[1]
                schedules.append(d)
        except:
            continue

d = {}
for schedule in schedules:
    if 'SUMMARY' in schedule.keys():
        key = schedule['SUMMARY']
    if 'DTSTART' in schedule.keys():
        value1 = schedule['DTSTART'][:8]
    elif 'DTSTART;VALUE=DATE' in schedule.keys():
        value1 = schedule['DTSTART;VALUE=DATE'][:8]
    
    if 'DTEND' in schedule.keys():
        value2 = schedule['DTSTART'][:8]
    elif 'DTEND;VALUE=DATE' in schedule.keys():
        value2 = schedule['DTEND;VALUE=DATE'][:8]
    d[key] = (value1,value2)
print(d)