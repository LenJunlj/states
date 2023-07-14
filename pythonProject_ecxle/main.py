# # 这是一个示例 Python 脚本。
#
# # 按 Shift+F10 执行或将其替换为您的代码。
# # 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
#
#
# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
#
#
# # 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
import pandas as pd

# 读取Excel文件
data = pd.read_excel('delivery_manifest.xlsx')

# 获取列名
column_names = data.columns.tolist()
print(column_names)

# 选择指定的一列数据
if 'Part Number' in column_names and 'DLS/PLS' in column_names :
    column_data_PDU = data['Part Number'].tolist()
    column_data_ID=data['DLS/PLS'].tolist()
    # print(column_data_PDU)
    # print(column_data_ID)
else:
    print("Column 'PDU and ID' not found in the DataFrame.")
print(column_data_PDU[0])
column_data=[]
for i in range(len(column_data_ID)):
        first_element1 = column_data_PDU[i]
        first_element2 = column_data_ID[i]
        column_data.append([first_element1,first_element2])
print(column_data)



























