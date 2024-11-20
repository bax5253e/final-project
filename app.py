import tkinter as tk

root = tk.Tk()
root.title("Personal Finance Tracker")
root.geometry("800x600")


# Create a label
title_label = tk.Label(
    root, 
    text="Personal Finance Tracker", 
    font=("Helvetica", 16),
    bd=2,  # Border width
    relief="solid")

# Pack the label
title_label.pack(pady=50)

# Create a button
add_expense_button = tk.Button(
    root, 
    text="Add Expense", 
    font=("Helvetica", 12), 
    width=20)

# Pack the button
add_expense_button.pack(pady=5)

root.mainloop()

