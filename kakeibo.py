import tkinter as tk

# 関数の設定
def regist():
    ans1 = entry1.get()
    ans2 = entry2.get()
    ans3 = entry3.get()

# 箱の作成
root = tk.Tk()
root.title("家計簿")
root.geometry("800x600")
#hogeho
# ラベルの作成
lbl1 = tk.Label(root, text="日付")
lbl2 = tk.Label(root, text="摘要")
lbl3 = tk.Label(root, text="金額") 

# 空白の作成
entry1 = tk.Entry()
entry2 = tk.Entry()
entry3 = tk.Entry()

# 配置
lbl1.grid(column=3, row=2)
entry1.grid(column=4, row=2)
lbl2.grid(column=3, row=3)
entry2.grid(column=4, row=3)
lbl3.grid(column=3, row=4)
entry3.grid(column=4, row=4)

btn1 = tk.Button(root, text="合計金額").grid(column=4, row=5)

tk.mainloop()


