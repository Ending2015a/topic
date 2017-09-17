from tools.socket.serverSock import serverSock

import sys
import time


server = serverSock(name=sys.argv[1])
server.create(port=int(sys.argv[2]))

server.waitForClient()

while True:
    print('wait for task')
    cmd = server.recv().decode('ascii')
    print('get task \'{0}\''.format(cmd))
    cmd = cmd.split(' ')
    if cmd[0] == 'work':
        for i in range(int(cmd[1])):
            print('work' + str(i))
            time.sleep(1)

        print('done!!')
        server.send('done'.encode('ascii'))
    if cmd[0] =='bye':
        server.close()
        break


