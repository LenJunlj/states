import tkinter as tk
from tkinter import ttk
from canoe_open import canalyzer

def get_selected_item():
    item = combo.get()
    if item:
        selected_label.config(text="你选择了：" + item)

# 创建主窗口
root = tk.Tk()
root.title("Combobox Demo")

# 创建Combobox小部件
combo = ttk.Combobox(root)
combo['values'] = ('选项1', '选项2', '选项3', '选项4')
combo.pack(pady=10)

# 创建按钮
button = tk.Button(root, text="获取选中项", command=get_selected_item())
button.pack(pady=5)

# 创建标签用于显示选择的项
selected_label = tk.Label(root, text="")
selected_label.pack(pady=10)

# 运行主循环
root.mainloop()
