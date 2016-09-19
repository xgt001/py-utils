import datetime
import os
import inspect
import json

'''
Invocation:

logger = imp.load_source('logger', '../logger.py')
LOGPATH = '../'
LOGFILE = 'p.log'
LOG_WRITER = logger.Logging(open(LOGPATH+LOGFILE,'a',buffering=0)) #enables instant logging
LOG_WRITER.write('test')

'''
class Logging(object):
    def __init__(self, file_pointer):
        self.file_pointer = file_pointer

    def write(self, message=None):
        """
            This logs the 'message' sent to it
            @type message  : String
        """
        log_data = {}
        log_data['timestamp'] = str(datetime.datetime.utcnow())
        log_data['message'] = message
        log_data['pid'] = os.getpid()
        directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        _file = inspect.getfile(inspect.currentframe())
        log_data['hostname'] = os.uname()[1]
        log_data['path'] = directory + "/" + _file
        json_out = json.dumps(log_data)
        self.file_pointer.write(json_out)
        self.file_pointer.write("\n")
