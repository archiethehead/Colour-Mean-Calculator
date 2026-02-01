import tkinter as tk
from tkinter import colorchooser

from hex_calculator.calculator import hex_mean



test = ["004b9d",
        "202f55",
        "13c2f0",
        "003882",
        "2472ce",
        "0d2b60",
        "123576"]

root = tk.Tk()
root.title("Colour Mean Calculator")
root.geometry("600x400")

label = tk.Label(root, text = test)
label.pack()

label2 = tk.Label(root, text = hex_mean)
label2.pack()

label3 = tk.Label(root, text = "The mean colour is: " + hex_mean(test))
label3.pack()


frame = tk.Frame(root)
frame.pack()

print(hex_mean(test))

root.mainloop()