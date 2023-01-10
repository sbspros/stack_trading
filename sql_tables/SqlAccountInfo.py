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

class SqlAccountInfo(SqlTable):
    table_exists=False

    def create_table(self,bc,conn):
        try:
            sql_create_table = " CREATE TABLE IF NOT EXISTS {table_name} (\
                id integer PRIMARY KEY,\
                makerCommission int, \
                takerCommission int,\
                buyerCommission int,\
                sellerCommission int,\
                canTrade text,\
                canWithdraw text,\
                canDeposit text,\
                brokered text,\
                requireSelfTradePrevention text,\
                updateTime int,\
                accountType text,\
                creatation_date int,\
                modification_date \
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
            self.trunc(bc,conn)
            store_date=int(datetime.now().timestamp())
            sql_insert = "insert into {table_name} (\
                makerCommission,takerCommission,\
                buyerCommission,sellerCommission,\
                canTrade,canWithdraw,\
                canDeposit,brokered,\
                requireSelfTradePrevention,updateTime,\
                accountType,\
                creatation_date,modification_date) values (\
                {makerCommission},{takerCommission},\
                {buyerCommission},{sellerCommission},\
                '{canTrade}','{canWithdraw}',\
                '{canDeposit}','{brokered}',\
                '{requireSelfTradePrevention}',{updateTime},\
                '{accountType}',\
                {creatation_date},{modification_date}\
                );".format(\
                table_name=self._table_name,\
                makerCommission=self._makerCommission,\
                takerCommission=self._takerCommission,\
                buyerCommission=self._buyerCommission,\
                sellerCommission=self._sellerCommission,\
                canTrade=self._canTrade,\
                canWithdraw=self._canWithdraw,\
                canDeposit=self._canDeposit,\
                brokered=self._brokered,\
                requireSelfTradePrevention=self._requireSelfTradePrevention,\
                updateTime=self._updateTime,\
                accountType=self._accountType,\
                creatation_date=store_date,\
                modification_date=store_date)
            conn.execute(sql_insert)
            conn.commit()
            for asset in self._asset_list:
                asset.insert(bc,conn)

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