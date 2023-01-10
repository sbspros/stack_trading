from common.BaseClass import BaseClass
from connectors.BinanceConnection import BinanceConnection
from connectors.SqlConnector import SqlConnector
from controllers.GetAccountInfo import GetAccountInfo
from controllers.ReviewExistingOrders import ReviewExistingOrders
from controllers.CreateNewOrders import CreateNewOrders
from sql_tables.CreateTables import CreateTables

class StackTrading():

    def __init__(self,bc:BaseClass):
        self._bc=bc
        self._conn=SqlConnector(self._bc,self._bc._config._schema_name)._conn
        self._client=BinanceConnection(self._bc)
        CreateTables(bc,self._conn)

    def start_trading(self):
        ## Get account balances
        account_info = GetAccountInfo(self._bc,self._client,self._conn)

        ## check existing orders
        review_orders = ReviewExistingOrders(self._bc,self._client,self._conn)
        symbols=review_orders.process_orders()

        ## Create new orders
        CreateNewOrders(self._bc,self._client,self._conn)