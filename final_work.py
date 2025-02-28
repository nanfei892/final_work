# coding : UTF-8
# Author : zsm
# Created Time : 2024/11/3  11:12
# File Name : final_work.PY
# Development Tool : PyCharm
# Description :

import tkinter as tk
from tkinter import messagebox

from rps_tk import RockPaperScissorsGame
from tk_ascll import CharConversion
from tk_conversion_of_number_systems import ConversionOfNumberSystems
from tk_guess_number import GuessNumber
from tk_call_the_row import CallTheRow
from tk_guess_word import GuessWord
from tk_random_group import RandomGroup
win = tk.Tk()
win.title(" Python - 多功能应用")
win.geometry("800x600")
win.configure(bg="#f5f5f5")
# 假设用户数据库
users = {
    'zsm' : 'zsm123',
    'admin' : 'admin123',
    '1' : '1'
}

# 添加标题标签
title_label = tk.Label(win, text="欢迎登录Python多功能应用", font=("Helvetica", 20, "bold"), bg="#f5f5f5", fg="#4682b4")
title_label.pack(pady=20)

# 定义用户名和密码输入框
tk.Label(win, text="用户名：", font=("Helvetica", 14), bg="#f5f5f5").pack()
input_username = tk.Entry(win, font=("Helvetica", 12), width=30)
input_username.pack(pady=5)
tk.Label(win, text="密码：", font=("Helvetica", 14), bg="#f5f5f5").pack()
input_password = tk.Entry(win, show="*", font=("Helvetica", 12), width=30)
input_password.pack(pady=5)

# 登录按钮、以及处理登录函数
def login_submit():
    if input_username.get() in users and users[input_username.get()] == input_password.get():
        messagebox.showinfo("登录成功", message = "欢迎来到python")
        show_module_selection()
    else:
        messagebox.showinfo("错误", message = "用户名或密码错误，请重新输入！")
login_button = tk.Button(win, text="登录", font=("Helvetica", 14), bg="#4682b4", fg="white", command=login_submit)
login_button.pack(pady=15)

def show_module_selection():
    clear_widget()
    btn_back.pack_forget()
    module_frame = tk.Frame(win, bg="#f5f5f5")
    module_frame.pack(pady=20)
    # 显示模块
    button_rps = tk.Button(module_frame, text = "剪刀石头布", font=("Helvetica", 14), bg="#87ceeb", fg="white", width=20, command = play_rpk)
    button_rps.pack(pady=5)
    button_guess_number = tk.Button(module_frame, text = "猜数字", font=("Helvetica", 14), bg="#87ceeb", fg="white", width=20, command = play_gn)
    button_guess_number.pack(pady=5)
    button_random_group = tk.Button(module_frame, text = "随机分组", font=("Helvetica", 14), bg="#87ceeb", fg="white", width=20, command = random_group)
    button_random_group.pack(pady=5)
    btn_char_conversion = tk.Button(module_frame, text = "字符转换成ASCII码", font=("Helvetica", 14), bg="#87ceeb", fg="white", width=20, command = char_conversion)
    btn_char_conversion.pack(pady=5)
    btn_conversion_of_number = tk.Button(module_frame, text = "进制转换", font=("Helvetica", 14), bg="#87ceeb", fg="white", width=20, command = conversion_of_number_system)
    btn_conversion_of_number.pack(pady=5)
    btn_class_call_the_row = tk.Button(module_frame, text = "班级点名", font=("Helvetica", 14), bg="#87ceeb", fg="white", width=20, command = class_call_the_row)
    btn_class_call_the_row.pack(pady=5)
    btn_guess_word = tk.Button(module_frame, text = "猜单词", font=("Helvetica", 14), bg="#87ceeb", fg="white", width=20, command = guess_word)
    btn_guess_word.pack(pady=5)

# 返回按钮
btn_back = tk.Button(win, text="返回", font=("Helvetica", 14), bg="#4682b4", fg="white", command=show_module_selection)
btn_back.pack()
btn_back.pack_forget()

# 剪刀石头布
def play_rpk():
    clear_widget()
    btn_back.pack()
    # 创建剪刀石头布游戏界面
    game_frame = RockPaperScissorsGame(win)
    game_frame.create_widgets()
    game_frame.pack(expand = True, fill = tk.BOTH)

# 猜数字
def play_gn():
    # 清空当前模块界面
    clear_widget()
    btn_back.pack()
    game_frame = GuessNumber(win)
    game_frame.create_widgets()
    game_frame.pack(expand = True, fill = tk.BOTH)

# 随机分组
def random_group():
    clear_widget()
    btn_back.pack()
    game_frame = RandomGroup(win)
    game_frame.create_widgets()
    game_frame.pack(expand = True, fill = tk.BOTH)

# 字符转换为ASCII码
def char_conversion():
    clear_widget()
    btn_back.pack()
    game_frame = CharConversion(win)
    game_frame.create_widgets()
    game_frame.pack(expand = True, fill = tk.BOTH)

# 进制转换
def conversion_of_number_system():
    clear_widget()
    btn_back.pack()
    game_frame = ConversionOfNumberSystems(win)
    game_frame.create_widgets()
    game_frame.pack(expand = True, fill = tk.BOTH)

# 班级点名
def class_call_the_row():
    clear_widget()
    btn_back.pack()
    game_frame = CallTheRow(win)
    game_frame.create_widgets()
    game_frame.pack(expand = True, fill = tk.BOTH)

# 猜单词
def guess_word():
    clear_widget()
    btn_back.pack()
    game_frame = GuessWord(win)
    game_frame.create_widgets()
    game_frame.pack(expand = True, fill = tk.BOTH)
# 清空页面
def clear_widget():
    for widget in win.winfo_children():
        if widget != btn_back:
            widget.destroy()
win.mainloop()
