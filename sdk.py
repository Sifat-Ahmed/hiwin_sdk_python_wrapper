from ctypes import *
from sys import platform
import time
#shared_lib_path = ""

#shared_lib_path = r"lib/x86/HRSDK.dll"

# shared_lib_path = r"lib/x64/HRSDK.dll"
# try:
#     add_lib = CDLL(shared_lib_path)
#     print("Successfully loaded ", add_lib)
# except Exception as e:
#     print("Exception",e)


# CALLBACK = CFUNCTYPE(None, c_int,c_int, c_int, c_int)

# #@CFUNCTYPE(None, c_int, c_int, c_int, c_int)
# def callback(a, b, c, d):
#     #print("foo has finished its job (%d, %d)" % (a.value, b.value))
#     pass

# address = "192.168.1.2"
# level = c_int(1)
# callback_fn = CALLBACK(callback)

# bot = address.encode('utf-8')
# Connect = add_lib.open_connection
# Connect.argtypes = [c_char_p, c_int, CALLBACK]
# Connect.restype = c_int

# device_id = Connect(bot, level, callback_fn)

from Connector import Connection
from Motion import PTPMotion

conn = Connection()
dll = conn.get_dll()
device_id = conn.connect("192.168.1.2", 1)
ptpmotion = PTPMotion(dll)

if device_id >= 0:
    print("Connection established with code", device_id)
    

    posarr = [
				[ -400.0, 635.0, -12.0, -10.0, 0.0, 0.0 ],
				[ 0.0, 635.0, -12.0, -10.0, 0.0, 0.0 ],
				[ -50.0, 460.0, -12.0, -10.0, 0.0, 0.0 ],
				[ -400.0, 460.0, -12.0, -10.0, 0.0, 0.0 ],
				[ 0.0, 635.0, -97.0, -98.0, 0.0, 0.0 ],
				[ 0.0, 460.0, -93.0, -53.0, 0.0, 0.0 ],
            ]
	
    #add_lib.set_override_ratio(device_id, 100)
    
    for i in range(len(posarr)):
        pos = (c_double * len(posarr[i]))(*posarr[i])
        ptpmotion.ptp_pos(device_id, 1, pos)
        print(posarr[i])
        time.sleep(3)


    conn.disconnect(device_id)
else:
    print("Connection has terminated with code", device_id)



