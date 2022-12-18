from tables.Ticker import Ticker
from datetime import datetime

class TickerWeb(Ticker):


    def parse(self,ticker):
        self._open_time=ticker[0]
        self._open_price=ticker[1]
        self._close_price=ticker[2]
        self._high_price=ticker[3]
        self._low_price=ticker[4]
        self._volume=ticker[5]
        self._close_time=ticker[6]
        self._quote_asset_volume=ticker[7]
        self._taker_buy_base=ticker[8]
        self._taker_buy_asset=ticker[9]
        self._ticker_time_stamp="{date_str}".format(date_str=datetime.fromtimestamp(int(self._close_time/1000)))




        
