# fin=open(r"C:\Users\Administrator\Desktop\word.txt")
# fin_read=fin.read()
# print(fin_read)
#
# fin = open (r"C:\Users\Administrator\Desktop\word.txt")
# for line in fin :
#     word = line . strip ()
# print ( word )
# #
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
#             if len(word) > 15:
#                 print(word)


# ##字典 /列表 / 元组
# E_dict=dict()
# print(E_dict)
#
# E_List=list()
# print(E_List)
#
# E_tuple=tuple()
# print(E_tuple)
#
# E_eng=dict()
# E_eng['one']='you'
# print(E_eng)
#
# el={'1':'3','2':'4'}
# print(el)
# print(len(el))
#
# al=el.values()
# pl='3' in al
# # print(pl)
# # #
# # # print(type(pl))
# # # print(type(al))
# # # print(type(el))
# # # print(type(E_List))
# #
# #
# # hclc=[20,30,40,50,60]
# # for lg in hclc:
# #     if lg!=30:
# #         hclc[2]=80
# #         cd=len(hclc)
# #         print(cd)
# #         print(lg)
# # for hc in range(0,5):
# #     print(hc)
# # hclc.append('90')
# # print(hclc)
# # t=0
# # hc=hclc.pop(2)
# # print(hc)
# # hclc.remove('20')
# # print(hclc)
#
# x='ashlKHFS'
# y=list(x)
# print(y)


t=[1,2,3]
# def cumsum(t):
#     su=0
#     t.sum()
# #     for lp in t:
# #         su+=lp
# def cumsum(list):
#     cumulative_sum = []
#     current_sum = 0
#     for num in list:
#         current_sum += num
#         cumulative_sum.append(current_sum)
#     return cumulative_sum
#     print(cumulative_sum)
# cumsum(t)
# def middle(lst):
# #     return lst[1:-1]
# # my_list = [1, 2, 3, 4, 5]
# # result = middle(my_list)
# # print(result)
#
# import string
#
# def process_line(line):
#     line = line.strip()  # 去除行首和行尾的空格
#     line = line.translate(str.maketrans('', '', string.punctuation))  # 删除标点符号
#     line = line.lower()  # 转换为小写字母
#     words = line.split()  # 以空格为分隔符拆分为单词列表
#     return words
#
# def process_file(filename):
#     with open(filename, 'r') as file:
#         lines = file.readlines()
#         for line in lines:
#             words = process_line(line)
#             print(words)


# # 使用方式
# filename = r'C:\Users\Administrator\Desktop\word.txt'  # 你可以替换成你的文件名
# process_file(filename)

# import requests
#
# def download_book(url):
#     response = requests.get(url)
#     return response.text
#
# def process_book(text):
#     lines = text.split('\n')
#     # 在这里添加你对书籍文本的处理逻辑
#     # 例如，你可以统计单词频率、分析章节结构等
#
# # 使用方式
# book_url = 'https://www.gutenberg.org/files/1342/1342-0.txt'
# book_text = download_book(book_url)
# process_book(book_text)



import string

#读取文件
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
#
# file_name = r'C:\Users\Administrator\Desktop\word.txt'  # 你可以替换成你的文件名
# read_file(file_name)

####随机数
#####random 模块提供了生成伪随机数
import random
for i in range(2):
    x=random.random()
    print(x)

##函数 randint 接受参数 low 和 high ，返回一个 low 和 high 之间的整数

import random
x=random.randint(5,10)
print(x)
x=random.randint(5,10)
print(x)

