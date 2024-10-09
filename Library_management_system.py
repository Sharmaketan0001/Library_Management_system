from tkinter import *
from tkinter import ttk
import random 
import time
import datetime
from tkinter import messagebox
import tkinter.messagebox
import mysql.connector
import tkinter


class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")



        #===================================================Variable==========================================
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.Mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finallprice_var = StringVar()





        lbltitle = Label(self.root,text = "LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg = "green", bd = 20 , relief = RIDGE, font = ("times new roman",50 ,"bold"),padx = 2,pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief = RIDGE,padx = 20 ,bg = "Powder blue" )
        frame.place(x=0,y=130,width = 1530, height = 400)

        #======================================DataFrame Left ===================================
        DataFrameLeft=LabelFrame(frame,text = "Library Membership Information", bg="powder blue", fg = "green", bd = 12 , relief = RIDGE, font = ("times new roman",12 ,"bold"),padx = 2,pady=6)
        DataFrameLeft.place(x =0 , y=5, width=900, height = 350)

        lblMember= Label(DataFrameLeft,bg='powder blue', text="Member Type",font = ("times new roman", 13, "bold"),padx=2,pady=4)
        lblMember.grid(row=0,column=0,sticky=W) 

        comMember =ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font = ("arial",14 ,"bold"),width=27, background="powder blue", state='readonly')
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblPRN_NO= Label(DataFrameLeft,bg='powder blue', text="PRN No:", font = ("arial", 12, "bold"),padx=2,pady=6)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1 , column=1) 

        lblID_NO= Label(DataFrameLeft,bg='powder blue', text="ID No:", font = ("arial", 12, "bold"),padx=2,pady=6)
        lblID_NO.grid(row=2,column=0,sticky=W)
        ID_NO = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.id_var,width=29)
        ID_NO.grid(row=2 , column=1) 

        FIRST_name= Label(DataFrameLeft,bg='powder blue', text="First Name", font = ("arial", 12, "bold"),padx=2,pady=6)
        FIRST_name.grid(row=3,column=0,sticky=W)
        FIRST_name = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.firstname_var,width=29)
        FIRST_name.grid(row=3 , column=1) 

        LAST_name= Label(DataFrameLeft,bg='powder blue', text="Last Name", font = ("arial", 12, "bold"),padx=2,pady=6)
        LAST_name.grid(row=4,column=0,sticky=W)
        LAST_name = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.lastname_var,width=29)
        LAST_name.grid(row=4 , column=1) 

        Address_name1= Label(DataFrameLeft,bg='powder blue', text="Address 1", font = ("arial", 12, "bold"),padx=2,pady=6)
        Address_name1.grid(row=5,column=0,sticky=W)
        Address_name1 = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.address1_var,width=29)
        Address_name1.grid(row=5 , column=1) 

     
        Address_name2= Label(DataFrameLeft,bg='powder blue', text="Address 2", font = ("arial", 12, "bold"),padx=2,pady=6)
        Address_name2.grid(row=6,column=0,sticky=W)
        Address_name2 = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.address2_var,width=29)
        Address_name2.grid(row=6 , column=1) 

        Post_code= Label(DataFrameLeft,bg='powder blue', text="Post Code", font = ("arial", 12, "bold"),padx=2,pady=6)
        Post_code.grid(row=7,column=0,sticky=W)
        Post_code = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.postcode_var,width=29)
        Post_code.grid(row=7 , column=1) 

        Mobile= Label(DataFrameLeft,bg='powder blue', text="Mobile No:", font = ("arial", 12, "bold"),padx=2,pady=6)
        Mobile.grid(row=8,column=0,sticky=W)
        Mobile = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.Mobile_var,width=29)
        Mobile.grid(row=8 , column=1) 

        Book_id= Label(DataFrameLeft,bg='powder blue', text="Book Id:", font = ("arial", 12, "bold"),padx=4,pady=6)
        Book_id.grid(row=0,column=3,sticky=W)
        Book_id = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.bookid_var,width=29)
        Book_id.grid(row=0 , column=4) 

        Book_Title= Label(DataFrameLeft,bg='powder blue', text="Book Title:", font = ("arial", 12, "bold"),padx=4,pady=6)
        Book_Title.grid(row=1,column=3,sticky=W)
        Book_Title = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.booktitle_var,width=29)
        Book_Title.grid(row=1 , column=4) 

        Author_name= Label(DataFrameLeft,bg='powder blue', text="Author Name", font = ("arial", 12, "bold"),padx=4,pady=6)
        Author_name.grid(row=2,column=3,sticky=W)
        Author_name = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.author_var,width=29)
        Author_name.grid(row=2 , column=4) 

        
        Date_Borrowed= Label(DataFrameLeft,bg='powder blue', text="Date Borrowed", font = ("arial", 12, "bold"),padx=4,pady=6)
        Date_Borrowed.grid(row=3,column=3,sticky=W)
        Date_Borrowed = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.dateborrowed_var,width=29)
        Date_Borrowed.grid(row=3 , column=4)

        
        Date_Due= Label(DataFrameLeft,bg='powder blue', text="Date Due", font = ("arial", 12, "bold"),padx=4,pady=6)
        Date_Due.grid(row=4,column=3,sticky=W)
        Date_Due = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.datedue_var,width=29)
        Date_Due.grid(row=4 , column=4)

        
        Days_On_Book= Label(DataFrameLeft,bg='powder blue', text="Days on Book", font = ("arial", 12, "bold"),padx=4,pady=6)
        Days_On_Book.grid(row=5,column=3,sticky=W)
        Days_On_Book = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.daysonbook_var,width=29)
        Days_On_Book.grid(row=5 , column=4)

        Late_return_fine= Label(DataFrameLeft,bg='powder blue', text="Late Return Fine", font = ("arial", 12, "bold"),padx=4,pady=6)
        Late_return_fine.grid(row=6,column=3,sticky=W)
        Late_return_fine = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.latereturnfine_var,width=29)
        Late_return_fine.grid(row=6 , column=4)

        Date_over_Due= Label(DataFrameLeft,bg='powder blue', text="Date Over Due", font = ("arial", 12, "bold"),padx=4,pady=6)
        Date_over_Due.grid(row=7,column=3,sticky=W)
        Date_over_Due = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.dateoverdue_var,width=29)
        Date_over_Due.grid(row=7 , column=4)

        Actual_Price= Label(DataFrameLeft,bg='powder blue', text="Actual Price", font = ("arial", 12, "bold"),padx=4,pady=6)
        Actual_Price.grid(row=8,column=3,sticky=W)
        Actual_Price = Entry(DataFrameLeft, font =("arial", 13, "bold"),textvariable=self.finallprice_var,width=29)
        Actual_Price.grid(row=8 , column=4)




        #=====================================DataFRame Right ====================================
        DataFrameRight=LabelFrame(frame,text = "Book details", bg="powder blue", fg = "green", bd = 12 , relief = RIDGE, font = ("times new roman",12 ,"bold"),padx = 2,pady=6)
        DataFrameRight.place(x =910 , y=5, width=900, height = 350)


        self.txtBox = Text(DataFrameRight, font= ("arial", 12,"bold"), width = 32, height = 16, padx=2, pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollBar= Scrollbar(DataFrameRight)
        listScrollBar.grid(row = 0, column= 1, sticky="ns")


        listbooks = ["Head Firt Book","Structure and Interpretation of Computer Programs","The Pragmatic Programmer","Artificial Intelligence: A Modern Approach","Clean Code: A Handbook of Agile Software Craftsmanship","Computer Networking: Principles"," Protocols and Practice","The Mythical Man-Month: Essays on Software Engineering","Introduction to the Theory of Computation","Data Science for Business","Coders at Work: Reflections on the Craft of Programming"," Introduction to Computer Science Using Python","Code: The Hidden Language of Computer Hardware and Software","JavaScript: The Good Parts"," The Pragmatic Programmer","Modern Operating Systems","Introduction to Algorithms","Free Software, Free Society","The C++ Programming Language"," The Little Schemer","Computer Organization and Design"," Programming Pearls"]


        def SelectBook(event):
            selected = listBox.curselection() 
            value = str(listBox.get(selected)) 
            x = value
            if x == "Head Firt Book": 
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Mannual")
                self.author_var.set("Paul Berry")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
                self.datedue_var.set(d3.strftime("%Y-%m-%d"))
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdue_var.set("No")
                self.finallprice_var.set("Rs.788")





        listBox = Listbox(DataFrameRight,font=("arial", 12,"bold"), width = 32, height = 16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0,column =0 , padx = 4)
        listScrollBar.config(command=listBox.yview)

        for item in listbooks:
            listBox.insert(END, item)


       



        # ============================= Buttons Frame =======================================

        Framebutton = Frame(self.root, bd = 12, relief = RIDGE, padx = 20, bg= "powder blue")
        Framebutton.place(x =  0 , y = 530 , width = 1530, height = 70 )

        btnAddData = Button(Framebutton,command=self.add_data, text="Add Data", font =("aerial", 12,"bold"),width=23,bg="blue" , fg="white")
        btnAddData.grid(row=0, column=0)

        btnShowData = Button(Framebutton, command=self.showdata,text="Show Data", font =("aerial", 12,"bold"),width=23,bg="blue" , fg="white")
        btnShowData.grid(row=0, column=1)
        
        btnUpdateData = Button(Framebutton, command=self.update,text="Update", font =("aerial", 12,"bold"),width=23,bg="blue" , fg="white")
        btnUpdateData.grid(row=0, column=2)

        btnDeleteData = Button(Framebutton, command=self.delete,text="Delete", font =("aerial", 12,"bold"),width=23,bg="blue" , fg="white")
        btnDeleteData.grid(row=0, column=3)
        
        
        btnResetData = Button(Framebutton, command=self.reset,text="Reset", font =("aerial", 12,"bold"),width=23,bg="blue" , fg="white")
        btnResetData.grid(row=0, column=4)
        
        
        btnExitData = Button(Framebutton, command= self.Exit,text="Exit", font =("aerial", 12,"bold"),width=23,bg="blue" , fg="white")
        btnExitData.grid(row=0, column=5)


         # ============================= Informatiion Frame =======================================

        FrameDetails= Frame(self.root, bd = 12, relief = RIDGE, padx = 20, bg= "powder blue")
        FrameDetails.place(x =  0 , y = 590 , width = 1530, height = 70 )

        Table_frame = (FrameDetails)
        Table_frame.place(x =  0 , y =590 , width = 1460, height = 190 )

        xscroll = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column = ("membertype","prnno","title","firstName","lastName", "address1", "address2", "postid","mobile", "bookid","booktitle", "author","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice" ),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side =BOTTOM, fill =  X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command = self.library_table.yview)


        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="Reference No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstName",text="Firs tName")
        self.library_table.heading("lastName",text="Last Name")
        self.library_table.heading("address1",text="Address 1")
        self.library_table.heading("address2",text="Address 2")
        self.library_table.heading("postid",text="Post Id")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book Id")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days on Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Final Price")




        self.library_table["show"] ="headings"
        self.library_table.pack(fill=BOTH,expand =1 )

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstName",width=100)
        self.library_table.column("lastName",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        connection = mysql.connector.connect(host="localhost",username="root",password="9911288029", database="library_management_system")
        my_cursor = connection.cursor()
        my_cursor.execute("INSERT INTO Library (Member, PRN_NO, ID, FirstName, LastName, Address1, Address2, PostId, Mobile, BookId,Book_Title, Author, DateBorrowed, datedue, dayasofbook, Latereturnfine, dateoverdue, finalprice) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.Mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.finallprice_var.get()
            ))
        connection.commit()
        self.fetch_data()
        connection.close()

        messagebox.showinfo("Success","Member Has been inserted Successfully")


    def fetch_data(self):
        connection = mysql.connector.connect(host="localhost",username="root",password="9911288029", database="library_management_system")
        my_cursor = connection.cursor()
        my_cursor.execute("SELECT * FROM library")
        rows = my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values =i)
            connection.commit()
        connection.close()


    def get_cursor(self,event =""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row= content['values']
        
        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.Mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.author_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook_var.set(row[14])
        self.latereturnfine_var.set(row[15])
        self.dateoverdue_var.set(row[16])
        self.finallprice_var.set(row[17])

    def showdata(self):
        self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get() +"\n")
        self.txtBox.insert(END,"PRN No\t\t"+self.prn_var.get() +"\n")
        self.txtBox.insert(END,"ID No:-\t\t"+self.id_var.get() +"\n")
        self.txtBox.insert(END,"First Name\t\t"+self.firstname_var.get() +"\n")
        self.txtBox.insert(END,"Last Name\t\t"+self.lastname_var.get() +"\n")
        self.txtBox.insert(END,"Address1\t\t"+self.address1_var.get() +"\n")
        self.txtBox.insert(END,"Address2\t\t"+self.address2_var.get() +"\n")
        self.txtBox.insert(END,"Post Code\t\t"+self.postcode_var.get() +"\n")
        self.txtBox.insert(END,"Mobile No:-\t\t"+self.Mobile_var.get() +"\n")
        self.txtBox.insert(END,"Book ID: \t\t"+self.bookid_var.get() +"\n")
        self.txtBox.insert(END,"Book Title\t\t"+self.booktitle_var.get() +"\n")
        self.txtBox.insert(END,"Author\t\t"+self.author_var.get() +"\n")
        self.txtBox.insert(END,"Date Borrowed\t\t"+self.dateborrowed_var.get() +"\n")
        self.txtBox.insert(END,"Days On Book\t\t"+self.daysonbook_var.get() +"\n")
        self.txtBox.insert(END,"Late Rate Fine\t\t"+self.latereturnfine_var.get() +"\n")
        self.txtBox.insert(END,"Date Over Due\t\t"+self.datedue_var.get() +"\n")
        self.txtBox.insert(END,"Final Price\t\t"+self.finallprice_var.get() +"\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.Mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finallprice_var.set(""),
        self.txtBox.delete("1.0",END)


    def Exit(self):
        Exit =tkinter.messagebox.askyesno("Library Management System", "Do you want to Exit")
        if Exit>0:
            self.root.destroy()
            return


    def update(self):
        connection = mysql.connector.connect(host="localhost",username="root",password="9911288029", database="library_management_system")
        my_cursor = connection.cursor()
        my_cursor.execute("update library set Member=%s, PRN_NO=%s, ID=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, PostId=%s, Mobile=%s, BookId=%s,Book_Title=%s, Author=%s, DateBorrowed=%s, datedue=%s, dayasofbook=%s, Latereturnfine=%s, dateoverdue=%s, finalprice=%s where PRN_NO=%s",(
           
            self.member_var.get(),
            self.prn_var.get(), 
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.Mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.finallprice_var.get(),
            self.prn_var.get() 
        ))
        connection.commit()
        self.fetch_data()
        self.reset()
        connection.close()

        messagebox.showinfo("Success", "Member has been Updated")

    def delete(self):
        if(self.prn_var.get()=="" or self.id_var.get()==""):
            messagebox.showerror("Error","First Select the Member")
        else:
            connection = mysql.connector.connect(host="localhost",username="root",password="9911288029", database="library_management_system")
            my_cursor = connection.cursor()
            query ="delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)
            connection.commit()
            self.fetch_data() 
            self.reset()
            connection.close()

            messagebox.showinfo("Success","Member has been Deleted")          




if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()