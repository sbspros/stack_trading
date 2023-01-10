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

class SqlAsset(SqlTable):
    table_exists=False

    def create_table(self,bc,conn):
        try:
            sql_create_table = " CREATE TABLE IF NOT EXISTS {table_name} (\
                id integer PRIMARY KEY,\
                name TEXT,\
                free TEXT,\
                locked TEXT,\
                date_time INT,\
                tradable TEXT,\
                creatation_date INT,\
                modification_date INT\
                    ); ".format(table_name=self._table_name)
            conn.execute(sql_create_table)
        except:
            bc.log.error("\t"+":"+traceback.format_exc())
            raise SQLCreateError

    def update():
        pass

    def delete():
        pass

    def insert(self,bc,conn):
        try:
            store_date=int(datetime.now().timestamp())
            sql_insert = "insert into {table_name} (\
                name,free,\
                locked,date_time,\
                tradable,\
                creatation_date,modification_date) values (\
                '{name}','{free}',\
                '{locked}',{date_time},\
                '{tradable}',\
                {creatation_date},{modification_date}\
                );".format(\
                table_name=self._table_name,\
                name=self._name,free=self._free,\
                locked=self._locked,date_time=self._date_time,\
                tradable=self._tradable,\
                creatation_date=store_date,\
                modification_date=store_date)
            conn.execute(sql_insert)
            conn.commit()
        except:
            bc.log.error("\t"+":"+traceback.format_exc())
            raise SqlInsertError        
        pass

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

    def select(self,bc,conn):

        try:
            sql_select = " select * from {table_name} \
                    ; ".format()
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