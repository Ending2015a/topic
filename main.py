import cv2
import threading as th
import tabulate

from tools.tasks import taskManager
from tools.log.LogWriter import LogWriter


devices = [
    ['Dory', 140.114.75.144, 8888],
    ['Dory', 140.114.75.144, 8889]
]

def main():
    tm = taskManager.create(devices=devices)
    tm.setTimeOut(10)
    connection_list = tm.waitForConnection()

    # TODO: init camera

    

if __name__ == '__main__':
    main()
