from tkinter import *
import os
from PIL import ImageTk,Image
import sqlite3


con=sqlite3.Connection('DB')
cur=con.cursor()
cur.execute('create table if not exists Players (id varchar(20) PRIMARY KEY, fname varchar(20), lname varchar(20),dob date,passw varchar(20))')

def signback():
    root4.destroy()
    fpage()
def logback():
    log.destroy()
    fpage()
def login():
    first.destroy()
    global log
    log=Tk()
    global No,pas
    log.geometry("640x520")
    right=ImageTk.PhotoImage(Image.open("image/login.GIF"))
    Label(log,image=right).place(x=0,y=0)
    #Label(log,text="LOGIN",font=('Helvetica',20)).place(x=50,y=54)
    Label(log, text='User id. :',width=12,bg='green').place(x=200,y=420)
    No = Entry(log,bg='lightgreen')
    No.place(x=300,y=420)
    Label(log, text='Enter password:',width=12,bg='green').place(x=200,y=450)
    pas=Entry(log,show='*',bg='lightgreen')
    pas.place(x=300,y=450)
    Button(log,text="login",bg='green',command=logup,width=10).place(x=200,y=500)
    Button(log,text="back",bg='green',command=logback,width=10).place(x=300 ,y=500)
    log.mainloop()
def logup():
    user=('select * from Players where id= ? and passw =?')
    cur.execute(user,[(No.get()),(pas.get())])
    an=cur.fetchall()
    if an:
        #showinfo('well done!','you have successfully log in')
        log.destroy()
        starting()
    else :
        messagebox.showerror('ooopps !!','id and password did not match')
def signup():
    first.destroy()
    global root4,idNo,fname,lname,dob,password
    root4=Tk()
    root4.geometry('640x420')
    root4.config(bg='lightblue')
    right=ImageTk.PhotoImage(Image.open("image/signup.GIF"))
    Label(root4,image=right).place(x=0,y=0)
    Label(root4, text='user id :',width=10,bg='lightblue').place(x=400,y=100)
    idNo = Entry(root4,bg='grey')
    idNo.place(x=500,y=100)
    Label(root4, text='First name:',width=10,bg='lightblue').place(x=400,y=130)
    fname=Entry(root4,bg='grey')
    fname.place(x=500,y=130)
    Label(root4, text='Last name:',width=10,bg='lightblue').place(x=400,y=160)
    lname=Entry(root4,bg='grey')
    lname.place(x=500,y=160)
    Label(root4, text='D.O.B.',width=10,bg='lightblue').place(x=400,y=190)
    dob=Entry(root4,bg='grey')
    dob.place(x=500,y=190)
    Label(root4, text='password:',width=10,bg='lightblue').place(x=400,y=220)
    password=Entry(root4,show='*',bg='grey')
    password.place(x=500,y=220)
    Button(root4,text="submit",command=submit,width=10,bg='lightblue').place(x=400,y=250)
    Button(root4,text="back",command=signback,width=10,bg='lightblue').place(x=500,y=250)
    root4.mainloop()
def submit():
    l1=lname.get()
    f1=fname.get()
    user=('select * from Players where id= ? ')
    cur.execute(user,[idNo.get()])
    sign=cur.fetchall()
    if l1!=(lname.get()) or f1 !=str(fname.get()):
        messagebox.showerror('error','enter valid name')
    elif len(str(idNo.get()))==0 or len(str(fname.get()))==0 or len(str(lname.get()))==0 or len(str(password.get()))==0:
        messagebox.showinfo('error','enter a detail')
    elif len(dob.get().split('/'))!=3 or int(dob.get().split('/')[0])>31 or int(dob.get().split('/')[1])>12:
        messagebox.showerror('ERROR','Not a valid date of birth , or not a valid format')
    elif sign:
        messagebox.showinfo('sorryy!','user already exits')
    else :
        cur.execute('insert into Players values(?,?,?,?,?)',(idNo.get(),fname.get(),lname.get(),dob.get(),password.get()))
        con.commit()
        #root4.destroy()
        root4.destroy()
        starting()

def starting():
    import weather

    
def fpage():
    global first
    first=Tk()
    first.geometry('640x420')
    first.config(bg='lightblue')
    right=ImageTk.PhotoImage(Image.open("image/fro.GIF"))
    Label(first,image=right).place(x=0,y=0)
    Label(text="WEATHER FORECAST",bg="lightblue").place(x=250,y=30)
    Button(first,text='login',command=login,width=10,fg='red',bg='lightblue').place(x=100,y=400)
    Button(first,text='signup',command=signup,width=10,fg='red',bg='lightblue').place(x=500,y=400)
    first.mainloop()

fpage()
