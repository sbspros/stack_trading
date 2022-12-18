from common.BaseClass import BaseClass

def test_config():
    bc=BaseClass()
    assert bc._config._file_name=='logs/logfile.log'
