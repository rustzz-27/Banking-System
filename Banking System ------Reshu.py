#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import*
import os
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector


# In[ ]:


class bank_system:
    
    def register(self):
        #-------Register Screen----------
        register_screen=Toplevel(self.root)
        register_screen.title("Register")
        #-------------Declaring Variables----------------
        self.name_var=StringVar()
        self.age_var=StringVar()
        self.ac_var=StringVar()
        self.pass_var=StringVar()
        self.type_var=StringVar()
        self.amount_var=StringVar()
        #-------------LABELS------------
        t1=Label(register_screen,text="Please enter your details",font=("Calibri",15)).grid(row=0,pady=5)
        t2=Label(register_screen,text="Full Name",font=("Calibri",15)).grid(row=1,sticky=W)
        t3=Label(register_screen,text="Age",font=("Calibri",15)).grid(row=2,sticky=W)
        t4=Label(register_screen,text="Password",font=("Calibri",15)).grid(row=3,sticky=W)
        t5=Label(register_screen,text="Account Number",font=("Calibri",15)).grid(row=4,sticky=W)
        t6=Label(register_screen,text="Account Type[C/S]",font=("Calibri",15)).grid(row=5,sticky=W)
        t7=Label(register_screen,text="Amount",font=("Calibri",15)).grid(row=6,sticky=W)
        
        #------Entry Labels----------------
        E2=Entry(register_screen,textvariable=self.name_var,bd=5,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=10)
        E3=Entry(register_screen,textvariable=self.age_var,bd=5,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=10)
        E4=Entry(register_screen,show="*",textvariable=self.pass_var,bd=5,relief=GROOVE,font=("",15)).grid(row=3,column=1,padx=10)
        E4=Entry(register_screen,textvariable=self.ac_var,bd=5,relief=GROOVE,font=("",15)).grid(row=4,column=1,padx=10)
        E5=Entry(register_screen,textvariable=self.type_var,bd=5,relief=GROOVE,font=("",15)).grid(row=5,column=1,padx=10)
        E6=Entry(register_screen,textvariable=self.amount_var,bd=5,relief=GROOVE,font=("",15)).grid(row=6,column=1,padx=10)
        
        #--------Button---------------
        btn_reg=Button(register_screen,text="Register",width=14,font=("sans-serif",13),command=self.regbtn).grid(row=7,pady=5)
    def viewbal(self):
        viewbal_screen=Toplevel(self.login_session)
        viewbal_screen.title("Balance")
        conn = mysql.connector.connect(
            host="----",
            user="-----",
            passwd="",
            db="Bank")
        cur=conn.cursor(dictionary=True)
        cur.execute("SELECT Amount FROM Customers WHERE AC_Number = %s",(self.a_var.get(),))
        result=cur.fetchone()
        
        #---------Labels-----------
        b1=Label(viewbal_screen,text="Balance:"+" "+result["Amount"],font=("Calibri",15)).grid(row=1,padx=15,pady=15)
        
        conn.commit()
        conn.close()
    def withdr(self):
        conn = mysql.connector.connect(
            host="----",
            user="----",
            passwd="",
            db="Bank")
        cur=conn.cursor(dictionary=True)
        cur.execute("Select Amount from Customers WHERE AC_Number = %s",(self.a_var.get(),))
        result=cur.fetchone()
        d=result["Amount"]
        x=int(self.amt_var.get())
        d=int(d)-x
        y=str(d)
        cur.execute("UPDATE Customers SET Amount=%s WHERE AC_Number = %s",(y,self.a_var.get()))
        messagebox.showinfo("Successfull","Money WithDrawn")
        conn.commit()
        conn.close()
        
    def wd(self):
        wd_screen=Toplevel(self.login_session)
        wd_screen.title("Withdraw")
        
        #----------Declaring Variables----------
        self.amt_var=StringVar()
        
        #------Label---------
        w1=Label(wd_screen,text="Enter the amount:",font=("Calibri",15)).grid(row=1,pady=5)
        
        #---------Entry Label---------
        w_d1=Entry(wd_screen,textvariable=self.amt_var,bd=5,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=10)
        
        #-----------Button-------------
        b_wd=Button(wd_screen,text="WithDraw",width=14,font=("sans-serif",13),command=self.withdr).grid(row=2,pady=5)
        
    def findep(self):
        conn = mysql.connector.connect(
            host="----",
            user="----",
            passwd="",
            db="Bank")
        cur=conn.cursor(dictionary=True)
        cur.execute("Select Amount from Customers WHERE AC_Number = %s",(self.a_var.get(),))
        result=cur.fetchone()
        d=result["Amount"]
        x=int(self.amo_var.get())
        d=int(d)+x
        y=str(d)
        cur.execute("UPDATE Customers SET Amount=%s WHERE AC_Number = %s",(y,self.a_var.get()))
        messagebox.showinfo("Successfull","Money Credited")
        conn.commit()
        conn.close()
    def depo(self):
        depo_screen=Toplevel(self.login_session)
        depo_screen.title("Deposit")
        #-----_Declaring Varibales------
        self.amo_var=StringVar()
        #--------Label-------------
        d1=Label(depo_screen,text="Enter the amount:",font=("Calibri",15)).grid(row=1,pady=5)
        
        #---------Entry Label---------
        e_d1=Entry(depo_screen,textvariable=self.amo_var,bd=5,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=10)
        
        #-----------Button-------------
        b_dep=Button(depo_screen,text="Deposit",width=14,font=("sans-serif",13),command=self.findep).grid(row=2,pady=5)
        
        
    def login_session(self):
        self.login_session=Toplevel(self.login_screen)
        self.login_session.title("Actions")
        
        #-------Buttons-----------
        btn_bal=Button(self.login_session,text="View Balance",width=14,font=("sans-serif",13),command=self.viewbal).grid(row=1,pady=5)
        btn_Dep=Button(self.login_session,text="Deposit",width=14,font=("sans-serif",13),command=self.depo).grid(row=2,pady=5)
        btn_Wd=Button(self.login_session,text="WithDraw",width=14,font=("sans-serif",13),command=self.wd).grid(row=3,pady=5)
        
        
    def login(self):
        self.login_screen=Toplevel(self.root)
        self.login_screen.title("Login")

        #-----------Declaring Variables--------------
        self.a_var=StringVar()
        self.p_var=StringVar()
        
        #--------------Labels------------------------
        l1=Label(self.login_screen,text="Account Number",font=("Calibri",15)).grid(row=1,sticky=W)
        l2=Label(self.login_screen,text="Password",font=("Calibri",15)).grid(row=2,sticky=W)
        
        #--------------Entry Labels-----------------
        l_e1=Entry(self.login_screen,textvariable=self.a_var,bd=5,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=5)
        l_e2=Entry(self.login_screen,textvariable=self.p_var,show="*",bd=5,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=5)
        
        #------------Button--------------------
        btn_l=Button(self.login_screen,text="Login",width=14,font=("sans-serif",13),command=self.login_session).grid(row=3,pady=5)
        
        #--------Making details mandatory-----------------------
        if self.a_var.get()=="" or self.p_var.get()=="":
            messagebox.showerror("Alert","All fields are required!")
            
    def regbtn(self):
        conn = mysql.connector.connect(
            host="---",
            user="-----",
            passwd="",
            db="Bank")
        cur=conn.cursor()
        cur.execute("SELECT AC_Number FROM Customers WHERE AC_Number = %s",(self.ac_var.get(),))
        result=cur.fetchall()
        d=len(result)
        if d==1:
            messagebox.showwarning("Warning","Account already exists")
        
        elif d==0:
            cur.execute("INSERT INTO Customers VALUES(%s,%s,%s,%s,%s,%s)",(self.name_var.get(),self.age_var.get(),
                                                                       self.pass_var.get(),
                                                                       self.ac_var.get(),
                                                                       self.type_var.get(),
                                                                       self.amount_var.get()))
            messagebox.showinfo("Successful","Account Created")
        
        elif self.name_var.get()=="" or self.age_var.get()=="" or self.pass_var.get()=="" or self.ac_var.get()=="" or self.type_var.get()=="" or self.amount_var.get()=="":
            messagebox.showerror("Alert","All fields are required!")
        conn.commit()
        conn.close()
                                                                       
    def __init__(self,root):
        #-----Creating Frame----------
        self.root=root
        self.root.title("Banking App")
        #self.root.geometry('200x200')
        
        #--------Loading Images--------
        self.img=ImageTk.PhotoImage(Image.open("bank.jpg").resize((170,170)))
        
        #-------Labels----------------
        title=Label(self.root,text="BANKING SYSTEM",font=("Calibri",20,"bold","underline")).grid(row=0,sticky=N,pady=10)
        label_bg=Label(self.root,image=self.img).grid(row=2,sticky=N,pady=15)
        
        #------Buttons-------------
        btn_register=Button(self.root,text="Register",width=14,font=("sans-serif",13),command=self.register).grid(row=3,sticky=N)
        btn_login=Button(self.root,text="Login",width=14,font=("sans-serif",13),command=self.login).grid(row=4,sticky=N,pady=10)
        

root=Tk()
obj=bank_system(root)
root.mainloop()


# In[ ]:




