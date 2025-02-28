# coding : UTF-8
# Author : zsm
# Created Time : 2024/9/24  14:20
# File Name : ASCII.PY
# Development Tool : PyCharm
# Description : ASCII码转换

import tkinter as tk
from tkinter import messagebox

class CharConversion(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.config(bg="#f0f0f0")  # 设置浅灰背景

    # 创建窗口组件
    def create_widgets(self):
        # 创建提示文本、输入框、确认按钮
        title_label = tk.Label(self, text="ASCII码转换器", font=("Arial", 16, "bold"), fg="#333333", bg="#f0f0f0")
        title_label.pack(pady=10)
        tk.Label(self, text="请输入一个字符以转换成ASCII码", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        self.user_input = tk.Entry(self, font=("Arial", 12))
        self.user_input.pack(pady=5)
        btn_commit = tk.Button(self, text="确认转换", command=self.submit,
                               font=("Arial", 12), bg="#4a90e2", fg="white", relief="groove")
        btn_commit.pack(pady=10)
        # 创建结果标签，显示转换后的ASCII码
        self.result_label = tk.Label(self, text="", font=("Arial", 12, "italic"), bg="#f0f0f0", fg="#333333")
        self.result_label.pack(pady=10)

    def submit(self):
        user_input = self.user_input.get()
        if len(user_input) != 1:
            messagebox.showerror("错误", "请输入一个字符！")
        else:
            ascii_code = ord(user_input)
            self.result_label.config(text=f"ASCII码：{ascii_code}")


if __name__ == "__main__":
    win = tk.Tk()
    win.geometry("400x300")
    win.title("ASCII码转换")
    game_frame = CharConversion(win)
    game_frame.pack(expand=True, fill=tk.BOTH)
    win.mainloop()
