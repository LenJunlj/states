import can
import cantools,time

# 加载 CAN 数据库文件
db = cantools.database.load_file(r'C:\Users\YYU66\Desktop\1-CDX707\02 DBC\CAN_CDX707_MY2023_GAS_HEV_v6d_W1_R1\HS2_CAN_CDX707_MY2023_GAS_HEV_v6d.dbc')

# 初始化 CAN 总线
bus = can.interface.Bus(interface='vector', channel = 1 ,bitrate=500000)

# 创建 CAN 消息并填充数据
message_name = 'RCMStatusMessage2'


message = db.get_message_by_name(message_name)
message_id = message.frame_id
print(hex(message_id))
signal_values = {
}
for signal in message.signals:
    if signal.initial == None:
        signal_values[signal.name] = 0
    else:
        signal_values[signal.name] = signal.initial

signal_values['RstrnImpactEvntStatus'] = 5
print(signal_values)
data = message.encode(signal_values)
print(data)
can_message = can.Message(arbitration_id=message_id, data=data, is_extended_id=False)

# 发送 CAN 消息
while True:
    time.sleep(0.01)
    try:
        bus.send(can_message)
        print(f"Message sent on {bus.channel_info}")
    except can.CanError:
        print("Message NOT sent")

bus.shutdown()