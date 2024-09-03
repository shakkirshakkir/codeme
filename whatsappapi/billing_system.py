import tkinter as tk
from tkinter import ttk

def calculate():
    quantity=float(quantity_text.get())
    price=float(price_text.get())
    total=quantity*price
    total_text.delete(0,tk.END)
    total_text.insert(0,total)

def addtotable():
    item_name=item_text.get()
    quantity_name=quantity_text.get()
    price=price_text.get()
    total=total_text.get()

    table.insert("",tk.END,values=(item_name,quantity_name,price,total))

    item_text.delete(0,tk.END)
    quantity_text.delete(0,tk.END)
    price_text.delete(0,tk.END)
    total_text.delete(0,tk.END)
    grand_totals=0

    for item in table.get_children():
        values=table.item(item,"values")
        ind_total=float(values[3])
        grand_totals+=ind_total
        grand_total.configure(text=f"Grand Total:{grand_totals}")

def delete_row():
    selected_item=table.selection()
    if selected_item:
        table.delete(selected_item)


window=tk.Tk()
window.title("Billing system")
window.geometry("600x400")


heading=tk.Label(window,text="Billing System",
font="tohomo 20"
)
heading.pack()

item_details=tk.Frame(window)
item_details.pack()

for col in range(4):
    item_details.columnconfigure(col,minsize=150)

item_label=tk.Label(item_details,text="Item Name",font=("Arial",15))
item_label.grid(row=0,column=0)
quantity_label=tk.Label(item_details,text="Quantity",font=("Arial",15))
quantity_label.grid(row=0,column=1)
price_label=tk.Label(item_details,text="Price",font=("Arial",15))
price_label.grid(row=0,column=2)
total_label=tk.Label(item_details,text="Total",font=("Arial",15))
total_label.grid(row=0,column=3)


item_text=tk.Entry(item_details,font=("Arial",15),width=10)
item_text.grid(row=1,column=0)
quantity_text=tk.Entry(item_details,font=("Arial",15),width=10,justify="right")
quantity_text.grid(row=1,column=1)
price_text=tk.Entry(item_details,font=("Arial",15),width=10,justify="right")
price_text.grid(row=1,column=2)
total_text=tk.Entry(item_details,font=("Arial",15),width=10,justify="right")
total_text.grid(row=1,column=3)

calc_btn=tk.Button(item_details,text="Calculate",font=("Arial",15),bg="blue",fg="white",command=calculate)
calc_btn.grid(row=2,column=2,padx=10,pady=10)
add_total=tk.Button(item_details,text="Add to total",font=("Arial",15),bg="blue",fg="white",command=addtotable)
add_total.grid(row=2,column=3,padx=10,pady=10)
delete_btn=tk.Label(item_details,text="Delete",font=("Arial",15),bg="blue",fg="white",command=delete_row)
delete_btn.grid(row=0,column=4)

table=ttk.Treeview(item_details,columns=('item','quantity','price','total'),show='headings')
table.grid(row=3,column=0,columnspan=4,padx=10,pady=10)
table.heading("#1",text="Item name")
table.heading('#2',text="Quantity Name")
table.heading('#3',text="Price")
table.heading('#4',text="Total")
grand_total=tk.Label(window,text="Grand Total:",font=('Arial',30),fg="green")
grand_total.pack(padx=10,pady=10)



window.mainloop()