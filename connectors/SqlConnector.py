import sqlite3
from common.BaseClass import BaseClass,AppException
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"


class ConnectFailed(Exception):
    def __init__(self):
        self.msg = 'Media Finder failed to initialize'
        super().__init__(self.msg)
        
class SqlExecError(Exception):
    def __init__(self):
        self.msg = 'SQL query failed to run'
        super().__init__(self.msg)

class  SqlError (Exception):
    def __init__(self):
        self.msg = 'SQL - General Error'
        super().__init__(self.msg)       

class SqlConnector():

    def __init__(self,bc:BaseClass,database:str):
        self._bc=bc
        try:
            ## Load the clase in
            self._conn=sqlite3.connect(database)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise AppException

    def local_exec(self,query):
        create_flag=None
        try:
            create_flag=self._conn.execute(query)
        except SqlExecError:
            self._bc.log.error("\t: SQL Query error")
            raise SqlError
        except:
            self._bc.log.error("\t:"+traceback.format_exc())
            raise AppException
        finally:
             return create_flag   