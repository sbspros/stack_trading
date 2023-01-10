from common.BaseClass import BaseClass
from connectors.BinanceConnection import BinanceConnection
from connectors.SqlConnector import SqlConnector
from controllers.LoadBinanceOrders import LoadBinanaceOrders
class ReviewExistingOrders():
    def __init__(self,bc:BaseClass,binanace_conn:BinanceConnection,conn:SqlConnector):
        self._bc=bc
        self._binance_conn=binanace_conn
        self._conn=conn

    def process_orders(self):
        orders=LoadBinanaceOrders(self._bc,self._binance_conn,self._conn)
        return orders.load_orders()

