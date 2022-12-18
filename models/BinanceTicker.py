from common.BaseClass import BaseClass
from connectors.BinanceConnection import BinanceConnection,Client
from tables.TickerWeb import TickerWeb
import traceback
import os

class TickerFailed(Exception):
    def __init__(self):
        self.msg = 'Could not get a ticker.'
        super().__init__(self.msg)

class BinanceTicker():
    def __init__(self,bc:BaseClass,conn:BinanceConnection):
        self._bc=bc
        self._conn=conn

    def ticker(self,symbol:str):
        try:
            ticks=self._conn._client.get_klines(symbol=symbol,interval=Client.KLINE_INTERVAL_1MINUTE)
            return(self.parse_ticker(ticks[-1]))
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise TickerFailed()


    def parse_ticker(self,record):
        ticker=TickerWeb()
        ticker.parse(record)
        return ticker
