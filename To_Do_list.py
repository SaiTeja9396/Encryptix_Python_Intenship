import tkinter as tk
from tkinter import ttk, messagebox
import json

class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List App")
        self.geometry("500x550")
        self.configure(bg="#f0f0f0")
        
        # Configure the grid layout
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Task input with placeholder behavior
        self.task_input = ttk.Entry(self, font=("Helvetica", 14), width=30)
        self.task_input.grid(row=0, column=0, padx=20, pady=10)
        self.task_input.insert(0, "Enter your tasks:")
        self.task_input.bind("<FocusIn>", self.clear_placeholder)
        self.task_input.bind("<FocusOut>", self.restore_placeholder)
        
        # Task list
        self.task_list = tk.Listbox(self, font=("Helvetica", 14), height=10, selectmode=tk.SINGLE, bg="#ffffff", fg="#333333")
        self.task_list.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        
        # Frame for buttons
        button_frame = tk.Frame(self, bg="#f0f0f0")
        button_frame.grid(row=2, column=0, pady=10)
        
        # Buttons for adding, marking done, deleting, and viewing status
        self.add_button = ttk.Button(button_frame, text="Add", command=self.add_task, style="Add.TButton")
        self.add_button.grid(row=0, column=0, padx=5)
        
        self.done_button = ttk.Button(button_frame, text="Done", command=self.mark_done, style="Done.TButton")
        self.done_button.grid(row=0, column=1, padx=5)
        
        self.delete_button = ttk.Button(button_frame, text="Delete", command=self.delete_task, style="Delete.TButton")
        self.delete_button.grid(row=0, column=2, padx=5)
        
        self.view_status_button = ttk.Button(button_frame, text="View Status", command=self.view_status, style="Status.TButton")
        self.view_status_button.grid(row=0, column=3, padx=5)
        
        # Custom styles
        style = ttk.Style()
        style.configure("Add.TButton", background="#5cb85c", font=("Helvetica", 12, "bold"))
        style.configure("Done.TButton", background="#0275d8", font=("Helvetica", 12, "bold"))
        style.configure("Delete.TButton", background="#d9534f", font=("Helvetica", 12, "bold"))
        style.configure("Status.TButton", background="#5bc0de", font=("Helvetica", 12, "bold"))
        style.map("TButton",
                  background=[("active", "!disabled", "#e6e6e6")],
                  foreground=[("active", "!disabled", "#333333")])
        
        # Load tasks from JSON file
        self.load_tasks()
    
    def view_status(self):
        done_count = 0
        total_count = self.task_list.size()
        for i in range(total_count):
            if self.task_list.itemcget(i, "foreground") == "green":
                done_count += 1
        messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}")
    
    def add_task(self):
        task = self.task_input.get()
        if task != "Enter your tasks:" and task != "":
            self.task_list.insert(tk.END, task)
            self.task_list.itemconfig(tk.END, foreground="green")
            self.task_input.delete(0, tk.END)
            self.save_tasks()
            messagebox.showinfo("Task Added", "Your task has been added successfully!")
    
    def mark_done(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.itemconfig(task_index, foreground="green")
            self.save_tasks()
            messagebox.showinfo("Task Completed", "Your task has been marked as done!")
    
    def delete_task(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.delete(task_index)
            self.save_tasks()
            messagebox.showinfo("Task Deleted", "Your task has been deleted!")
    
    def clear_placeholder(self, event):
        if self.task_input.get() == "Enter your tasks:":
            self.task_input.delete(0, tk.END)
    
    def restore_placeholder(self, event):
        if self.task_input.get() == "":
            self.task_input.insert(0, "Enter your tasks:")
    
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                for task in data:
                    self.task_list.insert(tk.END, task["text"])
                    self.task_list.itemconfig(tk.END, foreground=task["color"])
        except FileNotFoundError:
            pass
    
    def save_tasks(self):
        data = []
        for i in range(self.task_list.size()):
            text = self.task_list.get(i)
            color = self.task_list.itemcget(i, "foreground")
            data.append({"text": text, "color": color})
        with open("tasks.json", "w") as f:
            json.dump(data, f)

if __name__ == '__main__':
    app = TodoListApp()
    app.mainloop()
