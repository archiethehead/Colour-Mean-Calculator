import tkinter as tk
from tkinter import colorchooser

from hex_calculator.calculator import hex_mean

def add_colour():
    colour_code = colorchooser.askcolor(title ="Choose color")
    if colour_code:
        hex_code = colour_code[1][1:]  # Get hex code without '#'
        listbox.insert(tk.END, hex_code)
        update_mean_colour()

def update_mean_colour():
    items = listbox.get(0, tk.END)
    if items:
        mean_hex = hex_mean(items)
        label2.config(text="The mean colour is: #" + mean_hex)
        colour_canvas.config(bg="#" + mean_hex)
    else:
        label2.config(text="The mean colour is: #000000")
        colour_canvas.config(bg="#000000")

def delete_colour():
    selected_indices = listbox.curselection()
    for index in reversed(selected_indices):
        listbox.delete(index)
    update_mean_colour()

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

label1 = tk.Label(root, text = "Selected Colours:")
label1.place(x=33, y=20)

listbox = tk.Listbox(root)
for item in test:
    listbox.insert(tk.END, item)
listbox.place(x=20, y=50)


label2 = tk.Label(root, text = "The mean colour is: #" + hex_mean(test))
label2.pack()

colour_canvas = tk.Canvas(root, bg="#" + hex_mean(test), width=150, height=150)
colour_canvas.pack()

add_colour_button = tk.Button(root, text="Add colour", command= add_colour) 
add_colour_button.pack()

delete_colour_button = tk.Button(root, text="Delete colour", command= delete_colour) 
delete_colour_button.pack()


root.mainloop()