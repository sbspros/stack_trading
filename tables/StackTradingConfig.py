from dataclasses import dataclass,field
from tables.AppConfig import AppConfig
from tables.Symbol import Symbol
import yaml


class YamlFailure(Exception):
    def __init__(self):
        self.msg = 'Yaml file failed to load'
        super().__init__(self.msg) 

@dataclass
class StackTradingConfig(AppConfig):
    _symbols:list=field(init=False,default_factory=list)    

    def parse_config_file(self):
        try:
            with open('yaml/config.yaml','r') as file:
                app_info=yaml.safe_load(file)
        except:
            raise YamlFailure()
        
        ## Letup Logging
        self._file_name=app_info['Logging']['fileName']
        self._log_level=app_info['Logging']['logLevel']

        ## Get App date
        for symbol in app_info['SymbolName']:
            symbol_info=Symbol(symbol)
            self._symbols.append(symbol_info)

        self._schema_name=app_info['DataBase']['Schema']