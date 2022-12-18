from common.BaseClass import BaseClass
from controllers.LoadBinanceOrders import LoadBinanaceOrders
from connectors.BinanceConnection import BinanceConnection
from models.BinanceTicker import BinanceTicker
from models.BinanceOrderStatus import BinanceOrderStatus
from connectors.SqlConnector import SqlConnector
from sql_tables.SqlOrder import SqlOrder
def get_binance_symbols(bc)->[]:

    symbols=LoadBinanaceOrders(bc)
    return symbols.load_orders()


def process_tickers(bc,symbols)->None:
    conn=BinanceConnection(bc)
    sql_conn=SqlConnector(bc, bc._config._schema_name)
    order_status = BinanceOrderStatus(bc,conn)
    get_ticker=BinanceTicker(bc,conn)
    for symbol in bc._config._symbols:
        ticker=get_ticker.ticker(symbol._name)
        for order in SqlOrder.select_price_range(bc,sql_conn._conn,'14.25','15.0',symbol._name,'SELL'):
                binance_order=order_status.order_status( symbol._name,order[3])
                if binance_order['side']=='SELL':
                    print('Order not sold')
                else:
                    print('Order sold')

        for order in SqlOrder.select_price_range(bc,sql_conn._conn,'14.25','15.0',symbol._name,'BUY'):
                binance_order=order_status.order_status( symbol._name,order[3])
                if binance_order['side']=='BUY':
                    print('Order not bought')
                else:
                    print('Need to create seel')
        #currentOrder = client.get_order(symbol=pair,orderId=orderId)
if __name__=="__main__":
    bc=BaseClass()
    symbols=get_binance_symbols(bc)
    process_tickers(bc,symbols)
