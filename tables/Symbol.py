from dataclasses import dataclass,field


@dataclass
class Symbol():
    _name:str
    _pairs:list=field(init=False,default_factory=list)  
    _orders:list=field(init=False,default_factory=list)  