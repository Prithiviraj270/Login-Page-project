import tkinter as tk
from tkinter import messagebox,ttk
import pymysql
def reg():
    root = tk.Tk()
    root.geometry("1080x600")
    root.title("Registration")
    root.config(highlightcolor="Black", highlightthickness=7, background="white")
    nam = tk.Label(root, text="Name :", font=("Times", 18, "bold"), fg="Black", bg="White")
    nam.place(x=20, y=30)
    na = tk.Entry(root, font=("Times", 18, "italic"), width=15, relief="solid", bg="White", fg="black")
    na.place(x=300, y=30)
    fan = tk.Label(root, text="Father's Name :", font=("Times", 18, "bold"), fg="Black", bg="White")
    fan.place(x=20, y=90)
    fa = tk.Entry(root, font=("Times", 18, "italic"), width=15, relief="solid", bg="White", fg="black")
    fa.place(x=300, y=90)
    bg = tk.Label(root, text="Blood Group : ", font=("Times", 18, "bold"), fg="Black", bg="White")
    bg.place(x=20, y=150)
    bg1 = tk.Entry(root, font=("Times", 18, "italic"), width=15, relief="solid", bg="White", fg="black")
    bg1.place(x=300, y=150)
    var1 = tk.StringVar(root)
    gen = tk.Label(root, text="Gender : ", font=("Times", 18, "bold"), fg="Black", bg="White")
    gen.place(x=20, y=210)
    qua = tk.Label(root, text="Qualification : ", font=("Times", 18, "bold"), fg="Black", bg="White")
    qua.place(x=20, y=270)

    def sh():
        messagebox.showinfo("Gender", f"{var1.get()} is selected")

    rd = tk.Radiobutton(root, text="Male", font=("Times", 18, "bold"), fg="Black", bg="White", variable=var1,
                        value="Male", command=sh)
    rd.place(x=300, y=210)
    rd1 = tk.Radiobutton(root, text="Female", font=("Times", 18, "bold"), fg="Black", bg="White", variable=var1,
                         value="Female", command=sh)
    rd1.place(x=400, y=210)
    va = tk.StringVar(root)
    val = ("BE", "ME", "BCA", "BA", "MA")
    cm = ttk.Combobox(root, font=("Times", 18, "bold"), textvariable=va, values=val)
    cm.place(x=300, y=270)

    def st(args):
        messagebox.showinfo("Qulification", f"{va.get()} is selected")

    cm.bind("<<ComboboxSelected>>", st)
    var2 = tk.IntVar(root)

    def show():
        if var2.get() == 1:
            btn.config(state="normal")
        else:
            btn.config(state="disabled")

    ch = tk.Checkbutton(root, text="I have Check Above", font=("times", 19), command=show, variable=var2, onvalue=1,
                        offvalue=0)
    ch.place(x=300, y=330)

    def ins():
        name = na.get()
        fname = fa.get()
        blood = bg1.get()
        gender = var1.get()
        qull = va.get()
        mysql = pymysql.connect(host="localhost", user="root", password="root", database="records")
        mycursor = mysql.cursor()
        sql = "insert into info(name,fname,bg,gender,qull)values(%s,%s,%s,%s,%s)"
        val = (name, fname, blood, gender, qull)
        mycursor.execute(sql, val)
        mysql.commit()
        mysql.close()
        messagebox.showinfo("Records", f"{name} is Record Created!!")
        na.delete(0, tk.END)
        fa.delete(0, tk.END)
        bg1.delete(0, tk.END)
        na.focus_set()

    btn = tk.Button(root, text="Submit", font=("arial", 15, "bold"), width=12, relief="groove", bg="cyan", fg="black",
                    state="disabled", command=ins)
    btn.place(x=360, y=420)
    root.mainloop()
reg()