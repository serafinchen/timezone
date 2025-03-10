from pytz import timezone
from datetime import datetime, timezone
import pytz
import time

class Timezone:

    def __init__(self):
        
        self.current_time = datetime.now()
        self.curren_timezone = self.current_time.astimezone().tzinfo
    
        self.result_time = datetime.now(timezone.utc)
        self.result_timezone = self.result_time.astimezone().tzinfo
        

    def get_current_time(self):
        return str(self.current_time)
    
    def get_current_timezone(self):
        return str(self.curren_timezone)
    
    def get_result_time(self):
        return str(self.result_time)
    
    def get_result_timezone(self):
        return str(self.result_timezone)
    
    
    def change_result_timezone(self, result_timezone):
        self.result_timezone = time.timezone(result_timezone)

    def change_result_time(self, result_timezone):
            self.result_time = self.current_time.astimezone(timezone(result_timezone))
    
    
    
if __name__ == '__main__':
    testTime = Timezone()
    print(testTime.get_current_time())
    print(testTime.get_current_timezone())
    print()
    print(testTime.get_result_time())
    print(testTime.get_result_timezone())