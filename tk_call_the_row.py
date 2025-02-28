# coding : UTF-8
# Author : zsm
# Created Time : 2024/10/8  16:30
# File Name : 班级点名.PY
# Development Tool : PyCharm
# Description : 随机点名

import pandas as pd
import random
import tkinter as tk
from tkinter import messagebox


class CallTheRow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.config(bg="#f0f0f0")  # 设置浅灰色背景
        df = pd.read_excel(r"./static/24-2.xls")
        df_names = df.iloc[:, 2]
        self.names = [name for name in df_names if pd.notna(name)]

    def create_widgets(self):
        # 标题
        title_label = tk.Label(self, text="随机点名", font=("Arial", 16, "bold"), fg="#333333", bg="#f0f0f0")
        title_label.pack(pady=10)
        # 人数选择提示
        tk.Label(self, text="请输入要点名的人数 (默认为1人)", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        # 输入框和确认按钮
        self.user_input = tk.Entry(self, font=("Arial", 12))
        self.user_input.pack(pady=5)
        btn_num = tk.Button(self, text="确认", command=self.submit,
                            font=("Arial", 12), bg="#4a90e2", fg="white", relief="groove")
        btn_num.pack(pady=10)
        # 显示点名结果
        self.result_label = tk.Label(self, text="", font=("Arial", 12, "italic"), bg="#f0f0f0", fg="#333333")
        self.result_label.pack(pady=10)

    def submit(self):
        # 获取输入的点名人数
        try:
            number = int(self.user_input.get()) if self.user_input.get() else 1
            if number <= 0:
                raise ValueError("人数必须大于0")
            elif number > len(self.names):
                messagebox.showwarning("警告", f"最多只能点 {len(self.names)} 人")
                return
            # 随机打乱并选出指定数量的名字
            random.shuffle(self.names)
            selected_names = ', '.join(self.names[:number])
            self.result_label.config(text=f"点到的同学: {selected_names}")
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字！")
            self.user_input.delete(0, tk.END)


if __name__ == '__main__':
    win = tk.Tk()
    win.title("随机点名")
    win.geometry("400x300")
    game_frame = CallTheRow(win)
    game_frame.pack(expand=True, fill=tk.BOTH)
    win.mainloop()
