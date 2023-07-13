from test03 import Open_Edge

web_path = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python39\Scripts\chromedriver.exe' #浏览器驱动本机存放路径
UserName = 'apptest33'                                                                               #OTA网页登录账号
PassWord = 'Pass1234'                                                                                #OTA网页登录密码
ECU_Name = "VCU"                                                                                     #OTA升级ECU的名字
Supplier_CODE = 'ISSECCO1'                                                                           #供应商
N='2'                                                                                                #OTA任务分号（每次都要不一样，以对每一个OTA任务做区别）
AppVersion_Path = r'C:\OTA\233to247\AddVersion233to247'                                                      #版本文件路径
Original_Version = '233'                                                                             #原始软件版本
Target_Version = '247'                                                                               #目标软件版本
list2 = {"26494740.bin", "26494742.smd",                                                             #软件包list
         "26494743.mnf", "26494744.BC",
         "26494745.BC", "26494746.BC",
         "26494747.BC", "26494748.BC",
         "26494749.BC", "26494750.BC",
         "26494751.BC", "26495103.AB",
         "26495112.BC"}
PNfile_Path = r'C:\OTA\233to247\U458'                                                                #软件包的上一层文件路径
VIN = 'VIN707'                                                                                    #VIN号
SRRConfigInformationFile_path = r'C:\OTA\233to247\SRRconfiginformation233To247.xlsx'                 #SRR配置文件路径
WhiteListFile_Path = r'C:\OTA\VIN0707.xlsx'                                                          #白名单路径


edge = Open_Edge(web_path, UserName, PassWord, ECU_Name, Supplier_CODE, N, AppVersion_Path, Original_Version,
                 Target_Version, list2, PNfile_Path, VIN, SRRConfigInformationFile_path, WhiteListFile_Path)
edge.log_in()
edge.addECUInfo()
edge.Project_Config()
edge.NewECU_Config()
edge.Campaign_Management()



