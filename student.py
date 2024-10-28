from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
class StudentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        title = Label(self.root, text="Student Details", font=("Tahoma", 20, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, width=1180, height=35)

        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_admission = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()


        lbl_roll = Label(self.root, text="Roll No.", font=("times new roman", 15, "bold"), bg="white")
        lbl_roll.place(x=10, y=60)
        
        lbl_name = Label(self.root, text="Name", font=("times new roman", 15, "bold"), bg="white")
        lbl_name.place(x=10, y=100)
        
        lbl_email = Label(self.root, text="Email", font=("times new roman", 15, "bold"), bg="white")
        lbl_email.place(x=10, y=140)
        
        lbl_gender = Label(self.root, text="Gender", font=("times new roman", 15, "bold"), bg="white")
        lbl_gender.place(x=10, y=180)
        lbl_state = Label(self.root, text="State", font=("times new roman", 15, "bold"), bg="white")
        lbl_state.place(x=10, y=220)
        txt_state = Entry(self.root, textvariable=self.var_state, font=("times new roman", 15, "bold"), bg="white")
        txt_state.place(x=150, y=220, width=150)
        lbl_city = Label(self.root, text="City", font=("times new roman", 15, "bold"), bg="white")
        lbl_city.place(x=320, y=220)
        txt_city = Entry(self.root, textvariable=self.var_city, font=("times new roman", 15, "bold"), bg="white")
        txt_city.place(x=380, y=220, width=100)
        lbl_pin = Label(self.root, text="Pin", font=("times new roman", 15, "bold"), bg="white")
        lbl_pin.place(x=510, y=220)
        txt_pin = Entry(self.root, textvariable=self.var_pin, font=("times new roman", 15, "bold"), bg="white")
        txt_pin.place(x=570, y=220, width=110)
        
        lbl_address = Label(self.root, text="Address", font=("times new roman", 15, "bold"), bg="white")
        lbl_address.place(x=10, y=260)

        

       

        # Separate creation and placement
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("times new roman", 15, "bold"), bg="white")
        self.txt_roll.place(x=150, y=60, width=200)
        
        txt_name = Entry(self.root, textvariable=self.var_name, font=("times new roman", 15, "bold"), bg="white")
        txt_name.place(x=150, y=100, width=200)
        
        txt_email = Entry(self.root, textvariable=self.var_email, font=("times new roman", 15, "bold"), bg="white")
        txt_email.place(x=150, y=140, width=200)
        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select","Male","female","Others") ,font=("times new roman", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)
        

        lbl_dob = Label(self.root, text="D.O.B", font=("times new roman", 15, "bold"), bg="white")
        lbl_dob.place(x=370, y=60)
        lbl_contact = Label(self.root, text="Contact", font=("times new roman", 15, "bold"), bg="white")
        lbl_contact.place(x=370, y=100)
        lbl_admission = Label(self.root, text="Admission", font=("times new roman", 15, "bold"), bg="white")
        lbl_admission.place(x=370, y=140)
        lbl_course = Label(self.root, text="Course", font=("times new roman", 15, "bold"), bg="white")
        lbl_course.place(x=370, y=180)


        self.course_list = ["Select"] 
        self.fetch_course()
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("times new roman", 15, "bold"), bg="white")
        txt_dob.place(x=480, y=60, width=200)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("times new roman", 15, "bold"), bg="white")
        txt_contact.place(x=480, y=100, width=200)
        txt_admission = Entry(self.root, textvariable=self.var_admission, font=("times new roman", 15, "bold"), bg="white")
        txt_admission.place(x=480, y=140, width=200)
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course,values= self.course_list,font=("times new roman", 15, "bold"), justify=CENTER)
        self.txt_course.place(x=480, y=180, width=200)
        self.txt_course.current(0)


        txt_state = Entry(self.root, textvariable=self.var_email, font=("times new roman", 15, "bold"), bg="white")
        txt_state.place(x=150, y=140, width=200)
        

        self.txt_address = Text(self.root, font=("times new roman", 15, "bold"), bg="white")
        self.txt_address.place(x=150, y=260, width=540, height=100)
        
        self.btn_add = Button(self.root, text = "Save", font = ("goudy old style", 15, "bold"), bg = "#2196f3", fg="white", cursor = "hand2", command=self.add).place(x=150, y=400, width=110, height=40)
        self.btn_update = Button(self.root, text = "Update", font = ("goudy old style", 15, "bold"), bg = "#4caf50", fg="white", cursor = "hand2", command= self.update).place(x=270, y=400, width=110, height=40)
        self.btn_delete = Button(self.root, text = "Delete", font = ("goudy old style", 15, "bold"), bg = "#f44336", fg="white", cursor = "hand2", command=self.delete ).place(x=390, y=400, width=110, height=40)
        self.btn_clear = Button(self.root, text = "Clear", font = ("goudy old style", 15, "bold"), bg = "#607d8b", fg="white", cursor = "hand2", command=self.clear).place(x=510, y=400, width=110, height=40)

        self.var_search = StringVar()
        lbl_search_roll = Label(self.root, text="Roll no.", font=("times new roman", 15, "bold"), bg="white").place(x=720, y=60)
        txt_search_roll = Entry(self.root, textvariable=self.var_search, font=("times new roman", 15, "bold"), bg="lightyellow").place(x=850, y=60, width=180)
        btn_search = Button(self.root, text = "Search", font = ("goudy old style", 15, "bold"), bg = "#2196f3", fg="white", cursor = "hand2", command=self.search).place(x=1050, y=58, width=120, height=28)
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)


        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("roll","Name", "Email", "Gender", "DOB", "Contact", "Admission","Course", "State", "City", "Pin", "Address"), xscrollcommand= scrollx.set, yscrollcommand= scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        
        self.CourseTable.heading("roll", text="roll")
        self.CourseTable.heading("Name", text="Name")
        self.CourseTable.heading("Email", text="Email")
        self.CourseTable.heading("Gender", text="Gender")
        self.CourseTable.heading("DOB", text="DOB")
        self.CourseTable.heading("Contact", text="Contact")
        self.CourseTable.heading("Admission", text="Admission")
        self.CourseTable.heading("Course", text="Course")
        self.CourseTable.heading("State", text="State")
        self.CourseTable.heading("City", text="City")
        self.CourseTable.heading("Pin", text="Pin")
        self.CourseTable.heading("Address", text="Address")

        self.CourseTable["show"] = "headings"
        self.CourseTable.column("roll", width=50)
        self.CourseTable.column("Name", width=100)
        self.CourseTable.column("Email", width=100)
        self.CourseTable.column("Gender", width=50)
        self.CourseTable.column("DOB", width=50)
        self.CourseTable.column("Contact", width=100)
        self.CourseTable.column("Admission", width=100)
        self.CourseTable.column("Course", width=100)
        self.CourseTable.column("State", width=100)
        self.CourseTable.column("City", width=100)
        self.CourseTable.column("Pin", width=50)
        self.CourseTable.column("Address", width=150)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        

    def delete(self):
        con = sqlite3.connect(database="lms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll no. should be required", parent = self.root)
            else:   
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()  
                if row == None:
                    messagebox.showerror("Error", "Please select student from the list", parent= self.root)
                else:
                    op =  messagebox.askyesno("Confirm", "Do you really want to delete?", parent = self.root)
                    if op == True:
                        cur.execute("delete from student where roll=?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Successfully Deleted Student", parent = self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
               
        


    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_admission.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.set("1.0", END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")



    def get_data(self, ev):
        self.txt_roll.config(state="readonly")
        self.txt_roll
        r = self.CourseTable.focus()
        content= self.CourseTable.item(r)
        row = content["values"]
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_admission.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.txt_address.set("1.0", END)
        self.txt_address.insert(END, row[11])






    def add(self):
        con = sqlite3.connect(database="lms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll no. should be required", parent = self.root)
            else:   
                cur.execute("select * from student where roll = ?", (self.var_roll.get(),))
                row = cur.fetchone()  
                if row != None:
                    messagebox.showerror("Error", "Roll no already present", parent= self.root)
                else:
                    cur.execute("insert into  student (roll, Name, Email, Gender, DOB, Contact, Admission, Course, State, City, Pin, Address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(self.var_roll.get(), self.var_name.get(), self.var_email.get(),self.var_gender.get(),self.var_dob.get(),self.var_contact.get(), self.var_admission.get(), self.var_course.get(), self.var_state.get(), self.var_city.get(), self.var_pin.get(), self.txt_address.get("1.0", END) ))
                    con.commit()
                    messagebox.showinfo("Success", "Student added  successfully", parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
   
    def update(self):
        con = sqlite3.connect(database="lms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", " Roll no iss required", parent = self.root)
            else:   
                cur.execute("select * from student where roll = ?", (self.var_roll.get(),))
                row = cur.fetchone()  
                if row == None:
                    messagebox.showerror("Error", "Select student from the list", parent= self.root)
                else:
                    cur.execute("update student set  Name=?, Email=?, Gender=?, DOB=?, Contact=?, Admission=?, Course=?, State=?, City=?, Pin=?, Address=? where roll=?", (self.var_name.get(), self.var_email.get(),self.var_gender.get(),self.var_dob.get(),self.var_contact.get(), self.var_admission.get(), self.var_course.get(), self.var_state.get(), self.var_city.get(), self.var_pin.get(), self.txt_address.get("1.0", END), self.var_roll.get()  ))
                    con.commit()
                    messagebox.showinfo("Success", "Student updated successfully", parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def fetch_course(self):
        con = sqlite3.connect(database="lms.db")
        cur = con.cursor()
        try:
            cur.execute("select name from course" )
            rows = cur.fetchall()  
            if len(rows)>0:
                for row in rows:
                     self.course_list.append(row[0])
                 
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def show(self):
        con = sqlite3.connect(database="lms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from student" )
            rows = cur.fetchall()  
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values= row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    
    def search(self):
        con = sqlite3.connect(database="lms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from student where roll=?", (self.var_search.get(),))
            row = cur.fetchone()  
            if row != None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('', END, values= row)
            else:
                messagebox.showerror("Error", "No record found", parent= self.root)       
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = StudentClass(root)
    root.mainloop()
