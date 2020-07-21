import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import sqlite3



root = tk.Tk()
root.title ('Stock Management System')
tabcontrol = ttk.Notebook(root)
Inventory = ttk.Frame(tabcontrol)
labelFrame = ttk.LabelFrame(Inventory,text="Inventory Management")
labelFrame.grid(column=0,row=0,padx=8,pady=4,sticky="N")



tabcontrol1 = ttk.Notebook(root)
Inventory1 = ttk.Frame(tabcontrol1)

labelFrame1 = ttk.LabelFrame(Inventory,text="product List", borderwidth=3)
#

labelFrame.grid(row=0,column=1, padx=8, pady=4, sticky="N")

Inventory1.pack()

#---------------------------------- Retrieval of Data ------------------------------------
# Create & Connect to db 



def Get_data():
	
	tree.delete(*tree.get_children())
	db = sqlite3.connect('Inventory_mgt.db')
	cursor = db.execute('select * from stock')
	for row in cursor:
		tree.insert('', 'end', text="Item_"+str(i), values=(row[0],row[1],row[2],row[3]))
		i=i+1

def Insert_data():
	db = sqlite3.connect('Inventory_mgt.db')
	db.execute('insert into stock (Product_Id,Product_Name,Sell_Price,Quantity) values (?,?,?,?)',[PRODUCT_ID_VALUE.get(),PRODUCT_NAME_VALUE.get(),PRODUCT_PRICE_VALUE.get(),PRODUCT_QUANTITY_VALUE.get()])
	db.commit()

def Update_data():
	db = sqlite3.connect('Inventory_mgt.db')
	db.execute('update stock set Product_Id = ? ,Product_Name = ?,Sell_Price = ?,Quantity = ?  where Product_Id = ?',(PRODUCT_ID_VALUE.get(),PRODUCT_NAME_VALUE.get(),PRODUCT_PRICE_VALUE.get(),PRODUCT_QUANTITY_VALUE.get(),PRODUCT_ID_VALUE.get()))
	db.commit()

def Delete_data():
	db = sqlite3.connect('Inventory_mgt.db')
	db.execute('delete from stock where Product_Id = ?',(PRODUCT_ID_VALUE.get(),))
	db.commit()


#----------------------- Tree View -------------------------------------------

tree = ttk.Treeview(labelFrame1, columns=('Product Id', 'Product Name','Price','Quantity'),height=20)
tree.place(x=30, y=95)
vsb = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
vsb.place(x=30+954+5, y=0, height=200+220)

tree.configure(yscrollcommand=vsb.set)
tree.heading('#0', text='Item no.')
tree.heading('#1', text='Product id')
tree.heading('#2', text='Name')
tree.heading('#3', text='Price')
tree.heading('#4', text='Quantity')
tree.column('#1', stretch=tk.YES)
tree.column('#2', stretch=tk.YES)
tree.column('#0', stretch=tk.YES)
tree.column('#3', stretch=tk.YES)
tree.column('#4', stretch=tk.YES)
tree.grid(row=11, columnspan=4, sticky='nsew')
tabcontrol1.pack(expand=0,fill="both")



global PRODUCT_QUANTITY_VALUE
global PRODUCT_ID_VALUE
global PRODUCT_PRICE_VALUE
global PRODUCT_NAME_VALUE



PRODUCT_ID_VALUE = tk.StringVar()
PRODUCT_NAME_VALUE = tk.StringVar()
PRODUCT_PRICE_VALUE = tk.StringVar()
PRODUCT_QUANTITY_VALUE = tk.StringVar()

productId = ttk.Label(labelFrame,text="Product ID: ")
productIdEntry = ttk.Entry(labelFrame,textvariable=PRODUCT_ID_VALUE)
productIdEntry.grid(column=0,row=1,sticky='W')

productName = ttk.Label(labelFrame,text="Product Name : ")
#productName.config(font=("Courier",15))
productNameEntry = ttk.Entry(labelFrame,textvariable=PRODUCT_NAME_VALUE)
#productNameEntry.config(font=("Courier",20))

productPrice = ttk.Label(labelFrame,text="Sell Price : ")
#productPrice.config(font=("Courier",15))

productPriceEntry = ttk.Entry(labelFrame,textvariable=PRODUCT_PRICE_VALUE)
#productPriceEntry.config(font=("Courier",20))
productPriceEntry.grid(column=0,row=5,sticky='W')

productQuantity = ttk.Label(labelFrame,text="Quantity : ")
#productQuantity.config(font=("Courier",15))
productQuantityEntry = ttk.Entry(labelFrame,textvariable=PRODUCT_QUANTITY_VALUE)
#productQuantityEntry.config(font=("Courier",20))
productQuantityEntry.grid(column=0,row=7,sticky="W")

InsertButton = ttk.Button(labelFrame,text='Insert',command=Insert_data)
ShowButton = ttk.Button(labelFrame,text='Show',command=Get_data)


style = ttk.Style()
style.configure('TButton', background='#3498db')


UpdateButton = ttk.Button(labelFrame,text='Update',command=Update_data,width=20)
DeleteButton = ttk.Button(labelFrame,text='Delete',command=Delete_data,width=20)
DeleteButton.grid(column=0,row=11,sticky='W',pady=7)
UpdateButton.grid(column=0,row=10,sticky='W')
ShowButton.grid(column=0,row=8,sticky='E')
InsertButton.grid(column=0,row=8,sticky='W',pady=7)
productQuantity.grid(column=0,row=6,sticky="W")
productPrice.grid(column=0,row=4,sticky='W')
productNameEntry.grid(column=0,row=3,sticky='W')
productName.grid(column=0,row=2,sticky='W')
productId.grid(column=0,row=0,sticky='W')
tabcontrol.add(Inventory,text='Inventory')
tabcontrol.pack(expand=1,fill="both")





root.mainloop()
