from dataclasses import dataclass,field
from sql_tables.SqlAsset import SqlAsset

@dataclass
class Asset(SqlAsset):
    _name:str=field(init=False)
    _free:str=field(init=False)
    _locked:str=field(init=False)
    _date_time:int=field(init=False)
    _tradable:str="False"
    _creatation_date:int=0
    _modification_date:int=0
    _table_name:str='assets'
    def parse_data(self,asset,data_time):    
        self._name=asset['asset']
        self._free=asset['free']
        self._locked=asset['locked']
        self._date_time=data_time