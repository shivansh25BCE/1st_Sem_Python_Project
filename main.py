from tkinter import *
from tkinter import messagebox
from tkinter import ttk
main=Tk()
main.geometry("500x500")
main.title("Main Menu")
main.config(bg='#89CFF0')
main.resizable(0,0)
menu ={"Pizza":150,
    "Burger":80,
    "Pasta":80,
    "Coffee":20,
    "Shake":140}

def user():
    main.withdraw()
    window=Toplevel(main)
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

    


    row_num = 1
    for item, price in menu.items():
        
        Label(Menu, text=item, bg="light blue",
              font=('ink free', 15), relief=GROOVE, bd=5).grid(row=row_num, column=0, padx=10, pady=10)
        
        
        Label(Menu, text=str(price), bg="light blue",
              font=('ink free', 15), relief=GROOVE, bd=5).grid(row=row_num, column=1, padx=10, pady=10)
        
        row_num += 1

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
    options['values'] = list(menu.keys())
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
        
    def close():
        window.destroy()
        main.deiconify()
    
    ex=Button(Bill,
           text="X",
           font=('ink free',15,'bold'),
           bg="red",
           fg="white",
           command=close,
           relief=RAISED,
           bd=5,
           padx=5)
    ex.grid(row=0,column=4,padx=5,pady=5)
    
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

MenuT=Label(main,
           text='Cafe Management System',
           font=('ink free',30,'italic'),
           bg='#CCCCFF',
           fg='dark blue',
           relief=RAISED,
           bd=5)
MenuT.pack(side="top",fill=BOTH)
    
                
 
    
user=Button(main,
           text="Order",
           font=('ink free',15,'italic'),
           bg="green",
           fg="white",
           command=user,
           relief=RAISED,
           bd=5,
           padx=20)
user.place(x=200,y=150)

def admin():
    main.withdraw()
    admin=Toplevel(main)
    admin.geometry("800x600")
    admin.title("ADMIN PANEl")
    admin.config(bg='#89CFF0')

    admin.resizable(0,0)

    
    name= StringVar()
    price= IntVar()
    frame= Frame(admin)
    frame.pack(side=RIGHT)

    x=Listbox(frame,
              font=('ink free',20),
              bg='#89CFF0',
              width=20,
              height=20,
              relief=RAISED,
              bd=15,
              borderwidth=20)

    x.pack(side=RIGHT,fill=BOTH)




    def select():
        if len(x.curselection())==0:
            messagebox.showerror("Select the name")
        else:
            ind=int(x.curselection()[0])
            items=list(menu.keys())
            return items[ind]

    def add():
        if name.get()!="" and price.get()!=0:
            
            menu[name.get()]=price.get()
            messagebox.showinfo("Confirmation","Successfully added new data")
            Select_set()
            
        else:
            messagebox.showerror("Error","Please enter data")
            
    def update():
        if name.get() and price.get():
            menu[name.get()]=price.get()
            messagebox.showinfo("Confirmation","Data has been updated")
            Select_set()    
        elif not(name.get()) and not(price.get()) and not(len(x.curselection())==0):
            messagebox.showerror("Error","Enter data")
        else:
            messagebox.showerror("Error","Select the data to be updated")

    def delete():
        temp= select()
        if temp!="":
            ans=messagebox.askyesno("Confirmation","Are you sure?")
            if ans==True:
                del menu[temp]
                Select_set()
        else:
            messagebox.showerror("Error","Select data")

    def view():
        temp=select()
        if temp!="":
            name.set(temp)
            price.set(menu[temp])
        
        else:
            messagebox.showerror("Error","Select data.;")

    def close():
        admin.destroy()
        main.deiconify()

    def Select_set() :
        x.delete(0,END)
        for name,price in menu.items():
            z=f"{name} :: {price}"
            x.insert (END, z)
    Select_set()


    n=Label(admin,
          text='Name',
          font=('ink free',20,'italic'),
          bg='#CCCCFF',
          fg='dark blue',
          relief=RAISED,
          bd=5)
    n.place(x=50,y=30)
    Entry(admin,textvariable=name,width=30).place(x=200,y=50)

    b=Label(admin,
          text='Price',
          font=('ink free',20,'italic'),
          bg='#CCCCFF',
          fg='dark blue',
          relief=RAISED,
          bd=5)
    b.place(x=50,y=80)
    Entry(admin,textvariable=price,width=30).place(x=200,y=100)


    Button(admin,
           text="Add Data",
           font=('ink free',15,'italic'),
           bg='#CCCCFF',
           fg='black',
           command=add,
           relief=RAISED,
           bd=5,
           padx=20).place(x=50,y=200)

    Button(admin,
           text="Update",
           font=('ink free',15,'italic'),
           bg='#CCCCFF',
           fg='black',
           command=update,
           relief=RAISED,
           bd=5,
           padx=20).place(x=50,y=250)

    Button(admin,
           text="Delete",
           font=('ink free',15,'italic'),
           bg='#CCCCFF',
           fg='black',
           command=delete,
           relief=RAISED,
           bd=5,
           padx=20).place(x=50,y=300)

    Button(admin,
           text="View",
           font=('ink free',15,'italic'),
           bg='#CCCCFF',
           fg='black',
           command=view,
           relief=RAISED,
           bd=5,
           padx=20).place(x=50,y=350)

    Button(admin,
           text="Exit",
           font=('ink free',15,'italic'),
           bg='red',
           fg='white',
           command=close,
           relief=RAISED,
           bd=5,
           padx=20).place(x=50,y=400)

    
user=Button(main,
           text="Admin",
           font=('ink free',15,'italic'),
           bg="green",
           fg="white",
           command=admin,
           relief=RAISED,
           bd=5,
           padx=20)
user.place(x=200,y=350)           
main.mainloop()        
