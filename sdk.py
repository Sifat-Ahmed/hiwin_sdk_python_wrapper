from ctypes import *
from sys import platform
import time
import random
from Connector import Connection
from Motion import PTPMotion

conn = Connection()
dll = conn.get_dll()
device_id = conn.connect("192.168.1.2", 1)
ptpmotion = PTPMotion(dll)

if device_id >= 0:
    print("Connection established with code", device_id)
    

    dll.set_override_ratio(device_id, 100)
    
    posarr = [0, 0, 0, 0, 0, 0, ]

    for i in range(0, 30):
        posarr[0] = random.randint(-400, 0)
        posarr[1] = random.randint(460, 635)
        posarr[2] = random.randint(-97, -12)
        posarr[3] = random.randint(-98, -10)
        posarr[4] = 0
        posarr[5] = 0
        
        #pos = (c_double * len(posarr))(*posarr)
        ptpmotion.ptp_pos(device_id, 1, posarr)
        #print(posarr)
        time.sleep(2)


    conn.disconnect(device_id)
else:
    print("Connection has terminated with code", device_id)



