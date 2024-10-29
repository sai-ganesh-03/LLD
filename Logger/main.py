from InfoLogProcessor import InfoLogProcessor
from ErrorLogProcessor import ErrorLogProcessor
from DebugLogProcessor import DebugLogProcessor
from Enums.LogLevel import LogLevel

def main():
    log_processor=InfoLogProcessor(DebugLogProcessor(ErrorLogProcessor(None)))
    
    log_processor.log(LogLevel.INFO,"I'm info msg")
    log_processor.log(LogLevel.DEBUG,"I'm debug msg")
    log_processor.log(LogLevel.ERROR,"I'm error msg")
    
    
if __name__=="__main__":
    main()