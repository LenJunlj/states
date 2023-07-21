import os

# 定义文件所在的目录路径
directory = r"D:\Work\OTA\C223_delta_package_user-test-keys_source68_to_target59_ANY"

# 使用os.listdir()函数获取目录中的文件和文件夹名称列表
file_names = os.listdir(directory)

# 遍历文件名列表并打印每个文件名
for file_name in file_names:
    file_path = os.path.join(directory, file_name)
    print(file_name)

    # 检查文件是否需要重命名
    if any(ext in file_name for ext in [".mnf", ".smd", ".csv", ".xml", ".vit"]):
        print(1)
    else:
        without_dot = file_name.replace(".", "", 1)
        new_path = os.path.join(directory, without_dot)
        os.rename(file_path, new_path)
        print(f"文件已重命名为: {new_path}")