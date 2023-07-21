import os
import pandas as pd
file_path = r'C:\Users\Administrator\Desktop\Download\DownloadDescriptor.XML'
folder_path = os.path.dirname(file_path)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

def write_excle():
    df = pd.read_excel('delivery_manifest.xlsx', sheet_name='BOOT')
    my_dict = dict(zip(df['Part Number'], df['DLS/PLS']))
    # my_dict2= dict(zip(df['Part ID'], df['DLS/PLS']))
    return my_dict
def write_excle2():
    df = pd.read_excel('delivery_manifest.xlsx', sheet_name='delivery_manifest')
    my_dict2= dict(zip(df['Part Number'], df['DLS/PLS']))
    return my_dict2

with open(file_path, "w") as file:
    file.write("<?xml version='1.0' encoding='GB18030'?>\n"
               "<VehicleDownloadDescriptor DDIdentifier='1.x'>\n"
               "	<ModuleDownloadDescriptor>\n"
               "		<DDVersion>7.3.0</DDVersion>\n"
               "		<CampaignID>SSr7n3bCEe2oCe7uCv96SAcmp</CampaignID>\n"
               "		<DownloadPackage>\n"
               "			<SubPackage>\n"
               "				<TargetDiagnosticAddress>0x84</TargetDiagnosticAddress>\n")
    for key,value in write_excle().items():
        file.write("				<PartNumberURI>https://180.167.150.90:50009/api/v1/dw/NFOTA/PackageDownload/Zhao_Li_R2T2/618/")
        file.write(f"{key}{value}")
        file.write("</PartNumberURI>\n")
    for key,value in write_excle2().items():
        file.write("				<PartNumberURI>https://180.167.150.90:50009/api/v1/dw/NFOTA/PackageDownload/Zhao_Li_R2T2/618/")
        file.write(f"{key}{value}")
        file.write("</PartNumberURI>\n")
    file.write("			</SubPackage>\n"
               "		</DownloadPackage>\n"
               "		<UIMessageList>\n"
               "			<VehicleTypeId>0</VehicleTypeId>\n"
               "			<UpdateTitle>&#x522b;&#x514b;B233_source2_to_target209_ANY&#x5347;&#x7ea7;&#x66f4;&#x65b0;</UpdateTitle>\n"
               "			<ReleaseNotes>&#x522b;&#x514b;B233_source2_to_target209_ANY&#x5347;&#x7ea7;&#x66f4;&#x65b0;&#x5c06;&#x4f1a;&#x4e3a;&#x7528;&#x6237;&#x5e26;&#x6765;&#x5168;&#x65b0;&#x7684;&#x4e92;&#x8054;&#x4f53;&#x9a8c;&#x548c;app&#x793e;&#x533a;&#x3002;</ReleaseNotes>\n"
               "			<UserInstructionToPrepareVehicle>&#x8bf7;&#x6309;&#x7167;&#x5c4f;&#x5e55;&#x63d0;&#x793a;&#x4fe1;&#x606f;&#x8fdb;&#x884c;&#x522b;&#x514b;B233_source2_to_target209_ANY&#x5347;&#x7ea7;&#x66f4;&#x65b0;&#xff01;</UserInstructionToPrepareVehicle>\n"
               "			<SuccessMessage>&#x522b;&#x514b;B233_source2_to_target209_ANY&#x5347;&#x7ea7;&#x66f4;&#x65b0;&#x6210;&#x529f;&#xff01;</SuccessMessage>\n"
               "			<FailureMessage>&#x522b;&#x514b;B233_source2_to_target209_ANY&#x5347;&#x7ea7;&#x66f4;&#x65b0;&#x5931;&#x8d25;&#xff0c;&#x8bf7;&#x8054;&#x7cfb;&#x534f;&#x52a9;&#x7535;&#x8bdd;&#xff1a;xxxxxxxx</FailureMessage>\n"
               "		</UIMessageList>\n"
               "		<UserDownloadInteractionType>HIGH</UserDownloadInteractionType>\n"
               "		<UserUpdateInteractionType>HIGH</UserUpdateInteractionType>\n"
               "		<Size>300</Size>\n"
               "		<NoneNoneDownloadTime>10</NoneNoneDownloadTime>\n"
               "		<NoneNoneDownloadRetriesAllowed>false</NoneNoneDownloadRetriesAllowed>\n"
               "		<Http503Delay>1000</Http503Delay>\n"
               "		<EnableChunk>false</EnableChunk>\n"
               "		<ChunkSize>1</ChunkSize>\n"
               "		<InterChunkDelay>12000</InterChunkDelay>\n"
               "		<ChkBatStaDownload>false</ChkBatStaDownload>\n"
               "		<NetworkConnection>\n"
               "			<NetworkType>CELLULAR</NetworkType>\n"
               "			<NetworkConnectionDelayTime>1</NetworkConnectionDelayTime>\n"
               "			<NetworkConnectionWaitTime>2</NetworkConnectionWaitTime>\n"
               "		</NetworkConnection>\n"
               "	</ModuleDownloadDescriptor>\n"
               "</VehicleDownloadDescriptor>\n")