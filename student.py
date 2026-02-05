import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

class std():
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        title = tk.Label(self.root, text="Student Record Management System", bd=4, relief="raised", bg="light blue", font=("Elephant", 40, "bold"))
        title.pack(side="top", fill="x")

        # option frame

        optFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(230,150,200))
        optFrame.place(width=self.width/3, height=self.height-180, x=50, y=100)

        addBtn = tk.Button(optFrame, command=self.addFrameFun, text="ADD STUDENT", bd=3, relief="raised", bg="light grey", width=20, font=("Arial", 20, "bold"))
        addBtn.grid(row=0, column=0, padx=30, pady=40)

        srchBtn = tk.Button(optFrame, command=self.srchFrameFun, text="SEARCH STUDENT", bd=3, relief="raised", bg="light grey", width=20, font=("Arial", 20, "bold"))
        srchBtn.grid(row=1, column=0, padx=30, pady=40)

        updBtn = tk.Button(optFrame, command=self.updFrameFun, text="UPDATE RECORD", bd=3, relief="raised", bg="light grey", width=20, font=("Arial", 20, "bold"))
        updBtn.grid(row=2, column=0, padx=30, pady=40)

        allBtn = tk.Button(optFrame, command=self.showAllFun, text="SHOW ALL", bd=3, relief="raised", bg="light grey", width=20, font=("Arial", 20, "bold"))
        allBtn.grid(row=3, column=0, padx=30, pady=40)

        delBtn = tk.Button(optFrame, command=self.delFrameFun, text="REMOVE STUDENT", bd=3, relief="raised", bg="light grey", width=20, font=("Arial", 20, "bold"))
        delBtn.grid(row=4, column=0, padx=30, pady=40)

        # detail frame

        self.detFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(150,230,120))
        self.detFrame.place(width=self.width/2+50, height=self.height-180 , x=self.width/3+100, y=100)

        lbl = tk.Label(self.detFrame, text="Record Details", font=("Arial", 30, "bold"), bg=self.clr(150,230,120))
        lbl.pack(side="top", fill="x")

        self.tabFun()

    def tabFun(self):
        tabFrame = tk.Frame(self.detFrame, bd=4, relief="sunken", bg="silver")
        tabFrame.place(width=self.width/2, height=self.height-280, x=23, y=70)

        x_scroll = tk.Scrollbar(tabFrame, orient="horizontal")
        x_scroll.pack(side="bottom", fill="x")

        y_scroll = tk.Scrollbar(tabFrame, orient="vertical")
        y_scroll.pack(side="right", fill="y")

        self.table = ttk.Treeview(tabFrame, xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, 
                                  columns=("std_id", "name", "dept", "course", "grade") )
        
        x_scroll.config(command=self.table.xview)
        y_scroll.config(command=self.table.yview)

        self.table.heading("std_id", text="STD ID")
        self.table.heading("name", text="Name") 
        self.table.heading("dept", text="Department")
        self.table.heading("course", text="Course")     
        self.table.heading("grade", text="Grade")

        self.table["show"] = "headings"
        
        self.table.pack(fill="both", expand=1)

    def addFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(150,180,250))
        self.addFrame.place(width=self.width/3, height=self.height-180, x=self.width/3+80, y=100)

        idLbl = tk.Label(self.addFrame, text="ID :", font=("Arial", 15, "bold"), bg=self.clr(150,180,250))
        idLbl.grid(row=0, column=0, padx=20, pady=30)
        self.idEnt = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
        self.idEnt.grid(row=0, column=1, padx=10, pady=30)

        nameLbl = tk.Label(self.addFrame, text="Name :", font=("Arial", 15, "bold"), bg=self.clr(150,180,250))
        nameLbl.grid(row=1, column=0, padx=20, pady=30)
        self.nameEnt = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
        self.nameEnt.grid(row=1, column=1, padx=10, pady=30)

        deptLbl = tk.Label(self.addFrame, text="Department :", font=("Arial", 15, "bold"), bg=self.clr(150,180,250))
        deptLbl.grid(row=2, column=0, padx=20, pady=30)
        self.deptEnt = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
        self.deptEnt.grid(row=2, column=1, padx=10, pady=30)

        courseLbl = tk.Label(self.addFrame, text="Course :", font=("Arial", 15, "bold"), bg=self.clr(150,180,250))
        courseLbl.grid(row=3, column=0, padx=20, pady=30)
        self.courseEnt = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
        self.courseEnt.grid(row=3, column=1, padx=10, pady=30)  

        gradeLbl = tk.Label(self.addFrame, text="Grade :", font=("Arial", 15, "bold"), bg=self.clr(150,180,250))
        gradeLbl.grid(row=4, column=0, padx=20, pady=30)
        self.gradeEnt = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
        self.gradeEnt.grid(row=4, column=1, padx=10, pady=30)   


        okBtn = tk.Button(self.addFrame, command=self.addFun, text="ENTER", bd=3, relief="raised", bg="light grey", width=20, font=("Arial", 20, "bold"))
        okBtn.grid(row=5, column=0, columnspan=30, padx=30, pady=30)

    def desAddFrame(self):
        self.addFrame.destroy()
    
    def addFun(self):
        id = self.idEnt.get()
        name = self.nameEnt.get()   
        dept = self.deptEnt.get()
        course = self.courseEnt.get()
        grade = self.gradeEnt.get()

        if id and name and dept and course and grade:
            stdID = int(id)
            try:
                self.dbFun()
                self.cur.execute("insert into student(std_id, name, dept, course, grade) values(%s, %s, %s, %s, %s)", (stdID, name, dept, course, grade))
                self.con.commit()
                tk.messagebox.showinfo("Success", f"Student {name} with ID {id} is Registered Successfully!")
                self.desAddFrame()

                self.cur.execute("select * from student where std_id=%s", (stdID))
                rows = self.cur.fetchone()
                self.table.delete(*self.table.get_children())
                self.table.insert("", tk.END, values=rows)

                self.con.close()

            except Exception as e:
                tk.messagebox.showerror("Error", f"Error due to {str(e)}")
                self.desAddFrame()

        else:
            tk.messagebox.showerror("Error", "Please fill all the fields")

    def srchFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(150,180,250))
        self.addFrame.place(width=self.width/3, height=self.height-350, x=self.width/3+80, y=100)

        optLbl = tk.Label(self.addFrame, text="ID :", font=("Arial", 15, "bold"), bg=self.clr(150,180,250))
        optLbl.grid(row=0, column=0, padx=20, pady=30)
        self.option = ttk.Combobox(self.addFrame, width=17, values=("std_id", "name", "course"), font=("Arial", 15, "bold") )
        self.option.set("Select Option")
        self.option.grid(row=0, column=1, padx=10, pady=30)

        valLbl = tk.Label(self.addFrame, text="Value :", font=("Arial", 15, "bold"), bg=self.clr(150,180,250))
        valLbl.grid(row=1, column=0, padx=20, pady=30)
        self.value = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
        self.value.grid(row=1, column=1, padx=10, pady=30) 

        okBtn = tk.Button(self.addFrame, command=self.srchFun, text="ENTER", bd=3, relief="raised", bg="light grey", width=20, font=("Arial", 20, "bold"))
        okBtn.grid(row=2, column=0, columnspan=30, padx=30, pady=30)

    def srchFun(self):
        opt = self.option.get()
        val = self.value.get()

        if opt == "std_id":
            ID = int(val)
            try:
                self.dbFun()
                self.cur.execute(f"select * from student where std_id=%s", ID)
                rows = self.cur.fetchone()
                self.table.delete(*self.table.get_children())
                self.table.insert("", tk.END, values=rows)

                self.desAddFrame()

                self.con.close()

            except Exception as e:
                tk.messagebox.showerror("Error", f"Error due to {str(e)}")

        else:
            try:
                self.dbFun()
                query = f"select * from student where {opt}=%s"
                self.cur.execute(query,(val))
                data = self.cur.fetchall()
                self.table.delete(*self.table.get_children())
                for i in data:
                    self.table.insert("", tk.END, values=i)

                self.desAddFrame()

                self.con.close()

            except Exception as e:
                tk.messagebox.showerror("Error", f"Error due to {str(e)}")
                 

    def dbFun(self):
        self.con = pymysql.connect(host="localhost", user="root", password="root", database="record")
        self.cur = self.con.cursor()

    def updFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(150,180,250))
        self.addFrame.place(width=self.width/3, height=self.height-300, x=self.width/3+80, y=100)

        optLbl = tk.Label(self.addFrame, text="ID :", font=("Arial", 15, "bold"), bg=self.clr(150,180,250))
        optLbl.grid(row=0, column=0, padx=20, pady=30)
        self.option = ttk.Combobox(self.addFrame, width=17, values=("name", "dept", "course", "grade"), font=("Arial", 15, "bold") )
        self.option.set("Select Option")
        self.option.grid(row=0, column=1, padx=10, pady=30)

        valLbl = tk.Label(self.addFrame, text="New_Value :", font=("Arial", 15, "bold"), bg=self.clr(150,180,250))
        valLbl.grid(row=1, column=0, padx=20, pady=30)
        self.value = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
        self.value.grid(row=1, column=1, padx=10, pady=30)

        idLbl = tk.Label(self.addFrame, text="Student ID :", font=("Arial", 15, "bold"), bg=self.clr(150,180,250))
        idLbl.grid(row=2, column=0, padx=20, pady=30)
        self.s_id = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
        self.s_id.grid(row=2, column=1, padx=10, pady=30) 

        okBtn = tk.Button(self.addFrame, command=self.updFun, text="ENTER", bd=3, relief="raised", bg="light grey", width=20, font=("Arial", 20, "bold"))
        okBtn.grid(row=3, column=0, columnspan=30, padx=30, pady=30)
    def updFun(self):
        opt = self.option.get()
        val = self.value.get()
        id = int(self.s_id.get())

        try:
            self.dbFun()
            query = f"update student set {opt}=%s where std_id=%s"
            self.cur.execute(query, (val, id))
            self.con.commit()
            tk.messagebox.showinfo("Success", f"Record Updated Successfully!")

            self.desAddFrame()

            self.cur.execute("select * from student where std_id=%s", (id))
            rows = self.cur.fetchone()

            self.table.delete(*self.table.get_children())
            self.table.insert("", tk.END, values=rows)


            self.con.close()

        except Exception as e:
            tk.messagebox.showerror("Error", f"Error due to {str(e)}")

    def showAllFun(self):
        try:    
            self.dbFun()
            self.cur.execute("select * from student")
            data = self.cur.fetchall()
            self.table.delete(*self.table.get_children())
            for i in data:
                self.table.insert("", tk.END, values=i)

            self.con.close()

        except Exception as e:
            tk.messagebox.showerror("Error", f"Error due to {str(e)}")

    def delFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(150,180,250))
        self.addFrame.place(width=self.width/3, height=self.height-400, x=self.width/3+80, y=100)

        idLbl = tk.Label(self.addFrame, text="ID :", font=("Arial", 15, "bold"), bg=self.clr(150,180,250))
        idLbl.grid(row=0, column=0, padx=20, pady=30)
        self.idEnt = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
        self.idEnt.grid(row=0, column=1, padx=10, pady=30)

        okBtn = tk.Button(self.addFrame, command=self.delFun, text="ENTER", bd=3, relief="raised", bg="light grey", width=20, font=("Arial", 20, "bold"))
        okBtn.grid(row=1, column=0, columnspan=30, padx=30, pady=30)

    def delFun(self):
        id = int(self.idEnt.get())
        try:
            self.dbFun()
            self.cur.execute("delete from student where std_id=%s", (id))
            self.con.commit() 
            tk.messagebox.showinfo("Success", f"Record Deleted Successfully!")

            self.desAddFrame()

            self.con.close()

        except Exception as e:
            tk.messagebox.showerror("Error", f"Error due to {str(e)}")

    def clr(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"
    

root = tk.Tk()
obj = std(root)
root.mainloop()