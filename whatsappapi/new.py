import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

additems=[]

window=tk.Tk()
window.title("Shpping List")
window.geometry("600x400")
itemframe=tk.Frame(window)
itemframe.pack()
table=ttk.Treeview(itemframe,columns='shoppingitems',show="headings")
table.grid(row=1,column=0,padx=10,pady=10,columnspan=1)
table.heading("#1",text="AddItem")

def addtotable():
    



    item=item_entry.get()
    if not item:
        messagebox.showerror("Error","emptyitem")
        return

    table.insert('',tk.END,value=(item))
    
    additems.append(item)
    additem.configure(text=f"added item {' '.join(additems)}")
   



def remove():
    selecteditems=table.selection()
    for item in selecteditems:
        itemvalue=table.item(item,"values")[0]
        table.delete(selecteditems)
        if itemvalue in additems:
            additems.remove(itemvalue)
    additem.configure(text=f"{''.join(additems)}")
    feedbacklabel.configure(text="selected item removed")


def clear():
    table.delete(*table.get_children())
    additems.clear()
    additem.configure(text="")

    feedbacklabel.configure(text=f"allitems cleared,",fg="green")

item_label=tk.Label(itemframe,text="Shopping Item",font=("Arial",15),fg="black")
item_label.grid(row=0,column=0,padx=10,pady=10)
item_entry=tk.Entry(itemframe,font=("Arial",15))
item_entry.grid(row=0,column=1)
item_button=tk.Button(itemframe,text="additem",font=("Arial",15),fg="white",bg="blue",command=addtotable)
item_button.grid(row=0,column=2,padx=10,pady=10)
remove_button=tk.Button(itemframe,text="removeitem",font=("Arial",15),fg="white",bg="blue",command=remove)
remove_button.grid(row=0,column=3,padx=10,pady=10)
clear_button=tk.Button(itemframe,text="clearitem",font=("Arial",15),fg="white",bg="blue",command=clear)
clear_button.grid(row=0,column=4,padx=10,pady=10)
additem=tk.Label(window,text="",font=("Arial",15))
additem.pack(pady=10)
feedbacklabel=tk.Label(window,text="",font=("Arial",15))
feedbacklabel.pack(pady=10)




window.mainloop()









































































































































































































