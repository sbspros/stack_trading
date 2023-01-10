from common.BaseClass import BaseClass
from connectors.BinanceConnection import BinanceConnection
from connectors.SqlConnector import SqlConnector
from models.BinanceOpenOrders import BinanceOpenOrders
from tables.TempOrders import TempOrders
from tables.Order import Order

class LoadBinanaceOrders():

    def __init__(self,bc:BaseClass,binanace_conn:BinanceConnection,conn:SqlConnector):
        self._bc=bc
        self._conn=conn
        self._binanace_conn=binanace_conn
        TempOrders().trunc(self._bc,self._conn)


    def load_orders(self):
        open_orders=BinanceOpenOrders(self._bc,self._binanace_conn)

        for symbol in self._bc._config._symbols:
            orders=open_orders.open_orders(symbol._name)
            for order in orders:
                print (order)
                ## Added for testing
                #order_info=TempOrders()
                #print(order_info)
                #order_info.insert(self._bc,self._conn)
                #self.compair_orders(order_info)
                #ssymbol._orders.append(order_info)
        return  symbol

    def compair_orders(self,order_info):
        select_data=self.read_order(order_info._order_id)
        db_order=Order()
        db_order.parse_select(select_data)
        if order_info!=db_order:
            if order_info._side=="BUY":
                order_info.bought(self._bc,self._conn)
            elif order_info._side=="SELL":
                order_info.sold(self._bc,self._conn)

    def read_order(self,order_id):
        db_order=Order()
        db_order._order_id=order_id
        return db_order.select(self._bc,self._conn)

    def save_new_orders(self,order_info):
        if order_info.in_database(self._bc,self._conn)==False:
                order_info.insert(self._bc,self._conn)     