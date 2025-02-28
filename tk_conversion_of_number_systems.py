# coding : UTF-8
# Author : zsm
# Created Time : 2024/9/24  13:38
# File Name : ConversionOfNumberSystems.PY
# Development Tool : PyCharm
# Description : 进制转化

import tkinter as tk
from tkinter import messagebox

class ConversionOfNumberSystems(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_16 = None
        self.label_10 = None
        self.label_2 = None
        self.label_8 = None
        self.master = master
        self.config(bg='#f0f0f0')  # 浅灰背景

    def create_widgets(self):
        # 标题标签
        title_label = tk.Label(self, text="进制转换工具", font=("Arial", 16, "bold"), fg="#333333", bg='#f0f0f0')
        title_label.pack(pady=10)
        # 单选按钮提示标签
        tk.Label(self, text="请选择输入的进制", font=("Arial", 12), bg='#f0f0f0').pack(pady=5)
        # 用于存储进制选择的变量
        self.status = tk.IntVar(value=10)   # 默认选中10进制
        # 单选按钮
        radio2 = tk.Radiobutton(self, text="2进制", variable=self.status, value=2, font=("Arial", 10),
                                bg='#f0f0f0', activebackground='#f0f0f0', selectcolor='#4a90e2')
        radio8 = tk.Radiobutton(self, text="8进制", variable=self.status, value=8, font=("Arial", 10),
                                bg='#f0f0f0', activebackground='#f0f0f0', selectcolor='#4a90e2')
        radio10 = tk.Radiobutton(self, text="10进制", variable=self.status, value=10, font=("Arial", 10),
                                 bg='#f0f0f0', activebackground='#f0f0f0', selectcolor='#4a90e2')
        radio16 = tk.Radiobutton(self, text="16进制", variable=self.status, value=16, font=("Arial", 10),
                                 bg='#f0f0f0', activebackground='#f0f0f0', selectcolor='#4a90e2')
        radio2.pack(pady=2)
        radio8.pack(pady=2)
        radio10.pack(pady=2)
        radio16.pack(pady=2)

        # 用户输入框和转换按钮
        user_input = tk.Entry(self, font=("Arial", 12))
        user_input.pack(pady=10)
        btn_submit = tk.Button(self, text="转换", command=lambda: self.conversion(user_input.get()),
                               bg="#4a90e2", fg="white", font=("Arial", 12), relief="groove")
        btn_submit.pack(pady=5)
        # 转换结果显示
        self.label_2 = tk.Label(self, text="", font=("Arial", 10), bg='#f0f0f0')
        self.label_2.pack(pady=2)
        self.label_8 = tk.Label(self, text="", font=("Arial", 10), bg='#f0f0f0')
        self.label_8.pack(pady=2)
        self.label_10 = tk.Label(self, text="", font=("Arial", 10), bg='#f0f0f0')
        self.label_10.pack(pady=2)
        self.label_16 = tk.Label(self, text="", font=("Arial", 10), bg='#f0f0f0')
        self.label_16.pack(pady=2)

    def conversion(self, user_input):
        # 获取用户选择的进制
        base = self.status.get()
        try:
            # 将用户输入的数字转换为十进制
            num = int(user_input, base)
            # 根据不同进制显示结果
            self.label_2.config(text=f"二进制：{bin(num)}")
            self.label_8.config(text=f"八进制：{oct(num)}")
            self.label_10.config(text=f"十进制：{num}")
            self.label_16.config(text=f"十六进制：{hex(num)}")
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字！")

if __name__ == '__main__':
    win = tk.Tk()
    win.title("进制转换工具")
    win.geometry("400x400")
    game_frame = ConversionOfNumberSystems(win)
    game_frame.pack(expand=True, fill=tk.BOTH)
    win.mainloop()
