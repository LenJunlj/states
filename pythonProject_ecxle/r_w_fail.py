# # open_file=open( r'C:\Users\Administrator\Desktop\word.txt','w')
# # line="lenjundadha\n"
# # line_c="warning测试，请勿打扰,dajia"
# # open_file.write(line)
# # open_file.write(line_c)
# # open_file.close()
#
# import os
#
# cwd=os.getcwd()
# cwd_a=os.path.abspath('word.txt')
# print(cwd)
# print(cwd_a)
#
# ###检查文件或者目录是否存在
# os.path.exists()
# ###检查他是否有这个目录
# os.path.isdir()
# os.path.isfile()
# os.listdir()
# ###os.path.join 接受一个目录和一个文件名，并把它们合并成一个完整的路径
# os.path.join()
#
# ##遍历指定路径下的所有文件和文件夹
# os.walk()
# ###捕获异常
# try:
#
# except:
# import dbm
# db=dbm.open('captions','c')
# db['cleese.png']='Photo of John Cleese .'
# cd=db['cleese.png']
# print(cd)

import pickle
# t=[1,2,3]
# l=pickle.dumps(t)###读取一个对象，并返回一个字符串表示‘
# print(l)

# e=pickle.loads(l)
# print(e)
# open_file=open( r'C:\Users\Administrator\Desktop\DownloadDescriptor.XML','w')

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

file_name = r'C:\Users\Administrator\Desktop\OTAManifest.XML'  # 你可以替换成你的文件名
read_file(file_name)
