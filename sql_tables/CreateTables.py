from common.BaseClass import BaseClass
from connectors.SqlConnector import SqlConnector
from tables.AccountInfo import AccountInfo
from tables.Asset import Asset
from tables.Order import Order
from tables.TempOrders import TempOrders

class CreateTables():
    def __init__(self,bc:BaseClass,conn:SqlConnector):
        self._bc=bc
        self._sql_conn=conn
        #=SqlConnector(self._bc, self._bc._config._schema_name)
        self.check_table(AccountInfo())
        self.check_table(Asset())
        self.check_table(Order())
        self.check_table(TempOrders())

    def check_table(self,table):
 
        if table.is_created(self._sql_conn)==False:
            table.create_table(self._bc,self._sql_conn)