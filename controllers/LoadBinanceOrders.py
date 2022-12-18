from common.BaseClass import BaseClass
from connectors.BinanceConnection import BinanceConnection
from connectors.SqlConnector import SqlConnector
from models.BinanceOpenOrders import BinanceOpenOrders
from tables.Order import Order


class LoadBinanaceOrders():

    def __init__(self,bc:BaseClass):
        self._bc=bc

    def load_orders(self):
        conn=BinanceConnection(self._bc)
        sql_conn=SqlConnector(self._bc, self._bc._config._schema_name)
        open_orders=BinanceOpenOrders(self._bc,conn)

        for symbol in self._bc._config._symbols:
            orders=open_orders.open_orders(symbol._name)
            for order in orders:
                order_info=Order(\
                    _order_id=order['orderId'],\
                    _symbol=order['symbol'],\
                    _client_order_id=order['clientOrderId'],\
                    _price=order['price'],\
                    _orig_qty=order['origQty'],\
                    _status=order['status'],\
                    _side=order['side'],
                            )
                if order_info.is_created(sql_conn._conn)==False:
                    order_info.create_table(self._bc,sql_conn._conn)
                if order_info.in_database(self._bc,sql_conn._conn)==False:
                    order_info.insert(self._bc,sql_conn._conn)
                symbol._orders.append(order_info)

                self._bc.log.debug(str(order_info))
        return  symbol     