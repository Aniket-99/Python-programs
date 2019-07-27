from tkinter import*
import time
import random
from tkinter import messagebox



#create new class RMS
class Main:
    def __init__(self):
        #configuration of root window
        self.root = Tk()
        self.screen_width=(self.root.winfo_screenwidth())-50
        self.screen_height=(self.root.winfo_screenheight())-100
        #self.root.geometry('{0}x{1}+0+0'.format(self.screen_width,self.screen_height))
        self.root.attributes("-fullscreen",True)
        self.root.title("Restaurant Management System")
        #root.resizable(width='enable',height='enable')
        self.header()
        self.body()
        self.footer()

#--------------------BACKEND------------------------
    def total(self):
        #-------Calculate Order No---------------
        orderno=random.randint(11111, 99999)
        self.v1.set(orderno)
        
        #-------Calculate Total Cost---------------
        Fries_Meal=30*(self.v2.get())
        Lunch_Meal=40*(self.v3.get())
        Burger_Meal=25*(self.v4.get())
        Pizza_Meal=40*(self.v5.get())
        Cheese_Burger=15*(self.v6.get())
        Drinks=10*(self.v7.get())
        items=[Fries_Meal,Lunch_Meal,Burger_Meal,Pizza_Meal,Cheese_Burger,Drinks]
        total=sum(items)
        self.v8.set('{0}₹'.format(total))
        
        #-------Calculate CGST AND SGST---------------
        cgst=(total*9)/100
        self.v9.set('{0}₹'.format(cgst))
        sgst=(total*9)/100
        self.v10.set('{0}₹'.format(sgst))

        #-------All Total Amt---------------
        all_total=total+cgst+sgst
        self.v11.set('{0}₹  => {1}₹'.format(all_total,round(all_total)))


    def reset(self):

        self.v1.set('')
        self.v2.set('')
        self.v3.set('')
        self.v4.set('')
        self.v5.set('')
        self.v6.set('')
        self.v7.set('')
        self.v8.set('')
        self.v9.set('')
        self.v10.set('')
        self.v11.set('')

    def consrtruction(self):
        messagebox.showinfo("Consrtruction", "Under Consrtruction!")
        
