import tkinter as tk
from tkinter import colorchooser

from hex_calculator.calculator import hex_mean

def add_colour():
    colour_code = colorchooser.askcolor(title ="Choose your colour")
    if colour_code and colour_code[0] != None:
        hex_code = colour_code[1][1:] 
        listbox.insert(tk.END, hex_code)
        update_mean_colour()

def update_mean_colour():
    items = listbox.get(0, tk.END)
    if items:
        mean_hex = hex_mean(items)
        label2.config(text="The mean colour is: #" + mean_hex)
        colour_canvas.config(bg="#" + mean_hex)
        print(mean_hex)
    else:
        label2.config(text="The mean colour is: #000000")
        colour_canvas.config(bg="#000000")

def delete_colour():
    selected_indices = listbox.curselection()
    for index in reversed(selected_indices):
        listbox.delete(index)
    update_mean_colour()

def update_selected_colour_display(event=None):
    selected_indices = listbox.curselection()
    if selected_indices:
        selected_colour_from_list = listbox.get(selected_indices[0])
        selected_colour_canvas.config(bg="#" + selected_colour_from_list)
        selected_colour_label.config(text="Your selected colour: #" + selected_colour_from_list)
    else:
        selected_colour_canvas.config(bg="#ffffff")
        selected_colour_label.config(text="Your selected colour: #ffffff")

def clear_all():
    listbox.delete(0, tk.END)
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
label1.place(x=33, y=40)

listbox = tk.Listbox(root, width=20, height=14)
for item in test:
    listbox.insert(tk.END, item)
listbox.place(x=20, y=70)

label2 = tk.Label(root, text = "The mean colour is: #" + hex_mean(test), font=("Arial", 14, "bold"))
label2.place(x=280,y=40)

colour_canvas = tk.Canvas(root, bg="#" + hex_mean(test), width=225, height=225)
colour_canvas.place(x=300,y=70)

add_colour_button = tk.Button(root, text="Add colour", command= add_colour) 
add_colour_button.place(x=170,y=100)

delete_colour_button = tk.Button(root, text="Delete colour", command= delete_colour) 
delete_colour_button.place(x=170,y=140)

clear_all_button = tk.Button(root, text="Clear all", command= clear_all)
clear_all_button.place(x=170,y=180)

selected_colour_from_list = listbox.get(tk.ACTIVE)

selected_colour_canvas = tk.Canvas(root, bg="#" + selected_colour_from_list if selected_colour_from_list else "#ffffff", width=50, height=50)
selected_colour_canvas.place(x=20,y=320)

selected_colour_label = tk.Label(root, text="Your selected colour: #" + selected_colour_from_list if selected_colour_from_list else "Your selected colour: #ffffff")
selected_colour_label.place(x=80,y=335)

listbox.bind("<<ListboxSelect>>", update_selected_colour_display)

root.mainloop()