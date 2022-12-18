from common.BaseClass import BaseClass
from abc import ABC,abstractmethod
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"

class SQLCreateError(Exception):
    def __init__(self):
        self.msg = 'Failed to create SQL Table'
        super().__init__(self.msg)

class SqlSelectError(Exception):
    def __init__(self):
        self.msg = 'Failed to exceute select'
        super().__init__(self.msg)

class SqlInsertError (Exception):
    def __init__(self):
        self.msg = 'Failed to exceute insert'
        super().__init__(self.msg)

class SqlTable(ABC):

    def is_created(self,conn)->None:
        query= "SELECT  name \
            FROM  \
                sqlite_schema \
            WHERE  \
                type='table' AND  \
                name='{table}' \
            ;".format(table=self._table_name) 

        cursor = conn.execute(query)
        result = cursor.fetchone()
        if result == None:
            return False
        else:
            return True

    @abstractmethod
    def create_table():
        pass

    @abstractmethod
    def update():
        pass

    @abstractmethod
    def delete():
        pass

    @abstractmethod
    def insert():
        pass

    @abstractmethod
    def select():
        pass
