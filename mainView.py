import tkinter as tk

class MainView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

        # Frame Title
        tk.Label(self, text="Personal Finance Tracker", font=("Arial", 24)).pack(pady=20)

        # Navigation Buttons
        tk.Button(self, text="Add Transaction", font=("Arial", 16), command=lambda: controller.show_frame("AddTransactionsView")).pack(pady=10)

        tk.Button(self, text="View Transactions", font=("Arial", 16), command=lambda: controller.show_frame("ViewTransactionsView")).pack(pady=10)

        tk.Button(self, text="Generate Reports", font=("Arial", 16), command=lambda: controller.show_frame("ReportsView")).pack(pady=10)

        tk.Button(self, text="Exit", font=("Arial", 16), command=controller.quit).pack(pady=20)
