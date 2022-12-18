from common.Logging import Logging,LoggingException
from tables.StackTradingConfig import StackTradingConfig
import platform
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "2.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"

## BaseClass now uses yaml for the config file

class AppException(Exception):
    def __init__(self):
        self.msg = 'Application has stopped, please check error logs'
        super().__init__(self.msg)

class BaseClass:
    """
    This class sets up the logging and ini variables
    for other objects to use. It
        - Will have variable and methods needed by other objects
        - Load in the config file
        - Setup any logging

    """
    def __init__(self):
        self.line_feed='\n'
        if platform.platform()[0:7]=='Windows':
            self.line_feed='\r\n'
        try:
            ## Get config values
            self._config=StackTradingConfig()
            self._config.parse_config_file()

            ## Start of Logs
            self.log = Logging(self._config._file_name,\
                int(self._config._log_level))

        except LoggingException as err:
            print("\t"+":"+traceback.format_exc())
            print("Logging Error")
            self._log_error=True

        except :
            print("\t"+":"+traceback.format_exc())
            print("Here in error area")
