
import tkinter as tk
from test02 import Open_Edge

# 定义窗口
root=tk.Tk()
# print(type(root))
root.title('OTA')
root.geometry('800x600')

# 定义标签位置
Label_1 = tk.Label(root)
Label_1[ 'justify' ] = 'left'
Label_1[ 'text' ] = 'UserName:'
Label_1.place(x=5,y=10,height=20)

# 定义文本框内容
Text_1 = tk.Entry(root)
Text_1.insert(0,'apptest33') # 文本框的起始位置插入默认值
Text_1.place(x=140,y=10,height=20,width=200)

Label_2 = tk.Label(root)
Label_2[ 'justify' ] = 'left'
Label_2[ 'text' ] = 'PassWord:'
Label_2.place(x=5,y=40,height=20)

Text_2 = tk.Entry(root)
Text_2.insert(0,'Pass1234')
Text_2.place(x=140,y=40,height=20,width=200)

Label_3 = tk.Label(root)
Label_3[ 'justify' ] = 'left'
Label_3[ 'text' ] = 'ECU_Name:'
Label_3.place(x=5,y=70,height=20)

Text_3 = tk.Entry(root)
Text_3.insert(0,'VCU')
Text_3.place(x=140,y=70,height=20,width=200)

Label_4 = tk.Label(root)
Label_4[ 'justify' ] = 'left'
Label_4[ 'text' ] = 'Supplier_CODE:'
Label_4.place(x=5,y=100,height=20)

Text_4 = tk.Entry(root)
Text_4.insert(0,'ISSECCO1')
Text_4.place(x=140,y=100,height=20,width=200)

Label_5 = tk.Label(root)
Label_5[ 'justify' ] = 'left'
Label_5[ 'text' ] = 'N:'
Label_5.place(x=5,y=130,height=20)

Text_5 = tk.Entry(root)
Text_5.insert(0,'5')
Text_5.place(x=140,y=130,height=20,width=200)

Label_6 = tk.Label(root)
Label_6[ 'justify' ] = 'left'
Label_6[ 'text' ] = 'Original_Version:'
Label_6.place(x=5,y=160,height=20)

Text_6 = tk.Entry(root)
Text_6.insert(0,'233')
Text_6.place(x=140,y=160,height=20,width=200)

Label_7 = tk.Label(root)
Label_7[ 'justify' ] = 'left'
Label_7[ 'text' ] = 'Target_Version:'
Label_7.place(x=5,y=190,height=20)

Text_7 = tk.Entry(root)
Text_7.insert(0,'247')
# Text_7[ 'text' ] = ''
Text_7.place(x=140,y=190,height=20,width=200)

Label_8 = tk.Label(root)
Label_8[ 'justify' ] = 'left'
Label_8[ 'text' ] = 'VIN:'
Label_8.place(x=5,y=220,height=20)

Text_8 = tk.Entry(root)
Text_8.insert(0,'VIN707')
Text_8.place(x=140,y=220,height=20,width=200)

def start():   # 获取开始按钮相关联的文本框的内容
    edge = Open_Edge(Text_1.get(),Text_2.get(),Text_3.get(),Text_4.get(),Text_5.get(),Text_6.get(),Text_7.get(),Text_8.get())
    print(Text_1.get())
    edge.log_in()
    edge.addECUInfo()
    edge.Project_Config()
    edge.NewECU_Config()
    edge.Campaign_Management()

# 定义开始按钮za./
Start_button = tk.Button(root)
Start_button['text'] = 'Start'
Start_button['command'] = start
Start_button.place(x=150,y=500)

# 运行主循环
root.mainloop()
