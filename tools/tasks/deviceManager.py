from junk.socket.clientSock import clientSock
from junk.log.LogWriter import LogWriter

'''
devices list = [
    ['name1', 'ip', port],
    ['name2', 'ip', port],
    ...
]
'''

class deviceManager(object):
    def __init__(self, devices_list=[], log=None, name='deviceManager'):
        self.device={}
        self.log = LogWriter(log, printout=True, name=name)
        self.name = name

        # add new devices to map
        self.addDevices(devices_list)


    def addDevices(self, devices_list=[]):
        for device in devices_list:
            form = self.__format(device[1], device[2])
            self.device[form] = {'name':device[0], 'ip':device[1], 'port':device[2],
                                    'sock': None, 'state':False}

    # create socket to connect with devices which is disconnected
    def waitForConnections(self, every_time_out=5):
        for form in self.devices:
            device = self.devices[form]
            # try to connect
            if device['state'] == False:
                sock = self.__wait_for_connections(device, every_time_out, log = self.log.path())
                device['sock'] = sock
                if sock != None:
                    device['state'] = True
                else:
                    device['state'] = False
                


    def __wait_for_connections(self, device, time_out, log):
        name = device[0]
        ip = device[1]
        port = device[2]
        sock = clientSock(log=log, name=name)
        if not sock.connect(ip=ip, port=port, time_out=time_out):
            self.log.Error('cannot connect to device \'{0}\', {1}:{2}'.format(name, ip, port))
            return None
        
        return sock
        

    def __connection_recovery(self):
        pass

    def __remove_bad_connections(self):
        pass

    def __format(self, ip, port):
        return '{0}:{1}'.format(ip , port)
