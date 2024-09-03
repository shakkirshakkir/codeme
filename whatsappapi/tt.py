import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


addeditems=[]
def calculate():
    quantity_errcheck = float(quantity_entry.get())
    price_errcheck = float(price_entry.get())
    
    if quantity_errcheck<0 or price_errcheck<0:
        messagebox.showerror("Error", "Both quantity and price must be filled with non negative.")
        return


 

    total_entrynew = quantity_errcheck * price_errcheck


    total_entry.delete(0, tk.END)
    total_entry.insert(0, f"{total_entrynew:.2f}")




def total():
    

    itemlabel=item_entry.get()
    quantitylabel=quantity_entry.get()
    pricelabel=price_entry.get()
    totallabel=total_entry.get()
    table.insert('',tk.END,values=(itemlabel,quantitylabel,pricelabel,totallabel))

    item_entry.delete(0,tk.END)
    quantity_entry.delete(0,tk.END)
    price_entry.delete(0,tk.END)
    total_entry.delete(0,tk.END)
    grandtotal=0.0
    addeditems.append(itemlabel)
    addedlists.config(text=f"addeditemlists:{''.join(addeditems)}")


    for item in table.get_children():
        values=table.item(item,"values")
        inditem=float(values[3])
        grandtotal+=inditem
        grand_total.configure(text=f"GrandTotal: {grandtotal}")
        # grand_total.configure(text=f"Grand Total: {grandtotal:.2f}")


def delete():
    selecteditem=table.selection()
    if selecteditem:
        table.delete(selecteditem)

def clear():
    for item in table.get_children():  
        table.delete(item) 







window=tk.Tk()
window.title("Tragon Media Interview on 2.9.24")
window.geometry("600x400")
heading=tk.Label(window,text="Trogon Media ULCyberpark",font="tohomo 20",bg="white",fg="black")
heading.pack(pady=15)




item_details=tk.Frame(window)
item_details.pack()

table=ttk.Treeview(item_details,columns=('item','quantity','price','total'),show='headings')
table.grid(row=3,column=0,columnspan=4,padx=10,pady=10)
table.heading("#1",text="Itemname")
table.heading("#2",text="Quantity")
table.heading("#3",text="Price")
table.heading("#4",text="Total")



for col in range(4):
    item_details.columnconfigure(col,minsize=150)

item_label=tk.Label(item_details,text="ItemName",font=("Arial",15),bg="white",fg="black")
item_label.grid(row=0,column=0)
quantity_label=tk.Label(item_details,text="Quantity",font=("Arial",15),bg="white",fg="black")
quantity_label.grid(row=0,column=1)
price_label=tk.Label(item_details,text="Price",font=("Arial",15),bg="white",fg="black")
price_label.grid(row=0,column=2)
total_label=tk.Label(item_details,text="Total",font=("Arial",15),bg="white",fg="black")
total_label.grid(row=0,column=3)

item_entry=tk.Entry(item_details,font=("Arial",15),width=10)
item_entry.grid(row=1,column=0)
quantity_entry=tk.Entry(item_details,font=("Arial",15),width=10,justify="right")
quantity_entry.grid(row=1,column=1)
price_entry=tk.Entry(item_details,font=("Arial",15),width=10,justify="right")
price_entry.grid(row=1,column=2)
total_entry=tk.Entry(item_details,font=("Arial",15),width=10,justify="right")
total_entry.grid(row=1,column=3)

calc_button=tk.Button(item_details,text="Calculate",font=("Arial",15),bg="blue",fg="white",command=calculate)
calc_button.grid(row=2,column=2,pady=10)
total_button=tk.Button(item_details,text="Total",font=("Arial",15),bg="blue",fg="white",command=total)
total_button.grid(row=2,column=3,padx=10,pady=10)
delete_button=tk.Button(item_details,text="DeleteItems",font=("Arial",15),bg="blue",fg="white",command=delete)
delete_button.grid(row=2,column=4,padx=10,pady=10)
clear_button = tk.Button(item_details, text="Clear Items", font=("Arial", 15), bg="blue", fg="white", command=clear)
clear_button.grid(row=2, column=5, padx=10, pady=10)

grand_total=tk.Label(window,text="Grandtotal:",font=("Arial",15),bg="green",fg="white")
grand_total.pack(pady=10)

addedlists=tk.Label(window,text="", font=("Arial",15))
addedlists.pack(pady=10)

window.mainloop()