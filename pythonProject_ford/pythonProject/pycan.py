import can,time
import cantools

def crash():
    # 创建Vector接口对象
    bus = can.interface.Bus(interface = 'vector', channel= 1, bitrate = 500000)

    # 读取DBC文件
    dbc_file = r'C:\Users\YYU66\Desktop\1-CDX707\02 DBC\CAN_CDX707_MY2023_GAS_HEV_v6d_W1_R1\HS2_CAN_CDX707_MY2023_GAS_HEV_v6d.dbc'

    database = cantools.database.load_file(dbc_file)

    # 获取要发送的消息定义
    message_name = 'RCMStatusMessage2' # 要发送的消息的名称
    message = database.get_message_by_name(message_name)

    # 构建信号值字典
    signal_values = {
    # 'Veh_V_ActlEng': 20 # 将信号名称映射到相应的物理值
    }
    for signal in message.signals:
        if signal.initial == None:
            signal_values[signal.name] = 0
        else:
            signal_values[signal.name] = signal.initial

    signal_values['RstrnImpactEvntStatus'] = 5

    print(signal_values)
    # 构建CAN消息
    message_data = message.encode(signal_values)
    can_id = message.frame_id
    is_fd = False # 是否为FD CAN消息
    is_extended_id = False # 是否使用扩展ID
    can_message = can.Message(arbitration_id=can_id, data=message_data, is_fd=is_fd, is_extended_id=is_extended_id)

    # 发送CAN消息
    # while True:
    bus.send(can_message)

    # 关闭总线
    bus.shutdown()

