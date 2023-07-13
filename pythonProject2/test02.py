import win32com.client
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.edge.options import Options
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pywinauto import Application
import pandas as pd
import openpyxl

#本地文件——PATH
current_file_path = os.path.abspath(__file__)
print(current_file_path)
parent_directory = os.path.dirname(current_file_path)
print(parent_directory)
grandparent_directory = os.path.dirname(parent_directory)
print(grandparent_directory)
AppVersion_Path = os.path.join(grandparent_directory, 'Add')
print(AppVersion_Path)
SRRConfigInformationFile_path = os.path.join(grandparent_directory, 'SRR')
print(SRRConfigInformationFile_path)
WhiteListFile_Path = os.path.join(grandparent_directory, 'VIN')
print(WhiteListFile_Path)
PNFile_Path = os.path.join(grandparent_directory, 'U')
print(PNFile_Path)
web_path = os.path.join(grandparent_directory, 'msedgedriver.exe')                                  #浏览器驱动本机存放路径
print(web_path)

# 读取Excel文件
df = pd.read_excel(r'C:\Users\Administrator\PycharmProjects\AddVersion233to247.xlsx')
e_values = df['Version Name'].tolist()
f_values = df['Part NO.'].tolist()
List = [f_values[i] for i in range(len(e_values) // 2)]
print(len(e_values) // 2)
print(List)

class Open_Edge():

    def __init__(self,User_Name,Pass_Word,ECU_Name,Supplier_CODE,N,
                 Original_Version,Target_Version,VIN):
        self.User_Name=User_Name
        self.Pass_Word=Pass_Word
        self.driver = webdriver.Edge(web_path)
        self.driver.implicitly_wait(200)
        self.ECU_Name = ECU_Name
        self.Supplier_CODE = Supplier_CODE
        self.N = N
        self.Original_Version=Original_Version
        self.Target_Version=Target_Version
        self.VIN = VIN
    def log_in(self):

        self.driver=webdriver.Edge(web_path)
        self.driver.get(r"https://vota-test.qa.sgmlink.com")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        #点击高级选项，进入ISMS管理平台
        self.driver.find_element(By.XPATH,'//*[@id="details-button"]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH,'//*[@id="proceed-link"]').click()
        self.driver.implicitly_wait(20)
        #SGM账号登录
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/button').click()
        self.driver.implicitly_wait(20)
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="j_username"]').send_keys(self.User_Name)
        self.driver.implicitly_wait(20)
        S0=self.driver.find_element(By.XPATH, '//*[@id="j_password"]')
        S0.send_keys(self.Pass_Word)
        self.driver.implicitly_wait(20)
        S0.send_keys(keys.Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="Button1"]').click()
        self.driver.implicitly_wait(200)


    def addECUInfo(self):
        #3.0软件管理平台
        S0=self.driver.find_element(By.XPATH,'//*[@id="app"]/section/main/div/div/form/div[2]/div/div')
        S0.click()
        self.driver.implicitly_wait(200)

        #ECU管理--新增
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/ul/li[1]/div[3]/img').click()#ECU管理
        self.driver.implicitly_wait(200)
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[2]/div[1]/span').click()#新增
        self.driver.implicitly_wait(200)
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div[2]/form/div[1]/div[1]/div/div[1]/input').send_keys(self.ECU_Name)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div[2]/form/div[1]/div[2]/div/div[1]/input').send_keys(self.Supplier_CODE)
        self.driver.implicitly_wait(20)
        # ISSECW序号下拉框及其选择
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div[2]/form/div[1]/div[3]/div/div/div/span/span/i').click()#下拉框
        self.driver.implicitly_wait(20)
        if int(self.N) >= 6:
            # js = "var q=document.getElementsByClassName('el-select-dropdown__wrap')[0].scrollTop = 10000"
            # driver.execute_script(js)
            target =self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[11]')  # 设置下拉框的目标元素
            self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的目标元素去
            time.sleep(2)
        if(self.N=="0"):
            self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()#序号选择
            self.driver.implicitly_wait(20)
            self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div[2]/div/span[2]').click()
            self.driver.implicitly_wait(20)
        elif(self.N=="1"):
            self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()  # 序号选择
            self.driver.implicitly_wait(20)
            self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div[2]/div/span[2]').click()
            self.driver.implicitly_wait(20)
        elif(self.N=="2"):
            self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[3]').click()  # 序号选择
            self.driver.implicitly_wait(20)
            self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div[2]/div/span[2]').click()
            self.driver.implicitly_wait(20)
        elif(self.N == "3"):
            self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[4]').click()  # 序号选择
            self.driver.implicitly_wait(20)
            self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div[2]/div/span[2]').click()
            self.driver.implicitly_wait(20)
        elif(self.N == "4"):
            self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[5]').click()  # 序号选择
            self.driver.implicitly_wait(20)
            self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div[2]/div/span[2]').click()
            self.driver.implicitly_wait(20)
        elif(self.N == "5"):
            self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[6]').click()  # 序号选择
            self.driver.implicitly_wait(20)
            self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div[2]/div/span[2]').click()
            self.driver.implicitly_wait(20)
        elif(self.N == "6"):
            self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[7]').click()  # 序号选择
            self.driver.implicitly_wait(20)
            self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div[2]/div/span[2]').click()
            self.driver.implicitly_wait(20)
        elif(self.N == "7"):
            self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[8]').click()  # 序号选择
            self.driver.implicitly_wait(20)
            self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div[2]/div/span[2]').click()
            self.driver.implicitly_wait(20)

        elif(self.N == "8"):
            self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[9]').click()  #
            self.driver.implicitly_wait(20)
            self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div[2]/div/span[2]').click()
            self.driver.implicitly_wait(20)
        elif(self.N == "9"):
            self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[10]').click()  # 序号选择
            self.driver.implicitly_wait(20)
            self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div[2]/div/span[2]').click()
            self.driver.implicitly_wait(20)
        elif(self.N == "10"):
            self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[11]').click()  # 序号选择
            self.driver.implicitly_wait(20)
            self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div[2]/div/span[2]').click()
            self.driver.implicitly_wait(20)

    def Project_Config(self):
        #项目配置
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/ul/div/li[1]/ul/div[3]/div/li').click()
        self.driver.implicitly_wait(20)
        time.sleep(2)
        #定位下拉框元素
        S0=self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/div[1]/div[1]/div/input')#在下拉框内输入项目名称
        S0.send_keys('4582025')
        time.sleep(2)
        S0.send_keys(keys.Keys.DOWN)
        self.driver.implicitly_wait(20)
        S0.send_keys(keys.Keys.ENTER)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/div[1]/button[1]').click()
        time.sleep(2)

        #4582025的配置点击
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/ul/li[1]/div/div[3]/div').click()
        self.driver.implicitly_wait(30)
        time.sleep(3)
        #新增按钮点击
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/ul/li[1]/div/div[5]/div/div/div[2]/div/div[1]/form/div[2]/div/span').click()
        time.sleep(12)
        #滑动新增界面到最底部
        js= "var q=document.getElementsByClassName('ecu-config')[0].scrollTop = 30000"
        self.driver.execute_script(js)
        time.sleep(5)
        form = self.driver.find_element(By.XPATH,'//div[@class="ecu-config"]//ul[@class="ecu-list"]//li[@class="ecu-item"][last()]')

        element1 = form.find_elements(By.CLASS_NAME,'el-input__inner')[0]
        element1.send_keys("0x8A")

        element2 = form.find_elements(By.CLASS_NAME,'el-input__inner')[1]
        element2.send_keys(self.ECU_Name+'_'+self.Supplier_CODE+'_'+self.N)
        time.sleep(2)
        element2.send_keys(keys.Keys.DOWN)
        time.sleep(2)
        element2.send_keys(keys.Keys.ENTER)
        time.sleep(2)

        #点击完成
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/ul/li[1]/div/div[5]/div/div/div[2]/div/div[2]/div[2]/span[1]').click()
        WebDriverWait(self.driver, 2000, 0.5).until_not(EC.presence_of_element_located((By.XPATH,
        '//*[@id="main-container"]/section/div[2]/div/ul/li[1]/div/div[5]/div/div/div[2]/div/div[2]/div[2]/span[1]')))
    def NewECU_Config(self):
        # #项目配置顶部搜索
        S0=self.driver.find_element(By.XPATH, '//*[@id="main-container"]/section/div[2]/div/div[1]/div[2]/div/input')
        S0.send_keys(self.ECU_Name + '_' + self.Supplier_CODE + '_' + self.N)
        self.driver.implicitly_wait(20)
        time.sleep(2)
        S0.send_keys(keys.Keys.DOWN)
        self.driver.implicitly_wait(20)
        time.sleep(1)
        S0.send_keys(keys.Keys.ENTER)
        self.driver.implicitly_wait(20)
        time.sleep(2)

        #版本管理
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/ul/li/div/ul/li/div[2]/div/div/span[1]').click()
        self.driver.implicitly_wait(20)
        #新增版本
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/div[1]/form/button').click()
        self.driver.implicitly_wait(20)
        #批量新增
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/div[2]/form/div[2]/div/div/label[2]/span[2]').click()
        self.driver.implicitly_wait(20)
        #添加本地AppVersion文件
        self.driver.find_element(By.XPATH,'//*[@id="version_Upload"]/div/div').click()
        time.sleep(2)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.Sendkeys(AppVersion_Path)
        time.sleep(2)
        shell.Sendkeys('{DOWN}' + '{ENTER}' + '\r\n')
        time.sleep(2)

        #点击完成
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/div[1]/div[1]/span[2]').click()
        self.driver.implicitly_wait(20)
        time.sleep(3)
        #回到项目配置

        S3=self.driver.find_element(By.XPATH,'//*[@id="main-container"]/ul/div/li[1]/ul/div[3]/div/li')
        S3.click()
        self.driver.implicitly_wait(20)
        time.sleep(3)

        #PN管理
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/ul/li/div/ul/li/div[2]/div/div/span[2]').click()
        self.driver.implicitly_wait(20)
        time.sleep(2)
        #添加PN文件

        a = 0
        for i in List:
            try:
                self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/div[1]/form/div[4]/div/div/input').send_keys(i)
                self.driver.implicitly_wait(20)
                time.sleep(2)
                self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/div[1]/form/div[5]/div/span').click()  # 查询
                time.sleep(5)
                self.driver.find_element(By.XPATH,
                '//*[@id="main-container"]/section/div[2]/div/div[3]/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr/td[8]/div/span').click()#点击上传按钮
                time.sleep(2)
                if(a<1):
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shell.Sendkeys(PNFile_Path + '{DOWN}' + '{ENTER}')
                    time.sleep(2)
                    shell.Sendkeys(i + '{ENTER}' + '\r\n')
                else:
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shell.Sendkeys(i + '{ENTER}' + '\r\n')
                WebDriverWait(self.driver, 2000, 0.5).until(EC.presence_of_element_located((By.XPATH,
                '//*[@id="main-container"]/section/div[2]/div/div[3]/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr/td[8]/div/a')))
                print('pass')
                self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/div[1]/form/div[6]/div/span').click()  # 重置
                self.driver.implicitly_wait(20)
                time.sleep(2)
                a += 1
                print(a)
            except:
                print(i)
                self.driver.find_element(By.XPATH, '//*[@id="main-container"]/section/div[2]/div/div[1]/form/div[6]/div/span').click()  # 重置
                time.sleep(5)
                continue
        time.sleep(2)

        # 回到项目配置
        S4= self.driver.find_element(By.XPATH, '//*[@id="main-container"]/ul/div/li[1]/ul/div[3]/div/li')
        S4.click()
        self.driver.implicitly_wait(20)
        time.sleep(2)

        # 升级文件
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/ul/li/div/ul/li/div[2]/div/div/span[3]').click()
        self.driver.implicitly_wait(20)
        # 新增
        self.driver.find_element(By.XPATH, '//*[@id="main-container"]/section/div[2]/div/div[1]/form/button').click()
        self.driver.implicitly_wait(20)
        time.sleep(2)
        # 新建升级文件——升级版本
        S5 = self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/div[3]/div/div[2]/div[1]/div[1]/form/div[1]/div/div/div[1]/input')
        S5.send_keys(self.Target_Version)
        time.sleep(2)
        self.driver.implicitly_wait(20)
        S5.send_keys(keys.Keys.DOWN)
        self.driver.implicitly_wait(20)
        S5.send_keys(keys.Keys.DOWN)
        self.driver.implicitly_wait(20)
        S5.send_keys(keys.Keys.ENTER)
        self.driver.implicitly_wait(20)
        # 新建升级文件——升级方式
        S6 = self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/div[3]/div/div[2]/div[1]/div[1]/form/div[2]/div/div/div/input')
        S6.send_keys('差分')
        self.driver.implicitly_wait(20)
        S6.send_keys(keys.Keys.DOWN)
        self.driver.implicitly_wait(20)
        S6.send_keys(keys.Keys.ENTER)
        self.driver.implicitly_wait(20)
        # 点击下一步
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div/button[2]').click()
        # self.driver.implicitly_wait(20)
        time.sleep(2)
        # 点击确认
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div/div[3]/div/div[2]/div[2]/div[2]/div/button[3]').click()
        self.driver.implicitly_wait(20)
        time.sleep(2)

    def Campaign_Management(self):
        # 点击campaign管理
        self.driver.find_element(By.XPATH, '//*[@id="main-container"]/ul/div/li[2]/div').click()
        self.driver.implicitly_wait(20)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="main-container"]/ul/div/li[2]/ul/div[1]/div/li').click()
        self.driver.implicitly_wait(20),
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="main-container"]/section/div[2]/div[3]/div[1]/span').click()
        self.driver.implicitly_wait(20)
        time.sleep(2)
        # 升级配置——基本信息
        S0 = self.driver.find_element(By.XPATH, '//*[@id="配置ECU"]/div[2]/form/div[1]/div[3]/div/div/div/input')
        S0.send_keys('4582025')
        time.sleep(3)
        self.driver.implicitly_wait(20)
        S0.send_keys(keys.Keys.DOWN)
        self.driver.implicitly_wait(20)
        S0.send_keys(keys.Keys.ENTER)
        time.sleep(2)
        S1 = self.driver.find_element(By.XPATH, '//*[@id="配置ECU"]/div[2]/form/div[1]/div[1]/div/div/input')
        S1.send_keys(self.ECU_Name + '_' + self.Original_Version + '_' + self.Target_Version + '_' + self.VIN)
        self.driver.implicitly_wait(20)

        S2 = self.driver.find_element(By.XPATH, '//*[@id="配置ECU"]/div[2]/form/div[1]/div[2]/div/div[1]/textarea')
        S2.send_keys(self.ECU_Name + '_' + self.Original_Version + '_' + self.Target_Version + '_' + self.VIN)

        time.sleep(2)

        # 升级配置——配置零件
        S1 = self.driver.find_element(By.XPATH, '//*[@id="配置版本"]/div[2]/form/div[1]/div/div[1]/div/input')
        S1.send_keys(self.ECU_Name + '_' + self.Supplier_CODE + '_' + self.N)
        self.driver.implicitly_wait(20)
        S1.send_keys(keys.Keys.DOWN)
        self.driver.implicitly_wait(20)
        S1.send_keys(keys.Keys.ENTER)
        self.driver.implicitly_wait(20)
        time.sleep(1)

        S3 = self.driver.find_element(By.XPATH,'//*[@id="配置版本"]/div[2]/form/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/input')
        S3.send_keys(self.Original_Version)
        self.driver.implicitly_wait(20)
        time.sleep(2)
        S3.send_keys(keys.Keys.DOWN)
        self.driver.implicitly_wait(20)
        S3.send_keys(keys.Keys.ENTER)
        self.driver.implicitly_wait(20)
        time.sleep(2)

        S4 = self.driver.find_element(By.XPATH,'//*[@id="配置版本"]/div[2]/form/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div[1]/input')
        S4.send_keys(self.Target_Version)
        self.driver.implicitly_wait(20)
        time.sleep(2)
        S4.send_keys(keys.Keys.DOWN)
        self.driver.implicitly_wait(20)
        time.sleep(2)
        S4.send_keys(keys.Keys.ENTER)
        self.driver.implicitly_wait(20)
        time.sleep(2)

        # 升级配置——配置信息
        self.driver.find_element(By.XPATH, '//*[@id="configFile"]/div').click()
        time.sleep(2)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.Sendkeys(SRRConfigInformationFile_path + '{DOWN}' + '{ENTER}' + '\r\n')
        self.driver.implicitly_wait(20)
        time.sleep(2)

        # 点击完成
        self.driver.find_element(By.XPATH, '//*[@id="main-container"]/section/div[2]/div[1]/div/span[2]').click()
        self.driver.implicitly_wait(20)
        time.sleep(1)


        # camp执行_点击
        self.driver.find_element(By.XPATH, '//*[@id="main-container"]/ul/div/li[2]/ul/div[2]/div/li').click()
        self.driver.implicitly_wait(20)
        time.sleep(1)
        # camp执行_新增
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[1]/form/div[7]/div/button').click()
        self.driver.implicitly_wait(20)
        time.sleep(1)

        S5 = self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/form/div[1]/div/div/input')
        S5.send_keys(self.ECU_Name + self.Original_Version + 'TTO' + self.Target_Version)
        self.driver.implicitly_wait(20)
        S6 = self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/form/div[2]/div/div/div[1]/input')
        S6.send_keys('4582025')
        self.driver.implicitly_wait(20)
        S6.send_keys(keys.Keys.DOWN)
        self.driver.implicitly_wait(20)
        S6.send_keys(keys.Keys.ENTER)
        self.driver.implicitly_wait(20)

        # 关闭手机OTA
        self.driver.find_element(By.XPATH,
        '//*[@id="main-container"]/section/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/form/div[3]/div/div/label[2]/span[1]/span').click()
        self.driver.implicitly_wait(20)
        time.sleep(2)
        # 添加任务
        self.driver.find_element(By.XPATH,
        '//*[@id="main-container"]/section/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/form/div[4]/div/div[1]/div/div[2]/div[3]/span[1]').click()
        self.driver.implicitly_wait(20)
        time.sleep(2)
        try:
            element3=self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[1]/div/div[1]/form/div[2]/div/div/input')#输入搜索值
            element3.send_keys(self.ECU_Name + '_' + self.Supplier_CODE + '_' + self.N)
            self.driver.implicitly_wait(20)
            time.sleep(2)

            self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[1]/div/div[1]/form/div[3]/div/span').click()  # 点击搜索
            self.driver.implicitly_wait(20)
            time.sleep(2)
            self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div[1]/label/span[2]').click()  # 选择搜索到的选项
            self.driver.implicitly_wait(20)
            time.sleep(2)

            self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/span[2]').click()  # 确认
            self.driver.implicitly_wait(20)
            time.sleep(2)
        except:
            element3 = self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[1]/div/div[1]/form/div[2]/div/div/input')  # 输入搜索值
            element3.send_keys(self.ECU_Name + '_' + self.Supplier_CODE + '_' + self.N)
            self.driver.implicitly_wait(20)
            time.sleep(2)

            self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[1]/div/div[1]/form/div[3]/div/span').click()  # 点击搜索
            self.driver.implicitly_wait(20)
            time.sleep(2)
            self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[1]/div/div[2]/div[1]/label/span[2]').click()  # 选择搜索到的选项
            self.driver.implicitly_wait(20)
            time.sleep(2)

            self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/span[2]').click()  # 确认
            self.driver.implicitly_wait(20)
            time.sleep(2)
            print('添加任务——except')

        # 添加白名单
        S7 = self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/form/div[4]/div/div[1]/div/div[2]/div[1]/div/div[4]/div/div[1]/div/div/span[1]')
        S7.click()
        time.sleep(2)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.Sendkeys(WhiteListFile_Path + '{DOWN}' + '{ENTER}' + '\r\n')
        time.sleep(2)

        # 新增campaign——确认点击
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/span[2]').click()
        self.driver.implicitly_wait(20)
        time.sleep(2)

        # 点击提交审核
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[2]/div[1]/div/div[1]/div[3]/div[8]/span').click()
        self.driver.implicitly_wait(20)
        # 审核人选择
        S8=self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[2]/div[7]/div/div[2]/div[1]/div/div/input')  # 下拉框
        S8.click()
        self.driver.implicitly_wait(20)
        time.sleep(1)
        S8.send_keys(keys.Keys.DOWN)
        self.driver.implicitly_wait(20)
        time.sleep(1)
        S8.send_keys(keys.Keys.ENTER)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[2]/div[7]/div/div[2]/div[2]/span[2]').click()  # 点击确认
        self.driver.implicitly_wait(20)
        time.sleep(2)

        # OTA审核
        self.driver.find_element(By.XPATH, '//*[@id="main-container"]/ul/div/li[3]/div').click()
        self.driver.implicitly_wait(200)
        time.sleep(2)
        # OTA审核——camp审核
        self.driver.find_element(By.XPATH, '//*[@id="main-container"]/ul/div/li[3]/ul/div/div/li').click()
        self.driver.implicitly_wait(20)
        time.sleep(2)
        # OTA审核——camp审核——审核
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[2]/div/div/div[2]/div/div[3]/table/tbody/tr[1]/td[6]/div').click()
        self.driver.implicitly_wait(20)
        # OTA审核——camp审核——审核——审核意见
        self.driver.find_element(By.XPATH, '//*[@id="verify-info"]/div[2]/form/div[3]/div/div[1]/textarea').send_keys('pass')
        self.driver.implicitly_wait(20)
        # OTA审核——camp审核——审核——审核意见——审核通过
        self.driver.find_element(By.XPATH, '//*[@id="verify-info"]/div[2]/div/span[2]').click()
        self.driver.implicitly_wait(20)
        time.sleep(2)
        # 点击campaign管理
        self.driver.find_element(By.XPATH, '//*[@id="main-container"]/ul/div/li[2]/div').click()
        self.driver.implicitly_wait(20)
        time.sleep(2)
        # campaign管理——camp执行
        self.driver.find_element(By.XPATH, '//*[@id="main-container"]/ul/div/li[2]/ul/div[2]/div/li').click()
        self.driver.implicitly_wait(20)

        # campaign管理——camp执行——执行
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[2]/div[1]/div/div[1]/div[3]/div[2]/span').click()
        self.driver.implicitly_wait(20)
        time.sleep(2)
        # campaign管理——camp执行——执行——确认
        self.driver.find_element(By.XPATH,'//*[@id="main-container"]/section/div[2]/div[2]/div[6]/div/div[2]/div/div[1]/div[2]/span[2]').click()
        time.sleep(10000)















