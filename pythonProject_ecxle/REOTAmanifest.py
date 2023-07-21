
import os
import pandas as pd
file_path = r'C:\Users\Administrator\Desktop\Download\example.XML'

def write_excle():
    df = pd.read_excel('delivery_manifest.xlsx', sheet_name='BOOT')
    my_dict = dict(zip(df['Part Number'], df['DLS/PLS']))
    # my_dict2= dict(zip(df['Part ID'], df['DLS/PLS']))
    return my_dict
def write_excle2():
    df = pd.read_excel('delivery_manifest.xlsx', sheet_name='delivery_manifest')
    my_dict2= dict(zip(df['Part Number'], df['DLS/PLS']))
    return my_dict2
folder_path = os.path.dirname(file_path)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

with open(file_path, "w") as file:
    file.write("<?xml version='1.0' encoding='GB18030'?>\n"
               "<VehicleOTAManifest OTAManifestIdentifier='1.x'>\n"
               "	<ModuleOTAManifest>\n"
               "		<OTAManifestFormatVersion>2022-12-08-7.2.0</OTAManifestFormatVersion>\n"
               "		<NumDiagnosticAddrs>1</NumDiagnosticAddrs>\n"
               "			<TargetDiagnosticAddrCurrPNs>		<DiagnosticAddrs>\n")
    for key,value in write_excle().items():
        file.write("			<TargetDiagnosticAddrCurrPNs>\n"
                   "				<DIDName>F180</DIDName>\n"
                   "				<DIDString>")
        file.write(f"{key}{value}")
        file.write("</DIDString>\n"
                   "			</TargetDiagnosticAddrCurrPNs>\n")
    for key,value in write_excle2().items():
        file.write("			<TargetDiagnosticAddrCurrPNs>\n"
                   "				<DIDName>F181</DIDName>\n"
                   "				<DIDString>")
        file.write(f"{key}{value}")
        file.write("</DIDString>\n"
                   "			</TargetDiagnosticAddrCurrPNs>\n")
print("文件创建成功并写入内容！")