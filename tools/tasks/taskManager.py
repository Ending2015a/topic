from .threadpool import ThreadPool
from ..log.LogWriter import LogWriter
from ..socket.clientSock import clientSock


class Task(object):
    def __init__(self, func, *argv, **kargv):
        self.state = False
        self

    def 
    

class taskManager(object):
    pool = None
    def __init__(self, num_thread, reliable, log=None, name=None):
        self.pool = ThreadPool(num_threads, log, name)
    

    def addTask(self, priority, func, *args, **kargs):
        task = Task()
    
