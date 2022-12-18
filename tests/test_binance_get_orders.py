from common.BaseClass import BaseClass
from connector.BinanceConnection import BinanceConnection
from models.BinanceOpenOrders import BinanceOpenOrders

def test_config():
    bc=BaseClass()
    conn=BinanceConnection(bc)
    open_orders=BinanceOpenOrders(bc,conn)
    orders=open_orders.open_orders('SOLUSDT')
    print(orders)
