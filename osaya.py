import tkinter as tk
def tasu():
    value1 = entry1.get()
    sahen = int(value1)
    value2 = entry2.get()
    uhen = int(value2)
    sum = sahen + uhen
    lbl.configure(text=sum)
def hiku():
    value1 = entry1.get()
    sahen = int(value1)
    value2 = entry2.get()
    uhen = int(value2)
    sum = sahen - uhen
    lbl.configure(text=sum)
def kakeru():
    value1 = entry1.get()
    sahen = int(value1)
    value2 = entry2.get()
    uhen = int(value2)
    sum = sahen * uhen
    lbl.configure(text=sum)
def waru():
    value1 = entry1.get()
    sahen = int(value1)
    value2 = entry2.get()
    uhen = int(value2)
    sum = sahen / uhen
    lbl.configure(text=sum)
root = tk.Tk()
root.geometry("300x300")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

lbl = tk.Label(text="答え")
btn1 = tk.Button(text="+",command = tasu)
btn2 = tk.Button(text="-",command = hiku)
btn3 = tk.Button(text="X",command = kakeru)
btn4 = tk.Button(text="÷",command = waru)

entry1.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
entry2.pack()
lbl.pack()
tk.mainloop()