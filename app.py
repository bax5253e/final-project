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

# Create a button
view_expense_button = tk.Button(
    root, 
    text="View Expenses", 
    font=("Helvetica", 12), 
    width=20)

# Pack the button
view_expense_button.pack(pady=5)

# Create a button
report_button = tk.Button(
    root, 
    text="Generate Report", 
    font=("Helvetica", 12), 
    width=20)

# Pack the button
report_button.pack(pady=5)

# Create a button
exit_button = tk.Button(
    root, 
    text="Exit", 
    font=("Helvetica", 12), 
    width=20, 
    command=root.quit)

# Pack the button
exit_button.pack(pady=20)




root.mainloop()

