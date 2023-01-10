from common.BaseClass import BaseClass
from connectors.BinanceConnection import BinanceConnection
from connectors.SqlConnector import SqlConnector
from models.BinanceAccountInfo import BinanceAccountInfo
from tables.AccountInfo import AccountInfo
class GetAccountInfo():

    def __init__(self,bc:BaseClass,binanace_conn:BinanceConnection,conn:SqlConnector):
        account_info = BinanceAccountInfo(bc, binanace_conn)
        accounts=AccountInfo()
        accounts.pasrse_data(account_info.account_info())
        accounts.insert(bc,conn)