import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Global list to store the names of added items
added_items = []

def addtotable():
    item_name = item_text.get()
    quantity_name = quantity_text.get()
    price = price_text.get()
    total = total_text.get()
    category = category_text.get()

    # Check for empty fields
    if not item_name or not quantity_name or not price or not total or not category:
        messagebox.showwarning("Input Error", "Please fill out all fields.")
        return

    # Validate numeric values
    try:
        quantity_value = float(quantity_name)
        price_value = float(price)
        total_value = float(total)
        if quantity_value < 0 or price_value < 0 or total_value < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Quantity, Price, and Total must be non-negative numbers.")
        return

    # Insert new item into the table with category
    table.insert("", tk.END, values=(item_name, quantity_name, price, total, category))

    # Update the list of added items
    added_items.append(item_name)
    feedback_label.config(text=f"Added items: {', '.join(added_items)}")

    # Clear input fields
    item_text.delete(0, tk.END)
    quantity_text.delete(0, tk.END)
    price_text.delete(0, tk.END)
    total_text.delete(0, tk.END)
    category_text.delete(0, tk.END)
    
    # Update grand total
    update_grand_total()

def update_grand_total():
    grand_totals = 0
    for item in table.get_children():
        values = table.item(item, "values")
        try:
            ind_total = float(values[3])
            grand_totals += ind_total
        except ValueError:
            continue
    grand_total.config(text=f"Grand Total INR: {grand_totals:.2f}")

def populate_entry_fields(event):
    selected_item = table.selection()
    if not selected_item:
        return
    
    # Get the values of the selected item
    item_values = table.item(selected_item[0], 'values')
    
    # Populate the Entry fields with the selected item's data
    item_text.delete(0, tk.END)
    item_text.insert(0, item_values[0])
    quantity_text.delete(0, tk.END)
    quantity_text.insert(0, item_values[1])
    price_text.delete(0, tk.END)
    price_text.insert(0, item_values[2])
    total_text.delete(0, tk.END)
    total_text.insert(0, item_values[3])
    category_text.delete(0, tk.END)
    category_text.insert(0, item_values[4])

def save_edits():
    selected_item = table.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select an item to edit.")
        return

    item_name = item_text.get()
    quantity_name = quantity_text.get()
    price = price_text.get()
    total = total_text.get()
    category = category_text.get()

    # Validate numeric values
    try:
        quantity_value = float(quantity_name)
        price_value = float(price)
        total_value = float(total)
        if quantity_value < 0 or price_value < 0 or total_value < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Quantity, Price, and Total must be non-negative numbers.")
        return

    # Update the selected item with new values
    table.item(selected_item[0], values=(item_name, quantity_name, price, total, category))
    
    # Update the list of added items
    update_added_items()
    feedback_label.config(text=f"Edited item: {item_name}")

    # Clear input fields
    item_text.delete(0, tk.END)
    quantity_text.delete(0, tk.END)
    price_text.delete(0, tk.END)
    total_text.delete(0, tk.END)
    category_text.delete(0, tk.END)
    
    # Update grand total
    update_grand_total()

def update_added_items():
    added_items.clear()
    for item in table.get_children():
        values = table.item(item, 'values')
        added_items.append(values[0])
    feedback_label.config(text=f"Added items: {', '.join(added_items)}")

def delete_row():
    selected_item = table.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select an item to delete.")
        return
    for item in selected_item:
        table.delete(item)
    update_grand_total()

def clear_table():
    for items in table.get_children():
        table.delete(items)
    update_grand_total()

def calculate():
    try:
        quantity = float(quantity_text.get())
        price = float(price_text.get())
        total = quantity * price
        total_text.delete(0, tk.END)
        total_text.insert(0, f"{total:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for Quantity and Price.")

def filter_by_category(*args):
    selected_category = category_filter.get()
    for item in table.get_children():
        values = table.item(item, 'values')
        if selected_category == 'All' or values[4] == selected_category:
            table.item(item, tags=('visible',))
        else:
            table.item(item, tags=('hidden',))

    # table.tag_configure('hidden', foreground='gray')
    # table.tag_configure('visible', foreground='black')

# Initialize the main window
window = tk.Tk()
window.title("Billing System")
window.geometry("800x500")

heading = tk.Label(window, text="Billing System", font="Tahoma 20")
heading.pack()

item_details = tk.Frame(window)
item_details.pack()

item_label = tk.Label(item_details, text="Item Name", font=("Arial", 15))
item_label.grid(row=0, column=0)
quantity_label = tk.Label(item_details, text="Quantity", font=("Arial", 15))
quantity_label.grid(row=0, column=1)
price_label = tk.Label(item_details, text="Price", font=("Arial", 15))
price_label.grid(row=0, column=2)
total_label = tk.Label(item_details, text="Total", font=("Arial", 15))
total_label.grid(row=0, column=3)
category_label = tk.Label(item_details, text="Category", font=("Arial", 15))
category_label.grid(row=0, column=4)

item_text = tk.Entry(item_details, font=("Arial", 15), width=10)
item_text.grid(row=1, column=0)
quantity_text = tk.Entry(item_details, font=("Arial", 15), width=10, justify="right")
quantity_text.grid(row=1, column=1)
price_text = tk.Entry(item_details, font=("Arial", 15), width=10, justify="right")
price_text.grid(row=1, column=2)
total_text = tk.Entry(item_details, font=("Arial", 15), width=10, justify="right")
total_text.grid(row=1, column=3)
category_text = tk.Entry(item_details, font=("Arial", 15), width=10)
category_text.grid(row=1, column=4)

calc_btn = tk.Button(item_details, text="Calculate", font=("Arial", 15), bg="blue", fg="white", command=calculate)
calc_btn.grid(row=2, column=2, padx=10, pady=10)
add_total = tk.Button(item_details, text="Add to Total", font=("Arial", 15), bg="blue", fg="white", command=addtotable)
add_total.grid(row=2, column=3, padx=10, pady=10)
delete_btn = tk.Button(item_details, text="Delete", font=("Arial", 15), bg="red", fg="white", command=delete_row)
delete_btn.grid(row=2, column=4, padx=10, pady=10)
clear_btn = tk.Button(item_details, text="Clear Items", font=("Arial", 15), bg="purple", fg="white", command=clear_table)
clear_btn.grid(row=2, column=5, padx=10, pady=10)

edit_btn = tk.Button(item_details, text="Edit Selected", font=("Arial", 15), bg="orange", fg="white", command=save_edits)
edit_btn.grid(row=3, column=0, padx=10, pady=10)

table = ttk.Treeview(item_details, columns=('item', 'quantity', 'price', 'total', 'category'), show='headings')
table.grid(row=4, column=0, columnspan=6, padx=10, pady=10)
table.heading("#1", text="Item Name")
table.heading('#2', text="Quantity")
table.heading('#3', text="Price")
table.heading('#4', text="Total")
table.heading('#5', text="Category")

# Bind the table selection event to populate Entry fields
table.bind('<<TreeviewSelect>>', populate_entry_fields)

# Add a dropdown menu for category filtering
categories = ['All', 'Category1', 'Category2', 'Category3']  # Example categories
category_filter = tk.StringVar(value='All')
category_menu = tk.OptionMenu(window, category_filter, *categories, command=filter_by_category)
category_menu.pack(pady=10)

feedback_label = tk.Label(window, text="", font=("Arial", 15))
feedback_label.pack(pady=20)

grand_total = tk.Label(window, text="Grand Total INR: 0.00", font=('Arial', 30), fg="green")
grand_total.pack(padx=10, pady=10)

window.mainloop()
