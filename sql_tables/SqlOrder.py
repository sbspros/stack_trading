from common.BaseClass import BaseClass
from sql_tables.SqlTable import SqlTable,SQLCreateError,SqlSelectError,SqlInsertError 
from datetime import datetime 
import traceback


__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"

class SqlOrder(SqlTable):
    table_exists=False

    def create_table(self,bc,conn):
        try:
            sql_create_table = " CREATE TABLE IF NOT EXISTS {table_name} (\
                id integer PRIMARY KEY,\
                symbol text NOT NULL,\
                client_order_id text NOT NULL,\
                order_id text NOT NULL,\
                orig_qty text NOT NULL,\
                price float NOT NULL,\
                side text NOT NULL,\
                status text NOT NULL,\
                creatation_date INT,\
                modification_date INT\
                    ); ".format(table_name=self._table_name)
            conn.execute(sql_create_table)
            SqlOrder.table_exists=True
        except:
            bc.log.error("\t"+":"+traceback.format_exc())
            raise SQLCreateError

    def trunc(self,bc,conn):

        try:
            sql_select = "DELETE FROM {table_name} \
                    ; ".format(table_name=self._table_name)
            conn.execute(sql_select)
            cursor = conn.execute(sql_select)
            return cursor.fetchone()
        except:
            bc.log.error("\t"+":"+traceback.format_exc())
            raise SqlSelectError  


    def drop(self,bc,conn):

        try:
            sql_drop = "DROP TABLE IF EXISTS {table_name} \
                    ; ".format(table_name=self._table_name)
            bc.log.error(sql_drop)
            conn.execute(sql_drop)
            cursor = conn.execute(sql_drop)
            return cursor.fetchone()
        except:
            bc.log.error("\t"+":"+traceback.format_exc())
            raise SqlSelectError  


    def update(self,bc:BaseClass,conn):
        store_date=int(datetime.now().timestamp())
        sql_update = "update {table_name} \
            set status='{status}'\
            where order_id={order_id};".format(\
            table_name=self._table_name,\
            status=self._status,\
            order_id=self._order_id)
        bc.log.error(sql_update)
        conn.execute(sql_update)
        conn.commit()

    def delete():
        pass

    def insert(self,bc,conn):
        try:
            store_date=int(datetime.now().timestamp())
            sql_insert = "\
                insert into {table_name} (\
                symbol,client_order_id,\
                order_id ,orig_qty,\
                price,side,\
                status,\
                creatation_date,modification_date) values(\
                '{symbol}',\
                '{client_order_id}',\
                '{order_id}' ,'{orig_qty}',\
                '{price}','{side}',\
                '{status}',\
                {creatation_date},{modification_date}\
                );".format(\
                symbol=self._symbol,\
                client_order_id=self._client_order_id,\
                order_id=self._order_id ,orig_qty=self._orig_qty,\
                price=float(self._price),side=self._side,\
                status=self._status, table_name=self._table_name,\
                creatation_date=store_date,\
                modification_date=store_date)
            bc.log.error(sql_insert)
            conn.execute(sql_insert)
            conn.commit()
        except:
            bc.log.error("\t"+":"+traceback.format_exc())
            raise SqlInsertError        
        pass

    def select(self,bc,conn):

        try:
            sql_select = " select * from {table_name} \
                where order_id ='{order_id}'\
                    ; ".format(table_name=self._table_name,\
                        order_id=self._order_id)
            conn.execute(sql_select)
            cursor = conn.execute(sql_select)
            return cursor.fetchone()
        except:
            bc.log.error("\t"+":"+traceback.format_exc())
            raise SqlSelectError        

    def in_database(self,bc,conn):
        if self.select(bc,conn)==None:
            return False
        return True

    def select_price_range(bc,conn,low,high,symbol,side):

        try:
            sql_select = " select * from {table_name} \
                where price between {low} and {high}\
                    and symbol = '{symbol}' and side='{side}'\
                    ; ".format(table_name='Orders',\
                        low=float(low),high=float(high),\
                            symbol=symbol,\
                            side=side)
            bc.log.error(sql_select)
            conn.execute(sql_select)
            cursor = conn.execute(sql_select)
            return cursor.fetchall()
        except:
            bc.log.error("\t"+":"+traceback.format_exc())
            raise SqlSelectError
