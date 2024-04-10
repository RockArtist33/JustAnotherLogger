from justanotherlogger import Logger

def test_LogTypes():
    assert Logger.DEBUG  == -1
    assert Logger.INFO   ==  0
    assert Logger.NOTICE ==  1
    assert Logger.WARN   ==  2
    assert Logger.ERROR  ==  3

def test_LogSetup():
    Log = Logger.Logger()
    assert Log.setup() == 0
    assert Log.setup(type=Logger.DEBUG) == 0
    assert Log.setup(type=Logger.INFO) == 0
    assert Log.setup(type=Logger.NOTICE) == 0
    assert Log.setup(type=Logger.WARN) == 0
    assert Log.setup(type=Logger.ERROR) == 0

def test_LogDebug():
    Log = Logger.Logger()
    Log.setup(Logger.DEBUG)
    assert Log.log(type=Logger.DEBUG, message="Test Message") == 0
    assert Log.log(type=Logger.INFO, message="Test Message") == 0
    assert Log.log(type=Logger.NOTICE, message="Test Message") == 0
    assert Log.log(type=Logger.WARN, message="Test Message") == 0
    assert Log.log(type=Logger.ERROR, message="Test Message") == 0

def test_LogInfo():
    Log = Logger.Logger()
    Log.setup(Logger.INFO)
    assert Log.log(type=Logger.DEBUG, message="Test Message") == 7
    assert Log.log(type=Logger.INFO, message="Test Message") == 0
    assert Log.log(type=Logger.NOTICE, message="Test Message") == 0
    assert Log.log(type=Logger.WARN, message="Test Message") == 0
    assert Log.log(type=Logger.ERROR, message="Test Message") == 0

def test_LogNotice():
    Log = Logger.Logger()
    Log.setup(Logger.NOTICE)
    assert Log.log(type=Logger.DEBUG, message="Test Message") == 7
    assert Log.log(type=Logger.INFO, message="Test Message") == 7
    assert Log.log(type=Logger.NOTICE, message="Test Message") == 0
    assert Log.log(type=Logger.WARN, message="Test Message") == 0
    assert Log.log(type=Logger.ERROR, message="Test Message") == 0

def test_LogWarn():
    Log = Logger.Logger()
    Log.setup(Logger.WARN)
    assert Log.log(type=Logger.DEBUG, message="Test Message") == 7
    assert Log.log(type=Logger.INFO, message="Test Message") == 7
    assert Log.log(type=Logger.NOTICE, message="Test Message") == 7
    assert Log.log(type=Logger.WARN, message="Test Message") == 0
    assert Log.log(type=Logger.ERROR, message="Test Message") == 0

def test_LogError():
    Log = Logger.Logger()
    Log.setup(Logger.ERROR)
    assert Log.log(type=Logger.DEBUG, message="Test Message") == 7
    assert Log.log(type=Logger.INFO, message="Test Message") == 7
    assert Log.log(type=Logger.NOTICE, message="Test Message") == 7
    assert Log.log(type=Logger.WARN, message="Test Message") == 7
    assert Log.log(type=Logger.ERROR, message="Test Message") == 0
