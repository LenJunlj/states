# #
# # import pandas as pd
# #
# # # 读取Excel文件
# # data = pd.read_excel('delivery_manifest.xlsx')
# #
# # # 获取列名
# # column_names = data.columns.tolist()
# # print(column_names)
# #
# # # 选择指定的一列数据
# # if 'Part Number' in column_names and 'DLS/PLS' in column_names :
# #     column_data_PDU = data['Part Number'].tolist()
# #     column_data_ID=data['DLS/PLS'].tolist()
# #     # print(column_data_PDU)
# #     # print(column_data_ID)
# # else:
# #     print("Column 'PDU and ID' not found in the DataFrame.")
# # print(column_data_PDU[0])
# # column_data=[]
# # for i in range(len(column_data_ID)):
# #         first_element1 = column_data_PDU[i]
# #         first_element2 = column_data_ID[i]
# #         column_data.append([first_element1,first_element2])
# # print(column_data)
#
#
#
# import pandas as pd
#
# # 读取 Excel 文件，假设数据在 Sheet1 中的 A 列
# df = pd.read_excel('delivery_manifest.xlsx', sheet_name='delivery_manifest')
#
# # 获取 A 列数据并转换为元组
# column_data = tuple(df['Part Number'])
#
# print(column_data)


import pandas as pd

# 读取 Excel 文件，假设数据在 Sheet1 中的 A 列
df = pd.read_excel('delivery_manifest.xlsx', sheet_name='delivery_manifest')

# 获取 A 列数据并转换为字典
column_data = df['Part Number'].to_dict()

print(column_data)
#



















