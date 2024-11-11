import tkinter as tk
import random as ran

def dispLabel1():
    kuji = ["大吉", "中吉", "小吉", "吉", "凶"]
    lbl.configure(text=ran.choice(kuji))

root = tk.Tk()
root.geometry("300x200")

lbl = tk.Label(text="今日の運勢")
btn = tk.Button(text="START", command=dispLabel1)

lbl.pack()
btn.pack()
tk.mainloop()