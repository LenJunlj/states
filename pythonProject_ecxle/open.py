# # fin=open(r"C:\Users\Administrator\Desktop\word.txt")
# # fin_read=fin.read()
# # print(fin_read)
#
# fin = open (r"C:\Users\Administrator\Desktop\word.txt")
# for line in fin :
#     word = line . strip ()
# print ( word )
#
# with open(r"C:\Users\Administrator\Desktop\word.txt") as file:
#     # 逐行读取文件内容
#     for line in file:
#         # 去除行尾换行符
#         line = line.rstrip()
#         # 按空格分隔单词
#         words = line.split()
#         # 遍历每个单词
#         for word in words:
#             # 判断单词长度是否超过20个字符
#             if len(word) > 20:
#                 print(word)


##字典 /列表 / 元组
E_dict=dict()
print(E_dict)

E_List=list()
print(E_List)

E_tuple=tuple()
print(E_tuple)

E_eng=dict()
E_eng['one']='you'
print(E_eng)

el={'1':'3','2':'4'}
print(el)
print(len(el))

al=el.values()
pl='3' in al
print(pl)