#--------------------FRONTEND------------------------
    def header(self):
        #-----RMS name with datetime-----
        top = Frame(self.root,width = self.screen_width,height=self.screen_height//6,relief=SUNKEN)
        top.pack(side=TOP)
        
        rms_label=Label(top,fg='green', font=( 'aria' ,30, 'bold' ),text="Restaurant Management System")
        rms_label.grid(pady=10)
        clock = Label(self.root, font=('times', 20, 'bold'), fg='dark green')
        clock.pack()
        def curr_time():
            time1 = ''
            time2 = time.strftime('%Y-%m-%d %H:%M:%S')
            if time2 != time1:
                time1 = time2
                clock.config(text=time2)
            clock.after(200, curr_time)
        curr_time()


    def body(self):
        self.bottom = Frame(self.root,width = self.screen_width,height=(self.screen_height)-(self.screen_height//6),relief=SUNKEN)
        self.bottom.pack(pady=25)
        #---------Order No--------------
        l1=Label(self.bottom, font=( 'arial' ,16, 'bold' ),text="Order No :",fg="#08CA60",bd=10,anchor='w')
        l1.grid(row=0,column=0,sticky=E)
        self.v1=IntVar()
        self.e1 = Entry(self.bottom,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg='#92E1B1' ,justify='right',width=25,textvariable=self.v1,relief=RIDGE,selectbackground='red')
        self.e1.grid(row=0,column=1)
        #---------Fries Meal--------------
        l2=Label(self.bottom, font=( 'arial' ,16, 'bold' ),text="Fries Meal  (₹30) :",fg="#08CA60",bd=10,anchor='nw')
        l2.grid(row=2,column=0,sticky=W)
        self.v2=IntVar()
        self.e2 = Entry(self.bottom,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v2,relief=RIDGE,selectbackground='red')
        self.e2.grid(row=2,column=1)
        #---------Lunch Meal--------------
        l3=Label(self.bottom, font=( 'arial' ,16, 'bold' ),text="Lunch Meal (₹40) :",fg="#08CA60",bd=10,anchor='w')
        l3.grid(row=3,column=0,sticky=E)
        self.v3=IntVar()
        self.e3 = Entry(self.bottom,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v3,relief=RIDGE,selectbackground='red')
        self.e3.grid(row=3,column=1)
        #---------Burger Meal--------------
        l4=Label(self.bottom, font=( 'arial' ,16, 'bold' ),text="Burger Meal (₹25) :",fg="#08CA60",bd=10,anchor='w')
        l4.grid(row=4,column=0,sticky=E)
        self.v4=IntVar()
        self.e4 = Entry(self.bottom,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v4,relief=RIDGE,selectbackground='red')
        self.e4.grid(row=4,column=1)
        #---------Pizza Meal--------------
        l5=Label(self.bottom, font=( 'arial' ,16, 'bold' ),text="Pizza Meal (₹40) :",fg="#08CA60",bd=10,anchor='w')
        l5.grid(row=5,column=0,sticky=E)
        self.v5=IntVar()
        self.e5 = Entry(self.bottom,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v5,relief=RIDGE,selectbackground='red')
        self.e5.grid(row=5,column=1)
        #---------Cheese Burger--------------
        l6=Label(self.bottom, font=( 'arial' ,16, 'bold' ),text="Cheese Burger (₹15) :",fg="#08CA60",bd=10,anchor='w')
        l6.grid(row=6,column=0,sticky=E)
        self.v6=IntVar()
        self.e6 = Entry(self.bottom,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v6,relief=RIDGE,selectbackground='red')
        self.e6.grid(row=6,column=1)
        #---------Drinks--------------
        l7=Label(self.bottom, font=( 'arial' ,16, 'bold' ),text="Drinks (₹10) :",fg="#08CA60",bd=10,anchor='w')
        l7.grid(row=7,column=0,sticky=E)
        self.v7=IntVar()
        self.e7 = Entry(self.bottom,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v7,relief=RIDGE,selectbackground='red')
        self.e7.grid(row=7,column=1)
        #-----------Calculate---------
        b1=Button(self.bottom,font=( 'arial' ,16, 'bold' ),text="CALCULATE",bg="#92E1B1",bd=10,width=15,command=self.total)
        b1.grid(row=8,column=1,pady=10)
        #-----------Reset---------
        b2=Button(self.bottom, font=( 'arial' ,16, 'bold' ),text="RESET",bg="#92E1B1",bd=10,command=self.reset)
        b2.grid(row=8,column=0,sticky=E,pady=10)
        

    def footer(self):
        self.bottom2= Frame(self.root,width = self.screen_width,height=self.screen_height-((self.screen_height)-(self.screen_height//6)),relief=SUNKEN)
        self.bottom2.pack(pady=25)
        #-----------Total Cost-------
        l8=Label(self.bottom2, font=( 'arial' ,16, 'bold' ),text="TOTAL COST :",fg="#08CA60",bd=10,anchor='w')
        l8.grid(row=0,column=0,sticky=E)
        self.v8=IntVar()
        self.e8 = Entry(self.bottom2,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v8,relief=RIDGE)
        self.e8.grid(row=0,column=1)
        #-----------CGST-------------
        l9=Label(self.bottom2, font=( 'arial' ,16, 'bold' ),text="CGST (9%) :",fg="#08CA60",bd=10,anchor='w')
        l9.grid(row=0,column=2,sticky=E)
        self.v9=IntVar()
        self.e9 = Entry(self.bottom2,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v9,relief=RIDGE)
        self.e9.grid(row=0,column=3)

        #-----------SGST-------------
        l10=Label(self.bottom2, font=( 'arial' ,16, 'bold' ),text="SGST (9%) :",fg="#08CA60",bd=10,anchor='w')
        l10.grid(row=0,column=4,sticky=E)
        self.v10=IntVar()
        self.e10 = Entry(self.bottom2,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v10,relief=RIDGE)
        self.e10.grid(row=0,column=5)
        #-----------All Total Amt-----
        l11=Label(self.bottom2, font=( 'arial' ,16, 'bold' ),text="ALL TOTAL AMT :",fg="#08CA60",bd=10,anchor='w')
        l11.grid(row=1,columnspan=4)
        self.v11=IntVar()
        self.e11 = Entry(self.bottom2,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',width=30,textvariable=self.v11,relief=RIDGE)
        self.e11.grid(row=1,columnspan=5,sticky=E,pady=15)
        #-----------Payment-------------
        self.b3=Button(self.bottom2, font=( 'arial' ,16, 'bold' ),text="PAYMENT",bg="#08CA60",bd=10,command=self.consrtruction)
        self.b3.grid(row=9,column=6,sticky=E)
        #-----------Exit-------------
        self.b3=Button(self.bottom2, font=( 'arial' ,16, 'bold' ),text="Exit",bg="#08CA60",bd=10,command=self.root.destroy,width=10)
        self.b3.grid(row=9,column=0,sticky=SE)
        


#call the class RMS
##app=RMS(root)
##root.mainloop()
Main()
