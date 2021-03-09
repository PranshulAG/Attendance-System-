from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database")
        self.root.geometry("1530x790+0+0")

        title = Label(self.root, text="Student Database", bd=10, relief=GROOVE, font=("times new roman", 40, "bold"),
                      bg="yellow", fg="blue")
        title.pack(side=TOP, fill=X)

        # all variables====================================================
        self.roll_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_var=StringVar()
        self.search_txt=StringVar()

        # frame=========================================

        frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        frame.place(x=10, y=90, width=550, height=680)
        m_title = Label(frame, text="Student Registration", bg="crimson", fg="white",
                        font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        roll = Label(frame, text="Roll No. :", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txtroll = Entry(frame, textvariable=self.roll_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txtroll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        name = Label(frame, text="Name:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txtname = Entry(frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txtname.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        email = Label(frame, text="E-Mail:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        email.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        txtemail = Entry(frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txtemail.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        gender = Label(frame, text="Gender:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        gender.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txtgender = ttk.Combobox(frame, textvariable=self.gender_var, width=19, font=("times new roman", 15, "bold"),
                                 state="readonly")
        txtgender['values'] = ["Male", "Female", "Other"]
        txtgender.grid(row=5, column=1, padx=20, pady=10)

        contact = Label(frame, text="Contact:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        contact.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txtcontact = Entry(frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5,
                           relief=GROOVE)
        txtcontact.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        dob = Label(frame, text="D.O.B:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        dob.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        txtdob = Entry(frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txtdob.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        add = Label(frame, text="Address:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        add.grid(row=8, column=0, pady=10, padx=20, sticky="w")
        self.txtadd = Text(frame, width=30, height=4, font=("", 10))
        self.txtadd.grid(row=8, column=1, pady=20, padx=20, sticky="w")

        btn = Frame(frame, bd=4, relief=GROOVE, bg="crimson", )
        btn.place(x=10, y=600, width=490)

        addbtn = Button(btn, text="ADD", width=13, pady=5, command=self.add_student)
        addbtn.grid(row=0, column=0, padx=10, pady=10)

        upbtn = Button(btn, text="UPDATE", width=13, pady=5, command=self.update_data)
        upbtn.grid(row=0, column=1, padx=10, pady=10)

        delbtn = Button(btn, text="DELETE", width=13, pady=5, command=self.delete_data)
        delbtn.grid(row=0, column=2, padx=10, pady=10)

        clbtn = Button(btn, text="CLEAR", width=13, pady=5, command=self.clear)
        clbtn.grid(row=0, column=3, padx=10, pady=10)

        # detail frame=====================================
        dt_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        dt_frame.place(x=600, y=90, width=900, height=680)

        lbsearch = Label(dt_frame, text="Search by", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbsearch.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        comlbsearch = ttk.Combobox(dt_frame,textvariable=self.search_var, width=10, font=("times new roman", 13, "bold"), state="readonly")
        comlbsearch['values'] = ["Roll No.", "Name", "Contact"]
        comlbsearch.grid(row=0, column=1, padx=20, pady=10)

        txtlbsearch = Entry(dt_frame,textvariable=self.search_txt, width=15, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txtlbsearch.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(dt_frame,command=self.search_data, text="SEARCH", width=13, pady=5)
        searchbtn.grid(row=0, column=3, padx=10, pady=10)

        showbtn = Button(dt_frame,command=self.fetch_data, text="SHOW ALL", width=13, pady=5)
        showbtn.grid(row=0, column=4, padx=10, pady=10)

        # table frame===========================================

        tb_frame = Frame(dt_frame, bd=4, relief=RIDGE, bg="crimson")
        tb_frame.place(x=10, y=65, width=870, height=594)

        scroll_x = Scrollbar(tb_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(tb_frame, orient=VERTICAL)

        self.st_table = ttk.Treeview(tb_frame, columns=("roll", "name", "email", "gender", "contact", "dob", "address"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.st_table.xview)
        scroll_y.config(command=self.st_table.yview)

        self.st_table.heading("roll", text="Roll No.")
        self.st_table.heading("name", text="Name")
        self.st_table.heading("email", text="E-mail")
        self.st_table.heading("gender", text="Gender")
        self.st_table.heading("contact", text="Contact")
        self.st_table.heading("dob", text="D.O.B")
        self.st_table.heading("address", text="Address")
        self.st_table['show'] = "headings"
        self.st_table.column("roll", width=120)
        self.st_table.column("name", width=100)
        self.st_table.column("email", width=100)
        self.st_table.column("gender", width=100)
        self.st_table.column("contact", width=100)
        self.st_table.column("dob", width=100)
        self.st_table.column("address", width=150)

        self.st_table.pack(fill=BOTH, expand=1)
        self.st_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def add_student(self):
        if self.roll_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All Fields Are Required!!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="fare")
            cur = con.cursor()
            cur.execute('insert into students values(%s,%s,%s,%s,%s,%s,%s)', (self.roll_var.get(),
                                                                              self.name_var.get(),
                                                                              self.email_var.get(),
                                                                              self.gender_var.get(),
                                                                              self.contact_var.get(),
                                                                              self.dob_var.get(),
                                                                              self.txtadd.get('1.0', END)
                                                                              ))

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record Inserted!")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="fare")
        cur = con.cursor()
        cur.execute('select * from students')
        rows = cur.fetchall()
        if len(rows) != 0:
            self.st_table.delete(*self.st_table.get_children())
            for row in rows:
                self.st_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.roll_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txtadd.delete("1.0", END)

    def get_cursor(self, ev):
        cursor_row = self.st_table.focus()
        content = self.st_table.item(cursor_row)
        row = content['values']
        self.roll_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txtadd.delete("1.0", END)
        self.txtadd.insert(END, row[6])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="fare")
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s, WHERE roll=%s",
                    (self.name_var.get(),
                     self.email_var.get(),
                     self.gender_var.get(),
                     self.contact_var.get(),
                     self.dob_var.get(),
                     self.txtadd.get('1.0', END),
                     self.roll_var.get()
                     ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="fare")
        cur = con.cursor()
        cur.execute('delete from students where roll=%s', self.roll_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="fare")
        cur = con.cursor()

        cur.execute('select * from students where'+str(self.search_var.get())+"Like '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.st_table.delete(*self.st_table.get_children())
            for row in rows:
                self.st_table.insert('', END, values=row)
            con.commit()
        con.close()


root = Tk()
ob = student(root)
root.mainloop()
