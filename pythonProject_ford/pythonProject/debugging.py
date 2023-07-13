import test
from test import open_Fenix
from canoe_open import canalyzer
import time

# def log_in(web,url,number,software,Vehicle_number,VIN,level,hours,json,Filepath):
Ota_ChromeDriver=r"C:\chromedriver_win32\chromedriver.exe"                        # 驱动器的地址
Ota_FinexUserId='YYU66@ford.com'                                                  # 输入账号
Ota_FinexEnvironment='production'                                                 # 选择环境  #production/sandbox
Ota_RolloutDescription='AC'                                                       # 输入ROLLOUT的描述
Ota_VehicleSet='CDX707_Prod_TT'                                                   # 选择车辆分组
Ota_VehicleVin='279'                                                              # 选择VIN
Ota_SoftwareSet='CD707C_GSM_732_TT_AB'                                            # 选择软件包
Ota_Install_Strategy='Null'                                                        # 选择安装策略
Ota_Inhibit_Required='Y'                                                           # 选择Inhibit Required
Ota_UploadJsonDirect='No'                                                         # 是否需要添加json,yes:添加
Ota_SWStype='单件改DC'                                                              # 判断是单件改DC还是两个件同时改DC
Ota_JsonfilePath=r"C:\Users\YYU66\Desktop\MMOTA\Config\schema_dc_sample_json.json"            # 选择本地json文件(单件的DC)
Ota_JsonfilePath1=r"C:\Users\YYU66\Desktop\MMOTA\Config\schema_dc_sample_json_New.json"       # 选择本地json文件(第二个ECU的DC)
Ota_ExpirationHours='5'                                                           # OTA超时时间
Ota_UserConsentLevel='1'                                                          # 选择用户等级
#
#
# # 引入变量
# # Real_Result = test.open_Fenix.log_in(Ota_ChromeDriver,Ota_FinexUserId,Ota_FinexEnvironment,Ota_RolloutDescription,Ota_VehicleSet,Ota_VehicleVin,Ota_SoftwareSet,Ota_Install_Strategy,Ota_Inhibit_Required,Ota_UploadJsonDirect,Ota_SWStype,Ota_JsonfilePath,Ota_JsonfilePath1,Ota_ExpirationHours,Ota_UserConsentLevel)
# # time.sleep(5)        # 等待5秒钟
# app=canalyzer()      # CANalyzer定义对象为app
# app.open_cfg(r"C:\Users\YYU66\Desktop\MMOTA\Config\Configuration_12.0Lin\Configuration_12.0LIN_Crash_120\Configuration1_crash.cfg")       # 导入某个CANalyzer config
# #time.sleep(5)        # 等待5秒钟
# #app.start_Measurement()  # 运行CAN工程
# #time.sleep(2)        # 等待2秒钟
# #app.stop_Measurement()   # 关闭CAN工程


