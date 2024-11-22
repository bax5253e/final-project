import tkinter as tk
from tkinter import ttk

class ViewTransactionsView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

        # Frame Title
        tk.Label(self, text="View Transactions", font=("Arial", 24)).pack(pady=20)

        # Create a treeview
        ttk.Treeview(self, 
                     columns=("Amount", "Description", "Date", "Category"), 
                     height=10, show="headings").pack(pady=20, fill="both", expand=True)


        # Go back button
        tk.Button(self, text="Back", font=("Arial", 16), 
                  command=lambda: controller.show_frame("MainView")).pack(pady=10)