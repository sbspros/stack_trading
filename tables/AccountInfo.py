from dataclasses import dataclass,field
from sql_tables.SqlAccountInfo import SqlAccountInfo
from tables.Asset import Asset

@dataclass
class AccountInfo(SqlAccountInfo):
    _makerCommission:int=field(init=False)
    _takerCommission:int=field(init=False)
    _buyerCommission:int=field(init=False)
    _sellerCommission:int=field(init=False)
    _canTrade:bool=field(init=False)
    _canWithdraw:bool=field(init=False)
    _canDeposit:bool=field(init=False)
    _brokered:bool=field(init=False)
    _requireSelfTradePrevention:bool=field(init=False)
    _updateTime:int=field(init=False)
    _accountType:str=field(init=False)
    _asset_list:list=field(default_factory=list)
    _creatation_date:int=0
    _modification_date:int=0 
    _table_name:str='account_info'

    def pasrse_data(self,account_info): 
        self._makerCommission=account_info['makerCommission']
        self._takerCommission=account_info['takerCommission']
        self._buyerCommission=account_info['buyerCommission']
        self._sellerCommission=account_info['sellerCommission']
        self._canTrade=account_info['canTrade']
        self._canWithdraw=account_info['canWithdraw']
        self._canDeposit=account_info['canDeposit']
        self._brokered=account_info['brokered']
        self._requireSelfTradePrevention=account_info['requireSelfTradePrevention']
        self._updateTime=account_info['updateTime']
        self._accountType=account_info['accountType']
        for asset in account_info['balances']:
            if asset['free']!='0.00000000' or asset['locked']!='0.00000000':
                asset_balance=Asset()
                asset_balance.parse_data(asset,self._updateTime)
                self._asset_list.append(asset_balance)
