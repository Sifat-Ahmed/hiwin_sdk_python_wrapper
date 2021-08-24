from ctypes import *

class PTPMotion:
    def __init__(self, dll):
        
        self.__exe = dll

        self.__ptp_pos = self.__exe.ptp_pos
        #self.__ptp_pos.argtypes = []

    def ptp_pos(self, device_id : int, level : int, pos ): 
        device_id = device_id
        level = c_int(level)
        posarr = (c_double * len(pos))(*pos)
        print(pos)
        self.__ptp_pos(device_id, level, posarr)
        