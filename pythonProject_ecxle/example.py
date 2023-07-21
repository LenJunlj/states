# file_path = r"C:\Users\Administrator\DesktopDownload\example.XML"
# # 打开文件以进行写入
# with open(file_path, "w") as file:
#     # 写入文件内容
#     file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
#     file.write("<DownloadDescriptor>\n")
#     file.write("  <File>example.txt</File>\n")
#     file.write("</DownloadDescriptor>\n")
#
# print("文件创建成功并写入内容！")
import os

import open_excle
from open_excle import write_BOOT

file_path = r'C:\Users\Administrator\Desktop\Download\example.XML'

# 获取文件夹路径
folder_path = os.path.dirname(file_path)

# 如果文件夹不存在，则创建文件夹
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 打开文件以进行写入
with open(file_path, "w") as file:
    # 写入文件内容
    file.write("<?xml version='1.0' encoding='GB18030'?>\n"
               "<VehicleOTAManifest OTAManifestIdentifier='1.x'>\n"
               "	<ModuleOTAManifest>\n"
               "		<OTAManifestFormatVersion>2022-12-08-7.2.0</OTAManifestFormatVersion>\n"
               "		<NumDiagnosticAddrs>1</NumDiagnosticAddrs>\n"
               "			<TargetDiagnosticAddrCurrPNs>		<DiagnosticAddrs>\n")
    file.write("			<TargetDiagnosticAddrCurrPNs>\n"
               "				<DIDName>F180</DIDName>\n"
               "				<DIDString>"open_excle.write_BOOT().re"</DIDString>\n"
               "			</TargetDiagnosticAddrCurrPNs>\n")
print("文件创建成功并写入内容！")