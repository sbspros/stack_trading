from dataclasses import dataclass,field
from common.BaseClass import BaseClass
from connectors.SqlConnector import SqlConnector
from sql_tables.SqlOrder import SqlOrder
import uuid

@dataclass
class Order(SqlOrder):
    _symbol:str=field(init=False)
    _client_order_id:str=field(init=False)
    _order_id:str=field(init=False)
    _orig_qty:str=field(init=False)
    _price:str=field(init=False)
    _side:str=field(init=False)
    _status:str=field(init=False)
    _buy_price:str="0.0000"
    _sell_price:str="0.0000"
    _profit:str="0.0000"
    _creatation_date:int=0
    _modification_date:int=0    
    _table_name:str='orders'
    _order_list_id:int=field(init=False,repr=False)
    _execute_qty:str=field(init=False,repr=False)
    _cummulative_quote_qyt:str=field(init=False,repr=False)
    _time_in_force:str=field(init=False,repr=False)
    _order_type:str=field(init=False,repr=False)
    _stop_price:str=field(init=False,repr=False)
    _iceberg_qty:str=field(init=False,repr=False)
    _order_time:int=field(init=False,repr=False)
    _update_time:int=field(init=False,repr=False)
    _is_working:bool=field(init=False,repr=False)
    _orig_quote_order_qty:str=field(init=False,repr=False)

    def __eq__(self, other): 
        if not isinstance(other, Order):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return str(self._order_id) == str(other._order_id) \
                and self._side == other._side \
                and self._status == other._status

    def parse_data(self,order):
        self._order_id=order['orderId']
        self._symbol=order['symbol']
        self._client_order_id=order['clientOrderId']
        self._price=order['price']
        self._orig_qty=order['origQty']
        self._status=order['status']
        self._side=order['side']    

    def parse_select(self,order):
        self._order_id=order[3]
        self._symbol=order[1]
        self._client_order_id=order[2]
        self._price=order[5]
        self._orig_qty=order[4]
        self._status=order[7]
        self._side=order[6]    


    def add(self,symbol,buy_price,sell_price:float,qty):
        self._symbol=symbol
        self._side='pending'
        self._buy_price=buy_price
        self._sell_price="{sell:.3f}".format(sell=sell_price)
        self._client_order_id=uuid.uuid4().hex
        self._orig_qty=qty
        return float(self._orig_qty)*float(self._buy_price)

    def sell(self):
        if self._side=='buy':
            self._side='complete'
            self._profit=str(\
                (float(self._sell_price)-float(self._buy_price))*float(self._orig_qty))
            return {'profit':(self._profit),'return_amount':float(self._sell_price)*float(self._orig_qty)}
            # afterwards add the money taken out code
        return {'profit':0.0,'return_amount':0.0}

    def buy(self):
        if self._side=='pending':
            self._side='buy'
        # afterwards add the money taken out code

    def check_table(self, sql_conn):
        if SqlOrder.table_exists!=True:
            self.is_created(sql_conn)

    def side(self):
        return self._side

    def bought(self,bc):
        bc.log.info("Order was bought")

    def sold(self,bc:BaseClass,conn:SqlConnector):
        self._status="Complete"
        self.update()
        bc.log.info("Order was sold")
        