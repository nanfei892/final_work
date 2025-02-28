# coding : UTF-8
# Author : zsm
# Created Time : 2024/10/8  16:30
# File Name : 班级点名.PY
# Development Tool : PyCharm
# Description : 随机点名

import pandas as pd
import random
import pyttsx3
import tkinter as tk

class RandomGroup(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        df = pd.read_excel(r".\static\24-2.xls")
        df_names = df.iloc[0:, 2]
        self.names = [i for i in df_names]

    def create_widgets(self):
        title_label = tk.Label(self, text="随机分组工具", font=("Arial", 16, "bold"), fg="#333333", bg='#f0f0f0')
        title_label.pack(pady=10)
        tk.Label(self, text = "请输入每组的人数(默认5人一组)", font=("Arial", 12), bg='#f0f0f0').pack()
        user_input_num = tk.Entry(self, width=10, font=("Arial", 12))
        user_input_num.pack(pady=5)
        btn_submit = tk.Button(self, text="确认分组",
                               command=lambda: self.group(int(user_input_num.get()) if user_input_num.get() else 5),
                               bg="#4a90e2", fg="white", font=("Arial", 12), relief="groove")
        btn_submit.pack(pady=10)
        # 定义选择框，用来展示结果
        self.result_list_box = tk.Listbox(self, font=("Arial", 10), width=40, height=10, bg="white",selectbackground="#4a90e2")
        self.result_list_box.pack(pady=10)
    # 分组
    def group(self, person_num = 5):
        random.shuffle(self.names)
        team = []

        for i in range(len(self.names) // person_num):
            team.insert(i, self.names[i * person_num:i * person_num + person_num:])
            print(team)
        if len(self.names) % person_num != 0 or person_num * len(team) < len(self.names):
            team.insert(len(team), self.names[person_num * len(team):])
        # 清空并更新列表框中的分组结果
        self.result_list_box.delete(0, tk.END)
        for idx, grp in enumerate(team):
            self.result_list_box.insert(tk.END, f"第{idx + 1}组: " + ", ".join(grp))

if __name__ == '__main__':
    win = tk.Tk()
    win.title("随机分组")
    win.geometry("500x400")
    game_frame = RandomGroup(win)
    game_frame.pack(expand=True, fill=tk.BOTH)
    win.mainloop()



