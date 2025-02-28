# coding : UTF-8
# Author : zsm
# Created Time : 2024/9/12  21:27
# File Name : guessNumber.PY
# Development Tool : PyCharm
# Description : 猜数字游戏

import random
import tkinter as tk


class GuessNumber(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.target_number = None
        self.master = master
    # 创建界面组件
    def create_widgets(self):
        # 提示文本
        label_title = tk.Label(self, text="猜数字游戏", font=("Arial", 16, "bold"), fg="#333333", bg='#f0f0f0')
        label_title.pack(pady=10)
        # 创建用户输入一个随机数的范围
        tk.Label(self, text = "请输入整数范围！默认为：1~100",  font=("Arial", 12), bg='#f0f0f0').pack(pady=5)
        user_start = tk.Entry(self, width=10, font=("Arial", 12))
        user_start.pack(pady=5)
        user_end = tk.Entry(self, width=10, font=("Arial", 12))
        user_end.pack(pady=5)
        btn_integer_range = tk.Button(self, text="确认范围", command=lambda: self.generate_integer(int(user_start.get()), int(user_end.get())), bg="#4a90e2", fg="white", font=("Arial", 12), relief="groove")
        btn_integer_range.pack(pady=10)
        # 创建输入框组件，供用户输入
        tk.Label(self, text = "请输入你的猜测！", font=("Arial", 12), bg='#f0f0f0').pack(pady=5)
        user_input = tk.Entry(self, width=10, font=("Arial", 12))
        user_input.pack(pady=5)
        btn_user_input = tk.Button(self, text = "确认", command = lambda: self.play(user_input.get()), bg="#4a90e2", fg="white", font=("Arial", 12), relief="groove")
        btn_user_input.pack(pady=10)
        # 显示结果的标签
        self.result_label = tk.Label(self, text="", font=("Arial", 12, "italic"), fg="#333333", bg='#f0f0f0')
        self.result_label.pack(pady=10)
        btn_result = tk.Button(self, text="猜不出来？点我公布答案！", command=self.result_answer, bg="#e94e77", fg="white", font=("Arial", 12), relief="groove")
        btn_result.pack(pady=10)
    # 用于生成随机整数
    def generate_integer(self, user_start = 1, user_end = 100):
        self.target_number = random.randint(int(user_start), int(user_end))
        self.result_label.config(text = f"我已经生成了{user_start}到{user_end}之间的整数")

    # 处理用户的猜测逻辑
    def play(self, user_input):
        if self.target_number is None:
            self.result_label.config(text = "请先生成数字在猜测！")
            return
        guess = int(user_input)
        if guess == self.target_number:
            self.result_label.config(text = f"猜对啦 答案是：{self.target_number}")
        elif guess > self.target_number:
            self.result_label.config(text = "猜大了！再试试吧")
        else:
            self.result_label.config(text = "猜小了！再试试吧")

    # 公布答案
    def result_answer(self):
        if self.target_number is not None:
            self.result_label.config(text=f"答案是：{self.target_number}")
        else:
            self.result_label.config(text="还未生成数字！")

# 主程序入口
if __name__ == "__main__":
    win = tk.Tk()
    win.title("猜数字游戏")
    win.geometry("400x400")
    # 创建游戏框架， 传入主窗口作为父窗口
    game_frame = GuessNumber(win)
    # 将框架添加到主窗口中，填满可用空间
    game_frame.pack(expand=True, fill=tk.BOTH)
    win.mainloop()

