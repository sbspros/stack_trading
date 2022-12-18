from tables.StackTradingConfig import StackTradingConfig
import traceback
def test_config():
    stack_trading=StackTradingConfig()
    try:
        stack_trading.parse_config_file()
        assert stack_trading._file_name=='logs/logfile.log'
    except KeyError as e:
        print("Key Error")
        print("\t"+":"+traceback.format_exc())
        assert False
    except:
        print("\t"+":"+traceback.format_exc())
        assert False