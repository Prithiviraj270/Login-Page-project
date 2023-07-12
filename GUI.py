import tkinter as tk
import pymysql
from tkinter import messagebox
import log as l
import LB

base = tk.Tk()
base.geometry("700x700")
base.title("LOGIN PAGE")
base.config(background="black",highlightcolor="pink",highlightthickness=10)
can = tk.Canvas(base,width=500,height=500,background="white",highlightbackground="red",highlightthickness=5)
can.place(x=470,y=160)
tit = tk.Label(base,text="LOGIN PAGE",font=("Block Font",30),fg="white",bg="black" ,relief="solid",width=15)
tit.place(x=550,y=50)
o = tk.Label(can,text="WELCOME!!!",font=("Times New Roman",20,"bold"),bg="grey",fg="Black",relief="groove")
o.place(x=150,y=50)
n = tk.Label(can,text="USER ID :",font=("Times New Roman",20,"bold"),bg="cyan",fg="Black",relief="groove")
n.place(x=60,y=150)
m = tk.Label(can,text="PASSWORD :",font=("Times New Roman",20,"bold"),bg="cyan",fg="Black",relief="groove")
m.place(x=60,y=250)
nam = tk.Entry(can,font=("Times",20,"italic"),width=15,relief="groove",bg="cyan",fg="black")
nam.place(x=250,y=150)
pas = tk.Entry(can,font=("Times",20,"italic"),width=15,relief="groove",bg="cyan",fg="black",show="*")
pas.place(x=250,y=250)
def log():
    mysql=pymysql.connect(host="localhost", user="root", password="root", database="records")
    mycuror=mysql.cursor()
    sql="select Uname,Password from user where Uname=%s and Password=%s"
    val=(nam.get(),pas.get())
    mycuror.execute(sql,val)
    ans=mycuror.fetchone()
    if ans==None:
        messagebox.showerror("Loign","Login Failed")
    else:
        messagebox.showinfo("Login","Login Successfully")

btn = tk.Button(can,text="Login",font=("arial",15,"bold"),width=12,relief="groove",bg="cyan",fg="black",command=log)
btn.place(x=280,y=400)
def new():
    LB.nr()
btn1 = tk.Button(can,text="NewUser",font=("arial",15,"bold"),width=12,relief="groove",bg="cyan",fg="black",command=new)
btn1.place(x=80,y=400)
var=tk.IntVar()
def show():
    if var.get()==1:
        pas.config(show="")
    elif var.get()==0:
        pas.config(show="*")
ch=tk.Checkbutton(can,text="Show Password",font=("times",18,"italic"),variable=var,onvalue=1,offvalue=0,command=show)
ch.place(x=280,y=320)

base.mainloop()