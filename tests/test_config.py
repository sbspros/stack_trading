from tables.StackTradingConfig import StackTradingConfig

def test_config():
    stack_trading=StackTradingConfig()
    assert stack_trading._file_name=='logs/logfile2.log'

    