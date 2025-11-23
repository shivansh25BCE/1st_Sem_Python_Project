from tkinter import *
from tkinter import messagebox
from tkinter import ttk

window=Tk()
window.geometry("800x600")
window.title("Cafe Management System")
window.config(bg='#89CFF0')

window.resizable(0,0)
b=IntVar()
Title=Label(window,
      text='Cafe Management System',
      font=('ink free',30,'italic'),
      bg='#CCCCFF',
      fg='dark blue',
      relief=RAISED,
      bd=5)
Title.pack(side="top",fill=BOTH)  

Menu=Frame(window,
           bg='#a5f2f3',
           bd=5,
           relief=RAISED)
Menu.place(x=15,y=80,width=300,height=500)

menu ={"Pizza":150,
    "Burger":80,
    "Pasta":80,
    "Coffee":20,
    "Shake":140}


i1=Label(Menu,
         text="Pizza",
         bg="light blue",
         font=('ink free',20),
         relief=GROOVE,
         bd=5)
i1.grid(row=1,column=0,padx=10,pady=10)

g1=Label(Menu,
         text="150",
         bg="light blue",
         font=('ink free',20),
         relief=GROOVE,
         bd=5)
g1.grid(row=1,column=1,padx=10,pady=10)

i2=Label(Menu,
         text="Burger",
         bg="light blue",
         font=('ink free',20),
         relief=GROOVE,
         bd=5)
i2.grid(row=2,column=0,padx=10,pady=10)

g2=Label(Menu,
         text="80",
         bg="light blue",
         font=('ink free',20),
         relief=GROOVE,
         bd=5)
g2.grid(row=2,column=1,padx=10,pady=10)

i3=Label(Menu,
         text="Pasta",
         bg="light blue",
         font=('ink free',20),
         relief=GROOVE,
         bd=5)
i3.grid(row=3,column=0,padx=10,pady=10)

g3=Label(Menu,
         text="80",
         bg="light blue",
         font=('ink free',20),
         relief=GROOVE,
         bd=5)
g3.grid(row=3,column=1,padx=10,pady=10)

i4=Label(Menu,
         text="Coffee",
         bg="light blue",
         font=('ink free',20),
         relief=GROOVE,
         bd=5)
i4.grid(row=4,column=0,padx=10,pady=10)

g4=Label(Menu,
         text="20",
         bg="light blue",
         font=('ink free',20),
         relief=GROOVE,
         bd=5)
g4.grid(row=4,column=1,padx=10,pady=10)

i5=Label(Menu,
         text="Shake",
         bg="light blue",
         font=('ink free',20),
         relief=GROOVE,
         bd=5)
i5.grid(row=5,column=0,padx=10,pady=10)

g5=Label(Menu,
         text="140",
         bg="light blue",
         font=('ink free',20),
         relief=GROOVE,
         bd=5)
g5.grid(row=5,column=1,padx=10,pady=10)

Bill=Frame(window,
           bg='#a5f2f3',
           bd=5,
           relief=RAISED)
Bill.place(x=350,y=80,width=420,height=500)

  
option=Label(Bill,
             text="Choose::",
             bg="light blue",
             font=('ink free',20))
option.grid(row=0,column=0,padx=20,pady=20)

options=ttk.Combobox(Bill,width=10,font=('ink free',20),state="readonly")
options['values']=("Pizza","Burger","Pasta","Coffee","Shake")
options.grid(row=0,column=1,padx=5,pady=15)

quantity=Label(Bill,
             text="Quantity::",
             bg="light blue",
             font=('ink free',20))
quantity.grid(row=1,column=0,padx=20,pady=20)

Entry(Bill,bd=5,textvariable=b,width=10,font=('ink free',20)).grid(row=1,column=1,padx=20,pady=20)
data=[]
bill=Listbox(Bill,
             width=50,
             height=10,
             bg="white",
             fg="black",
             font=('ink free',10))
bill.grid(row=3,column=0,padx=30,pady=30,columnspan=5)

    
total=Listbox(Bill,
            width=5,
            height=2,
            bg="white",
            fg="black",
            font=('ink free',15,"bold"))
total.place(x=350,y=400)

def total_bill():
    if options.get()!="" and b.get()!=0:
        tot_bill=0
        item= options.get()
        quan= b.get()
    
        for i in menu:
            if item==i:
                amt= menu[i]*quan
                prt=f"Bill For {quan} {item} is: {amt}"
                data.append(amt)
                bill.insert(END,prt)
    elif options.get()=="":
        messagebox.showerror("Error","Please selece an item.")
    else:
        messagebox.showerror("Error","Please select a valid quantity.")

def tota():
    totalamt=0
    if data!=[]:
        for i in data:
            totalamt=totalamt+i
        total.insert(END,totalamt)    
    else:
        messagebox.showerror("Error","Please select items first.")
    
    

rec=Button(Bill,
       text="Add",
       font=('ink free',15,'italic'),
       bg="green",
       fg="white",
       command=total_bill,
       relief=RAISED,
       bd=5,
       padx=20)
rec.grid(row=4,column=0,padx=5,pady=5)

tot=Button(Bill,
       text="Total::₹",
       font=('ink free',15,'italic'),
       bg="green",
       fg="white",
       command=tota,
       relief=RAISED,
       bd=5,
       padx=20)
tot.grid(row=4,column=1,padx=5,pady=5)

window.mainloop()
        
    

