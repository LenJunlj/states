import pandas as pd

excel_file = r'C:\Users\Administrator\Desktop\git\pythonProject_ecxle\delivery_manifest.xlsx'

# 读取Excel表格数据
df = pd.read_excel(excel_file)

# 获取指定列的数据
keys = df['Part ID'].tolist()
values = df['Part Number'].tolist()
data_dict = dict(zip(keys, values))
# 将键值对存储到字典中
def write_BOOT():
    if " VIP_BOOT" in data_dict:
        selected_data = data_dict["VIP_BOOT"]
        return selected_data













# 打印字典内容
for key, value in data_dict.items():
    print(f"Key: {key}, Value: {value}")
