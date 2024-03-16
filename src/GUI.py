import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("500x500")
root.title("Kurva Bézier")

label = tk.Label(root, text="Welcome to Bézier Curve Maker!", font=('Arial', 18))
label.pack(padx=10, pady=10)

jumlah_titik = tk.Label(root, text="Input jumlah titik: ", height=3, font=('Arial', 12))
jumlah_titik.pack()

entry = tk.Entry(root)
entry.pack()

textbox = tk.Text(root, height=3, font=('Arial', 12))
textbox.pack(padx=10, pady=10)


btnshow = tk.Button(root, text="Show Bézier Curve", font=('Arial', 12))
btnshow.pack(padx=10, pady=10)

root.mainloop()