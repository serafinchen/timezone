
from datetime import datetime
import pytz

class Timezone:

    def __init__(self):
        
        self.result_timezone = pytz.utc
        self.custom_timezones = ['UTC', 'Pacific/Midway', 'America/Anchorage', 'America/Los_Angeles', 'America/Denver','America/Chicago', 'America/New_York', 'America/Caracas', 'America/Sao_Paulo', 'Atlantic/Azores','Europe/London', 'Europe/Berlin', 'Europe/Moscow', 'Asia/Dubai', 'Asia/Karachi','Asia/Dhaka', 'Asia/Bangkok', 'Asia/Hong_Kong', 'Asia/Tokyo', 'Australia/Sydney','Pacific/Auckland']

    def get_custom_timezones(self):
        return self.custom_timezones

    def get_current_time(self):
        string = str(datetime.now().astimezone())
        string2 = string[11:19]
        return string2
    
    def get_current_timezone(self):
        return datetime.now().astimezone().tzinfo
    
    def get_result_time(self):
        string = str(datetime.now(self.result_timezone))
        string2 = string[11:19]
        return string2
    
    def get_result_timezone(self):
        return self.result_timezone
    
    
    def change_result_timezone(self, timezone_name):
        self.result_timezone = pytz.timezone(timezone_name)
    
if __name__ == '__main__':
    testTime = Timezone()
    print(testTime.get_result_time())
    print(testTime.get_result_timezone())
    print("-----")
    testTime.change_result_timezone("Asia/Tokyo")
    print(testTime.get_result_time())
    print(testTime.get_result_timezone())