from dataclasses import dataclass,field
from abc import ABC,abstractmethod

@dataclass
class AppConfig(ABC):
    # AppInfo
    _version:str=field(init=False)
    _appName:str=field(init=False)
    _status:str=field(init=False) 
    _github:str=field(init=False)
  
    #Logging:
    _file_name:str=field(init=False,default='logs/logfile2.log')
    _log_level:int=field(init=False,default=20)


    @abstractmethod
    def parse_config_file(self):
        pass
