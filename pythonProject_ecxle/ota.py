import string
import pandas as pd
def read_file(file_name):
    with open(file_name,'r') as file:
        lists=file.readlines()  ####列表
        for line in lists:
            change_list(line)
            print(line)
def change_list(line):
    line.strip()
    line.translate(str.maketrans('', '', string.punctuation))
    line.lower()
    line.split()
    return line
def read_excle():
    # 读取Excel文件
    data = pd.read_excel('delivery_manifest.xlsx')

    # 获取列名
    column_names = data.columns.tolist()
    print(column_names)
    if 'Part Number' in column_names and 'DLS/PLS' in column_names :
        column_data_PDU = data['Part Number'].tolist()
        column_data_ID=data['DLS/PLS'].tolist()
        print(column_data_PDU)
        print(column_data_ID)
    else:
        print("Column 'PDU and ID' not found in the DataFrame.")

file_name = r'C:\Users\Administrator\Desktop\OTAManifest.XML'  # 你可以替换成你的文件名
read_file(file_name)
read_excle()
