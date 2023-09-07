import tkinter as tk
from tkinter import font

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def update_task():
    selected_task = task_list.curselection()
    if selected_task:
        updated_task = task_entry.get()
        if updated_task:
            task_list.delete(selected_task)
            task_list.insert(selected_task, updated_task)
            task_entry.delete(0, tk.END)
            tasks[selected_task] = updated_task

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)
        del tasks[selected_task]

def clear_all_tasks():
    task_list.delete(0, tk.END)
    tasks.clear()

window = tk.Tk()
window.title("To-Do List")
window.configure(bg="black")  

task_entry = tk.Entry(window)
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(window, text="Add Task", command=add_task, bg="blue", fg="white")
add_button.grid(row=0, column=1, padx=10, pady=10)

update_button = tk.Button(window, text="Update Task", command=update_task, bg="blue", fg="white")
update_button.grid(row=1, column=0, padx=10, pady=10)

remove_button = tk.Button(window, text="Remove Task", command=remove_task, bg="blue", fg="white")
remove_button.grid(row=2, column=0, padx=10, pady=10)

clear_button = tk.Button(window, text="Clear All Tasks", command=clear_all_tasks, bg="blue", fg="white")
clear_button.grid(row=3, column=0, padx=10, pady=10)

task_list = tk.Listbox(window)
task_list.grid(row=4, column=0, padx=10, pady=10)


listbox_font = font.Font(size=16, weight="bold")
task_list.configure(font=listbox_font)

window.mainloop()