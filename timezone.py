from pytz import timezone
from datetime import datetime, timezone
import pytz

class Timezone:

    def __init__(self):
        
        self.current_time = datetime.now()
        self.curren_timezone = self.current_time.astimezone().tzinfo
    
        self.result_time = datetime.now(pytz.utc)
        self.result_timezone = self.result_time.tzinfo
        

    def get_current_time(self):
        return self.current_time
    
    def get_current_timezone(self):
        return self.curren_timezone
    
    def get_result_time(self):
        return self.result_time
    
    def get_result_timezone(self):
        return self.result_timezone
    
    
    def change_result_timezone(self, result_timezone):
        self.result_time = datetime.now(pytz.timezone(result_timezone))
        self.result_timezone = self.result_time.tzinfo
    
if __name__ == '__main__':
    testTime = Timezone()
    print(testTime.get_result_time())
    print(testTime.get_result_timezone())
    print("-----")
    testTime.change_result_timezone("Asia/Tokyo")
    print(testTime.get_result_time())
    print(testTime.get_result_timezone())