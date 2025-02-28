# coding : UTF-8
# Author : zsm
# Created Time : 2024/10/13  14:24
# File Name : 猜单词.PY
# Development Tool : PyCharm
# Description : 猜单词游戏

import random
import tkinter as tk
from tkinter import messagebox


class GuessWord(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.fruits = {}
        self.animals = {}
        self.vegetables = {}
        self.merge_dict = {}
        self.key = None
        self.value = None
        self.count = 0  # 游戏总次数
        self.correct = 0  # 正确次数
        self.error = 0  # 错误次数
        self.master = master
        self.config(bg="#f0f0f0")  # 浅灰背景

    def create_widgets(self):
        # 游戏标题
        title_label = tk.Label(self, text="猜单词游戏", font=("Arial", 16, "bold"), fg="#333333", bg="#f0f0f0")
        title_label.pack(pady=10)
        # 提示选择词库
        tk.Label(self, text="请选择词库 (默认为全部)", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        # 词库选择按钮
        btn_fruits = tk.Button(self, text="水果词组", command=lambda: self.user_choice("fruits"),
                               font=("Arial", 10), bg="#4a90e2", fg="white", relief="groove")
        btn_fruits.pack(pady=3)
        btn_animals = tk.Button(self, text="动物词组", command=lambda: self.user_choice("animals"),
                                font=("Arial", 10), bg="#4a90e2", fg="white", relief="groove")
        btn_animals.pack(pady=3)
        btn_vegetables = tk.Button(self, text="蔬菜词组", command=lambda: self.user_choice("vegetables"),
                                   font=("Arial", 10), bg="#4a90e2", fg="white", relief="groove")
        btn_vegetables.pack(pady=3)
        btn_all = tk.Button(self, text="全部词组", command=lambda: self.user_choice("all"),
                            font=("Arial", 10), bg="#4a90e2", fg="white", relief="groove")
        btn_all.pack(pady=3)
        # 显示打乱后的单词
        self.order_word = tk.Label(self, text="", font=("Arial", 12, "italic"), bg="#f0f0f0", fg="#555555")
        self.order_word.pack(pady=10)
        # 输入和确认按钮
        tk.Label(self, text="请输入正确的单词", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        self.user_input = tk.Entry(self, font=("Arial", 12))
        self.user_input.pack(pady=5)
        btn_affirm = tk.Button(self, text="确认", command=lambda: self.submit(self.user_input.get()),
                               font=("Arial", 12), bg="#4a90e2", fg="white", relief="groove")
        btn_affirm.pack(pady=5)
        # 结果显示
        self.result_label = tk.Label(self, text="", font=("Arial", 12, "italic"), bg="#f0f0f0", fg="#333333")
        self.result_label.pack(pady=10)

    # 显示打乱的单词提示
    def user_choice(self, user_choice):
        user_choice_dict = self.get_words(user_choice)
        # 随机选择一个单词，打乱顺序并显示
        key = random.choice(list(user_choice_dict.keys()))
        value = user_choice_dict[key]
        key_list = list(key)
        random.shuffle(key_list)
        key_str = ''.join(key_list)
        self.order_word.config(text=f"提示单词：{key_str}")
        self.key = key
        self.value = value
        # 清空结果和输入框
        self.result_label.config(text="")
        self.user_input.delete(0, tk.END)

    # 检查用户的猜测
    def submit(self, user_input):
        if user_input != self.key:
            self.result_label.config(text="猜错了！再试一次！", fg="red")
            self.error += 1
        else:
            self.result_label.config(text=f"猜对了！答案是：{self.key} - {self.value}", fg="green")
            self.correct += 1

    # 返回选定词库
    def get_words(self, user_choice="all"):
        fruits = {
            "Apple": "苹果",
            "Banana": "香蕉",
            "Orange": "橙子",
            "Grape": "葡萄",
            "Strawberry": "草莓",
            "Pineapple": "菠萝",
            "Mango": "芒果",
            "Watermelon": "西瓜",
            "Peach": "桃子",
            "Pear": "梨",
            "Cherry": "樱桃",
            "Lemon": "柠檬",
            "Lime": "青柠",
            "Kiwi": "奇异果（猕猴桃）",
            "Plum": "李子",
            "Apricot": "杏子",
            "Blueberry": "蓝莓",
            "Raspberry": "树莓",
            "Blackberry": "黑莓",
            "Avocado": "牛油果"
        }

        animals = {
            "Dog": "狗",
            "Cat": "猫",
            "Elephant": "大象",
            "Lion": "狮子",
            "Tiger": "老虎",
            "Bear": "熊",
            "Monkey": "猴子",
            "Giraffe": "长颈鹿",
            "Zebra": "斑马",
            "Wolf": "狼",
            "Fox": "狐狸",
            "Rabbit": "兔子",
            "Horse": "马",
            "Cow": "牛",
            "Sheep": "绵羊",
            "Goat": "山羊",
            "Pig": "猪",
            "Chicken": "鸡",
            "Duck": "鸭子",
            "Fish": "鱼"
        }

        vegetables = {
            "Tomato": "番茄",
            "Carrot": "胡萝卜",
            "Potato": "土豆",
            "Onion": "洋葱",
            "Cucumber": "黄瓜",
            "Lettuce": "生菜",
            "Broccoli": "西兰花",
            "Spinach": "菠菜",
            "Bell Pepper": "彩椒",
            "Garlic": "大蒜",
            "Cabbage": "卷心菜",
            "Cauliflower": "花椰菜",
            "Green Bean": "青豆",
            "Pea": "豌豆",
            "Zucchini": "西葫芦",
            "Eggplant": "茄子",
            "Radish": "萝卜",
            "Celery": "芹菜",
            "Kale": "羽衣甘蓝",
            "Asparagus": "芦笋"
        }

        if user_choice == "fruits":
            return fruits
        if user_choice == "animals":
            return animals
        if user_choice == "vegetables":
            return vegetables
        merge_dict = {**fruits, **animals, **vegetables}
        return merge_dict


if __name__ == "__main__":
    win = tk.Tk()
    win.title("猜单词游戏")
    win.geometry("400x500")
    # 创建游戏框架， 传入主窗口作为父窗口
    game_frame = GuessWord(win)
    # 将框架添加到主窗口中，填满可用空间
    game_frame.pack(expand=True, fill=tk.BOTH)
    win.mainloop()
