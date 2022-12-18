from common.BaseClass import BaseClass
from connector.BinanceConnection import BinanceConnection

def test_config():
    bc=BaseClass()
    conn=BinanceConnection(bc)
