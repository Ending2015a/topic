from ..log.LogWriter import LogWriter

import sys

py_ver = sys.version_info.major

if py_ver == 2:
    from Queue import PriorityQueue
else:
    from queue import PriorityQueue

import threading as th


class Worker(th.Thread):
    number = 0
    def __init__(self, tasks, log=None, name=None):
        th.Thread.__init__(self)
        self.tasks = tasks
        if name == None:
            name = 'Worker{0}'.format(self.number)
            self.number += 1
        self.log = LogWriter(log, True, name=name)
        
        self.paused = False
        self.pause_cond = th.Condition(th.Lock())

        # this will stop the thread when main thread is terminated
        self.daemon = True
        self.start()

    def run(self):
        while True:
            with self.pause_cond:
                while self.paused:
                    self.pause_cond.wait()

            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as e:
                self.log.Error(str(e))
            finally:
                self.tasks.task_done()

    def pause(self):
        self.paused = True
        self.pause_cond.acquire()

    def resume(self):
        self.paused = False
        self.pause_cond.notify()
        self.pause_cond.release()


class ThreadPool:
    def __init__(self, num_threads, log=None, name=None):
        self.workers=[]
        self.tasks = PriorityQueue(num_threads*3)
        for n in range(num_threads):
            tname = name
            if name != None:
                tname='{0}{1}'.format(name, n)
            
            self.workers.append(Worker(self.tasks, log=log, name=tname))

    def add_task(self, priority,  func, *args, **kargs):
        self.tasks.put((priority, func, args, kargs))

    def wait_completion(self):
        self.tasks.join()



