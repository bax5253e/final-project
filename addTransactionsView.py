import tkinter as tk
from tkinter import ttk

class AddTransactionsView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

        # Frame Title
        tk.Label(self, text="Add Transaction", font=("Arial", 24)).pack(pady=20)

        # Entry Fields
        entry_frame = tk.Frame(self)
        entry_frame.pack(pady=10)
        tk.Label(entry_frame, text="Amount:", font=("Arial", 16)).grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(entry_frame).grid(row=0, column=1, padx=5, pady=5)
        tk.Label(entry_frame, text="Description:", font=("Arial", 16)).grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(entry_frame).grid(row=1, column=1, padx=5, pady=5)
        tk.Label(entry_frame, text="Date:", font=("Arial", 16)).grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(entry_frame).grid(row=2, column=1, padx=5, pady=5)
        tk.Label(entry_frame, text="Category:", font=("Arial", 16)).grid(row=3, column=0, padx=5, pady=5)
        ttk.Combobox(entry_frame, values=["Income", "Food", "Rent", "Utilities", "Other"]).grid(row=3, column=1, padx=5, pady=5)


        # Go back button
        tk.Button(self, text="Add Transaction", font=("Arial", 16)).pack(pady=10)
        tk.Button(self, text="Back to Main Menu", font=("Arial", 16), 
                  command=lambda: controller.show_frame("MainView")).pack(pady=10)
        