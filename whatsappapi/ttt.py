import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

window=tk.Tk()
window.title("First tragon interview prepration begins")
window.geometry("600x400")
heading=tk.Label(window,text="Tkinter App",font="tohomo 20",bg="blue",fg="white")
heading.pack()






itemframe=tk.Frame(window)
itemframe.pack()
table=ttk.Treeview(itemframe,columns=('item','quantity','price','total'),show="headings")
table.grid(row=3,column=0,columnspan=4,padx=10,pady=10)
table.heading("#1",text="itemname")
table.heading("#2",text="quantity")
table.heading("#3",text="price")
table.heading("#4",text="total")



addlisteditems=[]
def calculation():
    itementryvalue=itementry.get()
    
    try:


        quantityentryvalue=float(quantityentry.get())
        priceentryvalue=float(priceentry.get())
        if not quantityentryvalue or not priceentryvalue<0:
            messagebox.showerror("e","e")
            return

    except ValueError:
        messagebox.showerror("error","error")
        return

    calculate=quantityentryvalue*priceentryvalue
    totalentry.delete(0,tk.END)
    

    totalentry.insert(0,f"{calculate:.2f}")

def total():
    grto=0
    itementryvalue=itementry.get()
    quantityentryvalue=quantityentry.get()
    priceentryvalue=priceentry.get()
    totalentryvalue=totalentry.get()

    table.insert('',tk.END,values=(itementryvalue,quantityentryvalue,priceentryvalue,totalentryvalue))
    itementry.delete(0,tk.END)
    quantityentry.delete(0,tk.END)
    priceentry.delete(0,tk.END)
    indt=0.0

    addlisteditems.append(itementryvalue)
    addlists.configure(text=f"{addlisteditems}")
    totalentry.delete(0,tk.END)
    
    for item in table.get_children():
        values=table.item(item,"values")
        valuesn=float(values[3])
        indt+=valuesn
    gtotal.configure(text=f"GT:{indt}")

    # for item in table.get_children():
    #     values=table.item(item,"values")
    #     valuesn=float(values[3])
    #     indt+=valuesn

def delete():
    selection=table.selection()
    if selection:

        table.delete(selection)


def clear():
    for item in table.get_children():
        table.delete(item)


for col in range(4):
    itemframe.columnconfigure(col,minsize=150)


itemlabel=tk.Label(itemframe,text="itemname",font=("Arial",15),bg="purple",fg="white")
itemlabel.grid(row=0,column=0,padx=10,pady=10)
quantitylabel=tk.Label(itemframe,text="quantity",font=("Arial",15),bg="purple",fg="white")
quantitylabel.grid(row=0,column=1,padx=10,pady=10)
pricelabel=tk.Label(itemframe,text="price",font=("Arial",15),bg="purple",fg="white")
pricelabel.grid(row=0,column=2,padx=10,pady=10)
totallabel=tk.Label(itemframe,text="total",font=("Arial",15),bg="purple",fg="white")
totallabel.grid(row=0,column=3,padx=10,pady=10)

itementry=tk.Entry(itemframe,font=("Arial",15),width=10)
itementry.grid(row=1,column=0,padx=10,pady=10)
quantityentry=tk.Entry(itemframe,font=("Arial",15),width=10,justify="right")
quantityentry.grid(row=1,column=1,padx=10,pady=10)
priceentry=tk.Entry(itemframe,font=("Arial",15),width=10,justify="right")
priceentry.grid(row=1,column=2,padx=10,pady=10)
totalentry=tk.Entry(itemframe,font=("Arial",15),width=10,justify="right")
totalentry.grid(row=1,column=3)

calc_button=tk.Button(itemframe,text="calculaed",font=("Arial",15),bg="blue",fg="white",command=calculation)
calc_button.grid(row=2,column=2,padx=10,pady=10)
total_button=tk.Button(itemframe,text="total",font=("Arial",15),bg="blue",fg="white",command=total)
total_button.grid(row=2,column=3,padx=10,pady=10)

delete_button=tk.Button(itemframe,text="delete",font=("Arial",15),bg="blue",fg="white",command=delete)
delete_button.grid(row=2,column=4,padx=10,pady=10)
clear_button=tk.Button(itemframe,text="clear",font=("Arial",15),bg="blue",fg="white",command=clear)
clear_button.grid(row=2,column=5,padx=10,pady=10)

gtotal=tk.Label(window,text="grandtotal",font=("Arial",15),bg="green",fg="white")
gtotal.pack(padx=10,pady=10)
addlists=tk.Label(window,text="",font=("Arial",15))
addlists.pack(pady=10)
window.mainloop()