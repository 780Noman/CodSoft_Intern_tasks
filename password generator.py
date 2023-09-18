import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(password_length))
    generated_password_entry.delete(0, tk.END)
    generated_password_entry.insert(tk.END, password)

def accept_password():
    username = username_entry.get()
    password = generated_password_entry.get()
    print("Username:", username)
    print("Password:", password)

def reset_fields():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    generated_password_entry.delete(0, tk.END)


window = tk.Tk()
window.geometry("600x500")
window.title("Password Generator")

extra_large_font = ("TkDefaultFont", 20)


button_color = "blue"
background_color = "black"


showLabel = tk.Label(window, text="Password Generator", font=("Alvicta", 20, 'bold'), fg="Purple", bg=background_color,)
showLabel.grid(row=0, column=0, columnspan=2, padx=5, pady=25)


window.configure(bg=background_color)


username_label = tk.Label(window, fg="white", text="Username:", font=extra_large_font, bg=background_color)
username_label.grid(row=1, column=0, padx=5, pady=5)
username_entry = tk.Entry(window, font=extra_large_font)
username_entry.grid(row=1, column=1, padx=5, pady=5)

length_label = tk.Label(window, fg="white",text="Password Length:", font=extra_large_font, bg=background_color)
length_label.grid(row=2, column=0, padx=5, pady=5)
length_entry = tk.Entry(window, font=extra_large_font)
length_entry.grid(row=2, column=1, padx=5, pady=5)


generate_button = tk.Button(window, text="Generate Password", command=generate_password, font=extra_large_font, bg=button_color, fg="white")
generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


generated_password_entry = tk.Entry(window, font=extra_large_font)
generated_password_entry.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


accept_button = tk.Button(window, text="Accept", command=accept_password, font=extra_large_font, bg=button_color, fg="white")
accept_button.grid(row=5, column=0, padx=5, pady=5)

reset_button = tk.Button(window, text="Reset", command=reset_fields, font=extra_large_font, bg=button_color, fg="white")
reset_button.grid(row=5, column=1, padx=5, pady=5)


window.attributes("-topmost", True)


window.mainloop()
