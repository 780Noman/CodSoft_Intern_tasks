import tkinter as tk
import math

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

def button_sqrt():
    expression = entry.get()
    result = math.sqrt(eval(expression))
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#f2f2f2")

entry = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0),
    ('8', 1, 1),
    ('9', 1, 2),
    ('/', 1, 3),
    ('4', 2, 0),
    ('5', 2, 1),
    ('6', 2, 2),
    ('*', 2, 3),
    ('1', 3, 0),
    ('2', 3, 1),
    ('3', 3, 2),
    ('-', 3, 3),
    ('0', 4, 0),
    ('C', 4, 1),
    ('=', 4, 2),
    ('+', 4, 3),
    ('√', 5, 0)
]

button_color = "black"
button_text_color = "white"

for button_text, row, column in buttons:
    if button_text in ['+', '-', '*', '/']:
        button = tk.Button(root, text=button_text, padx=20, pady=10, command=lambda text=button_text: button_click(text), font=("Arial", 24, 'bold'), bg=button_color, fg=button_text_color)
    else:
        button = tk.Button(root, text=button_text, padx=25, pady=10, command=lambda text=button_text: button_click(text), font=("Arial", 14), bg=button_color, fg=button_text_color)
    button.grid(row=row, column=column)

clear_button = tk.Button(root, text='Clear', padx=25, pady=10, command=button_clear, font=("Arial", 14), bg=button_color, fg=button_text_color)
clear_button.grid(row=5, column=1)

equal_button = tk.Button(root, text='Result', padx=25, pady=10, command=button_equal, font=("Arial", 14), bg=button_color, fg=button_text_color)
equal_button.grid(row=5, column=2)

sqrt_button = tk.Button(root, text='√', padx=30, pady=10, command=button_sqrt, font=("Arial", 24, 'bold'), bg=button_color, fg=button_text_color)
sqrt_button.grid(row=5, column=0)

root.mainloop()