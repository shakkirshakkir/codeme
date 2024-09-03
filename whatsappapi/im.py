import tkinter as tk
from tkinter import messagebox

class ShoppingListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping List")

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Entry widget to enter new items
        self.item_entry = tk.Entry(self.root, width=50)
        self.item_entry.pack(pady=10)

        # Button to add items to the list
        self.add_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_button.pack(pady=5)

        # Listbox to display items
        self.item_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50, height=10)
        self.item_listbox.pack(pady=10)

        # Button to remove selected items
        self.remove_button = tk.Button(self.root, text="Remove Selected Item", command=self.remove_item)
        self.remove_button.pack(pady=5)

        # Button to clear all items
        self.clear_button = tk.Button(self.root, text="Clear List", command=self.clear_list)
        self.clear_button.pack(pady=5)

        # Label to show feedback messages
        self.feedback_label = tk.Label(self.root, text="", fg="green")
        self.feedback_label.pack(pady=5)

    def add_item(self):
        item = self.item_entry.get().strip()  # Get text from the Entry widget
        if item:
            self.item_listbox.insert(tk.END, item)  # Add item to the Listbox
            self.item_entry.delete(0, tk.END)  # Clear the Entry widget
            self.feedback_label.config(text=f"'{item}' added to the list.", fg="green")
        else:
            messagebox.showwarning("Input Error", "Cannot add an empty item. Please enter a valid item.")
            self.feedback_label.config(text="", fg="green")

    def remove_item(self):
        selected_index = self.item_listbox.curselection()
        if selected_index:
            item = self.item_listbox.get(selected_index)
            self.item_listbox.delete(selected_index)
            self.feedback_label.config(text=f"'{item}' removed from the list.", fg="red")
        else:
            messagebox.showwarning("Selection Error", "No item selected. Please select an item to remove.")
            self.feedback_label.config(text="", fg="red")

    def clear_list(self):
        self.item_listbox.delete(0, tk.END)
        self.feedback_label.config(text="List cleared.", fg="blue")

# Create the main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingListApp(root)
    root.mainloop()
