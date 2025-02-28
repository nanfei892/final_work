# coding : UTF-8
# Author : zsm
# Created Time : 2024/9/12  21:07
# File Name : rock_paper_scissors.PY
# Development Tool : PyCharm
# Description : 剪刀石头布游戏

import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissorsGame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f0f8ff")  # 设置背景色
        self.master = master
        self.create_widgets()
    # 创建界面组件
    def create_widgets(self):
        # 标签
        title_label = tk.Label(self, text="剪刀石头布游戏", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#4682b4")
        title_label.pack(pady=10)  # 上下填充空间
        # 按钮框架
        button_frame = tk.Frame(self, bg="#f0f8ff")
        button_frame.pack(pady=10)
        # 创建按钮并设置风格
        button_rock = tk.Button(button_frame, text="石头", font=("Helvetica", 12), bg="#87ceeb", fg="white", width=10,
                                command=lambda: self.play("石头"))
        button_paper = tk.Button(button_frame, text="布", font=("Helvetica", 12), bg="#87ceeb", fg="white", width=10,
                                 command=lambda: self.play("布"))
        button_scissors = tk.Button(button_frame, text="剪刀", font=("Helvetica", 12), bg="#87ceeb", fg="white",
                                    width=10, command=lambda: self.play("剪刀"))
        # 布局按钮
        button_rock.grid(row=0, column=0, padx=10, pady=5)
        button_paper.grid(row=0, column=1, padx=10, pady=5)
        button_scissors.grid(row=0, column=2, padx=10, pady=5)
        # 结果标签
        self.result_label = tk.Label(self, text="", font=("Helvetica", 12), bg="#f0f8ff", fg="#333333")
        self.result_label.pack(pady=15)

    # 用户选择后调用的游戏逻辑
    def play(self, user_selection):
        computer_selection = self.get_computer_selection()
        result = self.determine_winner(user_selection, computer_selection)  # 调用判断胜负函数
        # 更新结果文本标签，显示用户和计算机的选择及结果
        self.result_label.config(text=f"你选择了：{user_selection} \n电脑选择了：{computer_selection} \n结果：{result}")

    # 定义电脑随机选择的函数
    def get_computer_selection(self):
        selections = ["石头", "剪刀", "布"]
        return random.choice(selections)

    # 判断胜负
    def determine_winner(self, user_selection, computer_selection):
        if user_selection == computer_selection:
            return "平局"
        if (user_selection == "石头" and computer_selection == "剪刀") or \
                (user_selection == "剪刀" and computer_selection == "布") or \
                (user_selection == "布" and computer_selection == "石头"):
            return "你赢了！"
        else:
            return "你输了！"

# 主程序入口
if __name__ == "__main__":
    win = tk.Tk()
    win.title("剪刀石头布游戏")
    win.geometry("400x300")
    win.configure(bg="#f0f8ff")
    # 创建游戏框架，传入主窗口作为父窗口
    game_frame = RockPaperScissorsGame(win)
    game_frame.pack(expand=True, fill=tk.BOTH)
    win.mainloop()
