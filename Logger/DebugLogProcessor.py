from LogProcessor import LogProcessor
from Enums.LogLevel import LogLevel

class DebugLogProcessor(LogProcessor):
    def __init__(self, next_log_processor:LogProcessor):
        super().__init__(next_log_processor)
        
    def log(self,log_level:LogLevel,msg):
        if(log_level==LogLevel.DEBUG):
            print(log_level.value+" : "+msg)
        else:
            super().log(log_level,msg)