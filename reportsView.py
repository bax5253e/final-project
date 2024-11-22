import tkinter as tk

class ReportsView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew") # This line is controlling the layout of the frame

        # Frame Title
        tk.Label(self, text="Generate Reports", font=("Arial", 24)).pack(pady=20)

        tk.Label(self, text="Functionality not yet implemented", font=("Arial", 16)).pack(pady=20)

        # Go back button
        tk.Button(self, text="Back", font=("Arial", 16), 
                  command=lambda: controller.show_frame("MainView")).pack(pady=10)