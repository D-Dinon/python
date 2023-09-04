import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikacija za vođenje popisa zadataka")

        self.conn = sqlite3.connect('tasks.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task_name TEXT, due_date TEXT)')
        self.conn.commit()

        self.task_name_label = tk.Label(root, text="Naziv zadatka:")
        self.task_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.task_name_entry = tk.Entry(root)
        self.task_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.due_date_label = tk.Label(root, text="Rok (DD-MM-YYYY):")
        self.due_date_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.due_date_entry = tk.Entry(root)
        self.due_date_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.add_button = tk.Button(root, text="Dodaj zadatak", command=self.add_task)
        self.add_button.grid(row=2, columnspan=2, padx=10, pady=5)

        self.tasks_frame = tk.Frame(root)
        self.tasks_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        self.delete_buttons = []
        self.refresh_list()

    def add_task(self):
        task_name = self.task_name_entry.get()
        due_date = self.due_date_entry.get()

        if task_name and self.validate_date(due_date):
            self.cursor.execute('INSERT INTO tasks (task_name, due_date) VALUES (?, ?)', (task_name, due_date))
            self.conn.commit()
            self.refresh_list()
            self.task_name_entry.delete(0, tk.END)
            self.due_date_entry.delete(0, tk.END)
        else:
            if not task_name:
                messagebox.showwarning("Upozorenje", "Molimo unesite naziv zadatka.")
            else:
                messagebox.showwarning("Upozorenje", "Neispravan format datuma. Format: DD-MM-YYYY")

    def delete_task(self, task_id):
        self.cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        self.conn.commit()
        self.refresh_list()

    def validate_date(self, date_string):
        try:
            datetime.strptime(date_string, '%d-%m-%Y')
            return True
        except ValueError:
            return False

    def refresh_list(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        self.delete_buttons = []

        self.cursor.execute('SELECT * FROM tasks')
        tasks = self.cursor.fetchall()
        for row, task in enumerate(tasks):
            task_name = task[1]
            task_name_label = tk.Label(self.tasks_frame, text=task_name, fg='green')
            task_name_label.grid(row=row, column=0, padx=5, pady=2, sticky="w")

            due_date = task[2]
            due_date_label = tk.Label(self.tasks_frame, text=due_date, fg='red')
            due_date_label.grid(row=row, column=1, padx=5, pady=2, sticky="w")

            delete_button = tk.Button(self.tasks_frame, text="Obriši", command=lambda task_id=task[0]: self.delete_task(task_id))
            delete_button.grid(row=row, column=2, padx=5, pady=2, sticky="e")

            self.delete_buttons.append(delete_button)

if __name__ == '__main__':
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()

    app.conn.close()