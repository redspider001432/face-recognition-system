from tkinter import *
from time import strftime
from datetime import datetime
from tkinter import ttk, filedialog, messagebox

import os
import csv
import mysql.connector
from PIL import Image, ImageTk

myData = []


class AttendanceSystem:
    def __init__(self, root):
        self.root = root
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Attendance")
        self.root.resizable(False, False)


        # variables
        self.var_attID = StringVar()
        self.var_rollno = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_course = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_status = StringVar()

        attendanceFrame = Frame(self.root, width=790, height=700)
        attendanceFrame.grid(row=0, column=0, pady=60)
        attendanceLabelFrame = LabelFrame(attendanceFrame, bd=2, text="Entry Details", width=780, height=700,
                                          bg="white")
        attendanceLabelFrame.place(x=10, y=0)

        studentDetailFrame = Frame(self.root, width=700, height=700)
        studentDetailFrame.grid(row=0, column=1, pady=60, padx=35)
        studentDetailLabelFrame = LabelFrame(studentDetailFrame, width=720, height=700, text="Student Details",
                                             bg="white")
        studentDetailLabelFrame.place(x=0, y=0)

        # left frame

        bg_img = Image.open(r"./images/gateway.jpg")
        bg_img = bg_img.resize((350, 200))
        self.photoImage = ImageTk.PhotoImage(bg_img)

        imageLabel = Label(attendanceLabelFrame, image=self.photoImage, width=300, height=100)
        imageLabel.place(x=190, y=50)

        new_label = LabelFrame(attendanceLabelFrame,width=600,height=500,bg="white")
        new_label.place(x=0,y=220)

        attId = Label(new_label,text="Entry Id:",font=("times now roman",15),bg="white")
        attId.grid(pady=30,row=0,column=0)
        attEntry = ttk.Entry(new_label,font=("times now roman",13),textvariable=self.var_attID)
        attEntry.grid(row=0,column=1,padx=20)

        roll_no = Label(new_label,text="Roll NO:",font=("times now roman",15),bg="white")
        roll_no.grid(row=0,column=2)
        rollEntry = ttk.Entry(new_label,font=("times now roman",13),textvariable=self.var_rollno)
        rollEntry.grid(row=0,column=3,padx=20)

        name = Label(new_label, text="Name:", font=("times now roman", 15), bg="white")
        name.grid(row=1, column=0)
        nameEntry = ttk.Entry(new_label, font=("times now roman", 13),textvariable=self.var_name)
        nameEntry.grid(row=1, column=1, padx=20)

        Department = Label(new_label, text="Department:", font=("times now roman", 15), bg="white")
        Department.grid(row=1, column=2)
        DepartmentEntry = ttk.Entry(new_label, font=("times now roman", 13),textvariable=self.var_department)
        DepartmentEntry.grid(row=1, column=3, padx=20,pady=20)

        time = Label(new_label, text="Time:", font=("times now roman", 15), bg="white")
        time.grid(row=2, column=0)
        timeEntry = ttk.Entry(new_label, font=("times now roman", 13),textvariable=self.var_time)
        timeEntry.grid(row=2, column=1, padx=20,pady=20)

        date = Label(new_label, text="Date:", font=("times now roman", 15), bg="white")
        date.grid(row=2, column=2)
        dateEntry = ttk.Entry(new_label, font=("times now roman", 13),textvariable=self.var_date)
        dateEntry.grid(row=2, column=3, padx=20,pady=20)

        attStatus = Label(new_label,font=("times now roman", 15),text="Status:",bg="white")
        attStatus.grid(row=3,column=0,pady=20)
        attCombo = ttk.Combobox(new_label,state="readonly",font=("times now roman", 13),textvariable=self.var_status)
        attCombo["values"] = ("Present","Absent")
        attCombo.set("Select Status")
        attCombo.grid(row=3,column=1)


        saveButton = Button(new_label, text="Import CSV",width=14, font=('times now roman', 13, "bold"), bg="blue",
                            fg="white",command=self.importCSV)
        saveButton.grid(row=4, column=0,pady=10)

        updateButton = Button(new_label, text="Export CSV", width=14,font=('times now roman', 13, "bold"), bg="blue",
                              fg="white",command=self.exportCsv)
        updateButton.grid(row=4, column=1,pady=10)

        delButton = Button(new_label, text="Delete",width=14, font=('times now roman', 13, "bold"), bg="blue",
                           fg="white")
        delButton.grid(row=4, column=2,pady=10)


        resetButton = Button(new_label, text="Reset", width=14,font=('times now roman', 13, "bold"), bg="blue",
                             fg="white",command=self.reset)
        resetButton.grid(row=4, column=3,pady=10)

        # right frame

        tableFrame = Frame(studentDetailLabelFrame, bd=2, relief=RIDGE, bg="white")
        tableFrame.place(x=2, y=30, width=700, height=650)

        scrollBarX = ttk.Scrollbar(tableFrame, orient=HORIZONTAL)
        scrollBarY = ttk.Scrollbar(tableFrame, orient=VERTICAL)

        self.studentDetailsTable = ttk.Treeview(tableFrame, columns=("id","roll_no","name",
                                                                     "dep", "course","time","date","status"),
                                                xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)
        scrollBarX.pack(side=BOTTOM, fill=X)
        scrollBarY.pack(side=RIGHT, fill=Y)
        scrollBarX.config(command=self.studentDetailsTable.xview)
        scrollBarY.config(command=self.studentDetailsTable.yview)

        self.studentDetailsTable.heading("id", text="Attendance Id")
        self.studentDetailsTable.heading("roll_no", text="Roll NO")
        self.studentDetailsTable.heading("name", text="Name")
        self.studentDetailsTable.heading("dep", text="Department")
        self.studentDetailsTable.heading("course", text="Course")
        self.studentDetailsTable.heading("time", text="Time")
        self.studentDetailsTable.heading("date", text="Date")
        self.studentDetailsTable.heading("status", text="Status")
        self.studentDetailsTable["show"] = "headings"
        #
        self.studentDetailsTable.column("id", width=100)
        self.studentDetailsTable.column('roll_no', width=100)
        self.studentDetailsTable.column('name', width=100)
        self.studentDetailsTable.column('dep', width=120)
        self.studentDetailsTable.column('course', width=50)
        self.studentDetailsTable.column('time', width=60)
        self.studentDetailsTable.column('date', width=60)
        self.studentDetailsTable.column('status', width=60)
        self.studentDetailsTable.pack(fill=BOTH, expand=1)

        self.studentDetailsTable.bind("<ButtonRelease>",self.getCursor)

    def fetchData(self,rows):
        self.studentDetailsTable.delete(*self.studentDetailsTable.children)
        for i in rows:
            self.studentDetailsTable.insert("",END,values=i)

    def importCSV(self):
        global myData

        fileName = filedialog.askopenfilename(initialdir=os.getcwd(), title="Opening CSV", filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fileName) as myFile:
            csvread = csv.reader(myFile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)

    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("Error","No Data Found to export",parent=self.root)
                return False
            filename= filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(filename,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported", "Your data is exported in current working directory!!",parent=self.root)
        except Exception as error:
            messagebox.showerror("Error",str(error),parent=self.root)

    def getCursor(self, event=""):
        cursorFocus = self.studentDetailsTable.focus()
        content = self.studentDetailsTable.item(cursorFocus)
        data = content["values"]

        self.var_attID.set(data[0]),
        self.var_rollno.set(data[1]),
        self.var_name.set(data[2]),
        self.var_department.set(data[3]),
        self.var_course.set(data[4]),
        self.var_time.set(data[5]),
        self.var_date.set(data[6]),
        self.var_status.set(data[7]),

    def reset(self):
        self.var_attID.set(""),
        self.var_rollno.set(""),
        self.var_name.set(""),
        self.var_department.set(""),
        self.var_course.set(""),
        self.var_time.set(""),
        self.var_date.set(""),
        self.var_status.set("Select Status"),


if __name__ == "__main__":
    root = Tk()
    obj = AttendanceSystem(root)
    root.mainloop()
