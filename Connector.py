from ctypes import *

class Connection:
    def __init__(self, dll_path = r"lib/x64/HRSDK.dll"):
        self.__dll_path = dll_path
        
        try:
            self.__exe = CDLL(self.__dll_path)
            print("DLL loaded", self.__exe)
        except Exception as e:
            print("DLL problem")
            print(e)
    
        def __callback( a, b, c, d):
            pass
        self.__CALLBACK = CFUNCTYPE(None, c_int, c_int, c_int, c_int)
        self.__callback_fn = self.__CALLBACK(__callback)

        ## Connection function reference
        ## Takes 3 arguments, IP address (Str), level (int), CallBack (Function)
        ## Returns ID of the robot
        self.create_connection = self.__exe.open_connection
        self.create_connection.argtypes = [c_char_p, c_int, self.__CALLBACK]
        self.create_connection.restype = c_int
        
        ## Disconnect function reference 
        ## Takes the robot id/device id as argument (int)
        ## Returns 1 / 0
        self.__disconnect = self.__exe.disconnect
        self.__disconnect.argtypes = [c_int]
        self.__disconnect.restype = c_int

        
        ## Sets the connection level
        ## Requires two arguments, device/robot id (int) and mode (int) 
        self.__set_connection_level = self.__exe.set_connection_level
        self.__set_connection_level.argtypes = [c_int, c_int]
        self.__set_connection_level.restype = c_int
        
        ## gets the level of connection 
        ## requires the device/robot id (int)
        self.__get_connection_level = self.__exe.get_connection_level
        self.__get_connection_level.argtypes = [c_int]
        self.__get_connection_level.restype = c_int

        ## 
        self.__get_hrsdk_version = self.__exe.get_hrsdk_version
        self.__get_hrsdk_version.argtypes = [c_char_p]
        self.__get_hrsdk_version.restype = c_int

    def get_dll(self):
        return self.__exe
        
    def connect(self, address: str, level: int) -> int:
        address = address.encode('utf-8')
        level = c_int(level)
        device_id = self.create_connection(address, level, self.__callback_fn)
        self.__exe.set_override_ratio(device_id, 100)
        return device_id

    def disconnect(self, device_id : int) -> int:
        
        device_id = c_int(device_id)
        res = self.__disconnect(device_id)
        return res

    def set_connection_level(self, device_id :  int, level : int) -> int :
        device_id = c_int(device_id)
        level = c_int(level)
        res = self.__set_connection_level(device_id, level)
        return res
    
    def get_connection_level(self, device_id : int) -> int:
        device_id = c_int(device_id)
        res = self.__get_connection_level(device_id)        
        return res

    def get_hrsdk_version(self) -> str:
        version = "".encode('utf-8')
        version = self.__get_hrsdk_version(version)
        return version
    
if __name__ == "__main__":
    Conn = Connection()
    device_id = Conn.connect("192.168.1.2", 1)
        
    #if device_id >= 0:
        # print("Connection established with code", device_id)
        # ptpmotion = add_lib.ptp_pos

        # posarr = [
        # 			[ -400.0, 635.0, -12.0, -10.0, 0.0, 0.0 ],
        # 			[ 0.0, 635.0, -12.0, -10.0, 0.0, 0.0 ],
        # 			[ -50.0, 460.0, -12.0, -10.0, 0.0, 0.0 ],
        # 			[ -400.0, 460.0, -12.0, -10.0, 0.0, 0.0 ],
        # 			[ 0.0, 635.0, -97.0, -98.0, 0.0, 0.0 ],
        # 			[ 0.0, 460.0, -93.0, -53.0, 0.0, 0.0 ],
        #         ]
        
        # add_lib.set_override_ratio(device_id, 100)
        
        # for i in range(len(posarr)):
        #     pos = (c_double * len(posarr[i]))(*posarr[i])
        #     ptpmotion(device_id, c_int(1), pos)
        #     print(posarr[i])
        #     time.sleep(3)


        # print(Conn.get_connection_level(device_id))
        # print(Conn.get_hrsdk_version())

        # Conn.disconnect(device_id)
        # #add_lib.disconnect(device_id)
    # else:
    #     print("Connection has terminated with code", device_id)
