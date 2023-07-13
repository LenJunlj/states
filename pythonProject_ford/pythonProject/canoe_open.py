import os
import sys
import time
from win32com.client import *
from win32com.client.connect import *
class canalyzer:   # 定义canalyzer的类
    def __init__(self):
        self.application = None
        self.application = DispatchEx("CANalyzer.Application")
        self.ver = self.application.Version
        print('Loaded CANalyzer version ',
              self.ver.major, '.',
              self.ver.minor, '.',
              self.ver.Build, '...')  # , sep,''
        self.Measurement = self.application.Measurement.Running

    def open_cfg(self, cfgname):   # 打开本地CAN工程
        # open CANoe simulation
        if (self.application != None):
            # ##3#check for valid file ##and it is *.cfg file
            if os.path.isfile(cfgname) and (os.path.splitext(cfgname)[1] == ".cfg"):  # 动态获取CNA工程文件的本地路径
                self.application.Open(cfgname)
                print("opening..."+cfgname)
            else:
                raise RuntimeError("Can't find CANalyzer cfg file")
        else:
            raise RuntimeError("CANalyzer Not open")
    def close_cfg(self):          # 关闭CAN工程
        if (self.application != None):
            # self.stop_Measurement()
            self.application.Quit()
            self.application = None

    def start_Measurement(self):  # 运行CAN工程
        if(not self.application.Measurement.Running):
            self.application.Measurement.start()
        else:
            pass
    def stop_Measurement(self):   # 停止CAN工程
        if self.application.Measurement.Running:
            self.application.Measurement.stop()
        else:
            pass

# 获取CAN信号
    def get_signal(self,Bus_type,channel_num,msg_name,sig_name):
        if(self.application!=None):
            result=self.application.GetBus(Bus_type).GetSignal(channel_num,msg_name,sig_name)    # CAN工程配置的固定写法
            return result.Value    # 获取信号的对应的值
        else:
            raise RuntimeError("CANoe start measurement failed, Please Check Connection!")
# 发送CAN信号
    def set_signal(self,Bus_type,channel_num,msg_name,sig_name,setValue):
        if(self.application!=None):
            result=self.application.GetBus(Bus_type).GetSignal(channel_num,msg_name,sig_name)
            result.Value=setValue
        else:
            raise RuntimeError("CANoe start measurement failed, Please Check Connection!")



# 防止总线堵塞
    def DoEvents(self):
        pythoncom.PumpWaitingMessages()
        time.sleep(1)

# app =canalyzer()  # 实例化对
# app.open_cfg(r"C:\OTA\706\CANOE12\Configuration707(2).cfg") #导入某个CANoe config
# time.sleep(5)
# app.start_Measurement()
# ##.close_cfg()