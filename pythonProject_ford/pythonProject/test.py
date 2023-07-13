import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class open_Fenix:
    def log_in(web,userId,environment,rolloutdescription,vehicleset,vehicleVIN,softwareset,Install_Strategy,Inhibit_Required,json,SWStype,jsonpath,jsonpath1,hours,level):
        driver=webdriver.Chrome(web)
        # 打开Fenix网页
        driver_web=driver.get('https://fenix2-fire-ui-prd.apps.pd01.cneast.cf.ford.com.cn/fire/fenix-dashboard/')
        driver.implicitly_wait(20)
        # 最大化窗口
        driver.maximize_window()
        driver.implicitly_wait(20)
        # 输入账户名
        Account=driver.find_element(By.XPATH,'//*[@id="i0116"]').send_keys(userId)
        driver.implicitly_wait(10)
        # 点击下一步
        Next =driver.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
        driver.implicitly_wait(10)
        # 点击Active_Directory
        driver.Active_Directory=driver.find_element(By.XPATH,'//*[@id="bySelection"]/div[3]/div/span').click()
        driver.implicitly_wait(10)    # 智能等待10秒钟

        # 外网账户信息输入
        # driver.find_element(By.XPATH,'//*[@id="passwordInput"]').send_keys('LJ19990812xxyy\n')
        # driver.implicitly_wait(20)
        # driver.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()

        driver.implicitly_wait(20)
        # driver_production = driver.find_element(By.XPATH,'/html/body/app-root/div/main/div[4]/app-current-tmc-environment/div/div/div[2]/div[1]/ota-primary-button/p-button/button/span').click()
        # 判断整车环境是Sandbox还是Production
        if(environment=="production"):
            driver_production=driver.find_elements(By.XPATH,'//*[@id="undefined"]/button/span')[0].click()
        else:
            driver_Sandbox=driver.find_elements(By.XPATH ,'//*[@id="undefined"]/button/span')[1].click()
        driver.implicitly_wait(20)
        # 单击Deployment菜单
        driver_Deloyment=driver.find_element(By.XPATH,'//*[@id="app-header"]/ota-navigation/div/ota-wide/div/div[2]/div[1]/p-megamenu/div/ul/li[2]/a').click()
        driver.implicitly_wait(20)
        # 选择SoftwareSetRollout任务
        driver_Create_Rollout=driver.find_element(By.XPATH,'//*[@id="app-header"]/ota-navigation/div/ota-wide/div/div[2]/div[1]/p-megamenu/div/ul/li[2]/div/div/div[1]/ul[2]/li[2]/a/span').click()
        driver.implicitly_wait(20)
        # 创建RolloutID的命名
        driver_Rollout_Description=driver.find_element(By.XPATH,'/html/body/app-root/div/main/div[4]/app-create-rollout/div/div[6]/textarea').send_keys(rolloutdescription)
        driver.implicitly_wait(20)
        # 选择目标车辆设置
        driver_target=driver.find_element(By.XPATH,'/html/body/app-root/div/main/div[4]/app-create-rollout/div/div[7]/app-radio-button-input/div/div/p-radiobutton').click()
        driver.implicitly_wait(20)
        # 选择车辆分组
        driver_Vehicle_Set=driver.find_element(By.XPATH,'/html/body/app-root/div/main/div[4]/app-create-rollout/div/div[8]/div/p-dropdown/div/span').click()
        driver.implicitly_wait(20)
        # 在车辆分组的下拉框输入“自定义的组群的名称”
        driver_Vehicle_model=driver.find_element(By.XPATH,'/html/body/app-root/div/main/div[4]/app-create-rollout/div/div[8]/div/p-dropdown/div/div[3]/div[1]/div/input').send_keys(vehicleset)
        driver.implicitly_wait(20)
        # 点击VehicleSet的联想框
        driver_target_Way=driver.find_element(By.XPATH,'/html/body/app-root/div/main/div[4]/app-create-rollout/div/div[8]/div/p-dropdown/div/div[3]/div[2]/ul/p-dropdownitem/li/span').click()
        driver.implicitly_wait(20)
        # 选择车辆集合中的VIN
        driver_target_vin=driver.find_element(By.XPATH,'/html/body/app-root/div/main/div[4]/app-create-rollout/div/div[9]/app-radio-button-input/div/div[2]/p-radiobutton/div/div[2]').click()
        driver.implicitly_wait(20)
        # 点击选择车辆VIN码的下拉框
        driver_vin_start=driver.find_element(By.XPATH,'/html/body/app-root/div/main/div[4]/app-create-rollout/div/div[10]/div/p-multiselect/div/div[2]/div').click()
        time.sleep(2)
        driver.implicitly_wait(20)
        # 在车辆VIN码下拉框内输入“车辆VIN”
        driver_VIN=driver.find_element(By.XPATH,'/html/body/app-root/div/main/div[4]/app-create-rollout/div/div[10]/div/p-multiselect/div/div[4]/div[1]/div[2]/input').send_keys(vehicleVIN)
        driver.implicitly_wait(20)
        time.sleep(2)
        # 针对于联想出的VIN码进行勾选
        driver_Precise_selection_VIN=driver.find_element(By.XPATH,'/html/body/app-root/div/main/div[4]/app-create-rollout/div/div[10]/div/p-multiselect/div/div[4]/div[2]/ul/cdk-virtual-scroll-viewport/div[1]/p-multiselectitem/li/div/div').click()
        driver.implicitly_wait(20)
        # 点击空白处，将车辆VIN码节选上
        # driver.point_back=driver.find_element(By.XPATH,'/html/body/app-root/div/main/div[4]/app-create-rollout/div/div[10]/div/p-multiselect/div/div[2]/div').click()
        # driver.implicitly_wait(20)

        # 选择Software_Set
        driver.software=driver.find_element(By.XPATH,'/html/body/app-root/div/main/div[4]/app-create-rollout/div/div[11]/div/p-autocomplete/span/input').send_keys(softwareset)
        driver.implicitly_wait(20)

        # 模糊搜索相应的软件包
        driver_software_choose=driver.find_element(By.XPATH,'//*[@id="pr_id_1_list"]/li[1]/span').click()
        driver.implicitly_wait(20)

        # 选择设备类型
        driver_Device_Type=driver.find_element(By.XPATH,'/html/body/app-root/div/main/div[4]/app-create-rollout/div/div[12]/app-radio-button-input/div/div/p-radiobutton/div/div[2]').click()
        driver.implicitly_wait(20)

        # 选择BusinessRules为自定义
        driver_Business_Rules=driver.find_element(By.XPATH,'/html/body/app-root/div/main/div[4]/app-create-rollout/div/div[14]/app-radio-button-input/div/div[2]/p-radiobutton/div/div[2]').click()
        driver.implicitly_wait(20)
        # 选择需要添加DirectConfiguration
        driver_Include_direct=driver.find_element(By.XPATH,'/html/body/app-root/div/main/div[4]/app-create-rollout/div/div[15]/app-radio-button-input/div/div[2]/p-radiobutton/div/div[2]').click()
        driver.implicitly_wait(100)
        # 选择的DirectConfiguration为Enable类型
        driver_Enable_include=driver.find_element(By.XPATH,'/html/body/app-root/div/main/div[4]/app-create-rollout/div/div[16]/app-radio-button-input/div/div[1]/p-radiobutton/div/div[2]').click()
        driver.implicitly_wait(100)
        # 判断安装策略是根据空间还是连通性
        if(Install_Strategy=='Space'):
            driver_Install_Strategy=driver.find_element(By.XPATH,'//*[@id="customRules"]/div[2]/app-radio-button-input/div/div[2]/p-radiobutton/label').click()
        else:
            driver_Install_Strategy=driver.find_element(By.XPATH,'//*[@id="customRules"]/div[2]/app-radio-button-input/div/div[1]/p-radiobutton/label').click()
        driver.implicitly_wait(100)
        # 软件包升级时间的计算
        driver_UpdateTimeInSeconds=driver.find_element(By.XPATH,'//*[@id="customRules"]/div[3]/app-radio-button-input/div/div[1]/p-radiobutton/label').click()
        driver.implicitly_wait(100)
        # 判断是否选择进入Inhibit条件(No None& Yes permanentInhibit)
        if(Inhibit_Required=="Y"):
            driver_Inhibit_required = driver.find_element(By.XPATH,'//*[@id="customRules"]/div[4]/app-group-manager/div/div[1]/app-group/div/div/div[1]/div[1]/app-radio-button-input/div/div[1]/p-radiobutton/div/div[2]').click()
            driver.implicitly_wait(20)

            driver_Response = driver.find_element(By.XPATH,'//*[@id="customRules"]/div[4]/app-group-manager/div/div[1]/app-group/div/div/div[1]/div[2]/div/p-dropdown/div/span').click()
            driver.implicitly_wait(20)

            driver_Permanent = driver.find_element(By.XPATH,'//*[@id="customRules"]/div[4]/app-group-manager/div/div[1]/app-group/div/div/div[1]/div[2]/div/p-dropdown/div/div[3]/div[2]/ul/p-dropdownitem[1]/li/span').click()
            driver.implicitly_wait(20)

            driver_Node_ecu = driver.find_element(By.XPATH, '//*[@id="p-accordiontab-0"]').click()
            driver.implicitly_wait(100)
        else:
            driver_Inhibit_required = driver.find_element(By.XPATH,'//*[@id="customRules"]/div[4]/app-group-manager/div/div[1]/app-group/div/div/div[1]/div[1]/app-radio-button-input/div/div[2]/p-radiobutton/div/div[2]/span').click()
            driver.implicitly_wait(20)

            driver_Response = driver.find_element(By.XPATH,'//*[@id="customRules"]/div[4]/app-group-manager/div/div[1]/app-group/div/div/div[1]/div[2]/div/p-dropdown/div/span').click()
            driver.implicitly_wait(20)

            driver_None = driver.find_element(By.XPATH,'//*[@id="customRules"]/div[4]/app-group-manager/div/div[1]/app-group/div/div/div[1]/div[2]/div/p-dropdown/div/div[3]/div[2]/ul/p-dropdownitem[4]/li/span').click()
            driver.implicitly_wait(20)

            driver_Node_ecu = driver.find_element(By.XPATH,'//*[@id="p-accordiontab-0"]').click()
            driver.implicitly_wait(100)

        # 判断是否改写DC(单件的DC)
        if(json=="yes"):
            time.sleep(2)
            driver_Choose_file=driver.find_element(By.XPATH,'//*[@id="p-accordiontab-0-content"]/div/app-group-node/div/div/div[1]/div[2]/div/input').send_keys(jsonpath)

            driver.implicitly_wait(20)

            # 判断是否是两个件改DC
            if(SWStype =='两个件同时改DC'):
                # 两个件同时分成两个Group；先选择第2页的sheet，然后选择Y，PermanentInhibit，因为第一页的sheet在之前的程序块中已经写好了；
               try:
                   driver_Page2 =driver.find_element(By.XPATH,'//*[@id="customRules"]/div[4]/app-group-manager/div/div[2]/div/p-paginator/div/span/button[2]').click()

                   driver_Inhibit_required1 =driver.find_element(By.XPATH,'//*[@id="customRules"]/div[4]/app-group-manager/div/div[1]/app-group/div/div/div[1]/div[1]/app-radio-button-input/div/div[1]/p-radiobutton/div/div[2]').click()

                   driver_Response1 =driver.find_element(By.XPATH,'//*[@id="customRules"]/div[4]/app-group-manager/div/div[1]/app-group/div/div/div[1]/div[2]/div/p-dropdown/div/span').click()

                   driver_Permanent1 =driver.find_element(By.XPATH,'//*[@id="customRules"]/div[4]/app-group-manager/div/div[1]/app-group/div/div/div[1]/div[2]/div/p-dropdown/div/div[3]/div[2]/ul/p-dropdownitem[1]/li/span').click()

                   driver_Node_ecu1 =driver.find_element(By.XPATH,'//*[@id="p-accordiontab-1"]').click()

                   driver_Choose_file1 = driver.find_element(By.XPATH,'//*[@id="p-accordiontab-1-content"]/div/app-group-node/div/div/div[1]/div[2]/div/input').send_keys(jsonpath1)
                # 将两个件打包成同一个Group时，因为第一个sheet里面的ECU的改DC部分已经写好
               except:
                   driver_Node_ecu1 =driver.find_element(By.XPATH,'//*[@id="p-accordiontab-1"]').click()

                   driver_Choose_file1 =driver.find_element(By.XPATH,'//*[@id="p-accordiontab-1-content"]/div/app-group-node/div/div/div[1]/div[2]/div/input').send_keys(jsonpath1)
            else:
                pass
        else:
            pass
        # 超时时间
        driver_Hours=driver.find_element(By.XPATH,'//*[@id="customRules"]/div[5]/div[1]/textarea').send_keys(hours)
        driver.implicitly_wait(20)
        # 用户等级:(1,2,3,4,5)
        driver_OTA_Level=driver.find_element(By.XPATH,'//*[@id="customRules"]/div[5]/div[2]/div/textarea').send_keys(level)
        driver.implicitly_wait(20)

        try:   # 判断用户level等级为1时，默认
            driver_VIL = driver.find_element(By.XPATH, '//*[@id="submit-button"]/button/span').click()
            time.sleep(5)
        except:   # 判断用户level等级为2或3时
            driver_Additional_User_Consent=driver.find_element(By.XPATH,'//*[@id="customRules"]/div[5]/div[3]/textarea').send_keys('https://mmota.p0.tmc79.cn/1/bytestream/AdditionalConsentTextFile_V3')
            driver_VIL = driver.find_element(By.XPATH, '//*[@id="submit-button"]/button/span').click()
        time.sleep(5)
        driver.quit()




