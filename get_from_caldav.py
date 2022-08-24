import caldav
import datetime
import os
from dotenv import load_dotenv

today = datetime.datetime.now()
class CalDAV:
    def __init__(self) -> None:
        load_dotenv()
        self.url = os.getenv('url')
        self.username = os.getenv('username')
        self.password = os.getenv('password')
    def getSchedules(self,start:datetime,days:int):
        with caldav.DAVClient(url=self.url, username=self.username, password=self.password) as client:
            principal = client.principal()
            calendars = principal.calendars()
            end = start + datetime.timedelta(days=days)

            schedules = []
            for calendar in calendars:
                    try:
                        events = calendar.date_search(start=start, end=end, expand=True)
                        for event in events:
                            var = calendar.name
                            d = {}
                            for event_data in event.data.splitlines():
                                pair = event_data.split(":")
                                d[pair[0]] = pair[1]
                            schedules.append((var,d))
                    except:
                        continue
            #print(schedules)
           
            schedulelist = []
            for schedule in schedules:
                var = schedule[0]
                
                if 'SUMMARY' in schedule[1].keys():
                    summary = schedule[1]['SUMMARY']
                if 'DTSTART' in schedule[1].keys():
                    startdate = schedule[1]['DTSTART'][:8]
                elif 'DTSTART;VALUE=DATE' in schedule[1].keys():
                    startdate = schedule[1]['DTSTART;VALUE=DATE'][:8]
                
                if 'DTEND' in schedule[1].keys():
                    enddate = schedule[1]['DTSTART'][:8]
                elif 'DTEND;VALUE=DATE' in schedule[1].keys():
                    enddate = schedule[1]['DTEND;VALUE=DATE'][:8]
                schedulelist.append((var,summary,(startdate,enddate)))
            return schedulelist

if __name__=='__main__':
    c = CalDAV()
    c.getSchedules(datetime.datetime.now(),1)