import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyttsx3
import cv2
import mysql.connector


class studentDetails:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Attendance")

        # variables
        self.var_ID = StringVar()
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_rollNO = StringVar()
        self.var_Name = StringVar()
        self.var_hodName = StringVar()
        self.var_floor = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_gender = StringVar()
        self.var_radio = StringVar()

        labelledTitle = Label(self.root, text="Student Details", font=("times new roman", 35, "bold"),
                              bg="white", fg="red")
        labelledTitle.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=800)

        # LHS
        leftFrame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                               font=("times new roman", 12, "bold"))
        leftFrame.place(x=30, y=30, width=660, height=600)

        current_department = LabelFrame(leftFrame, bd=2, bg="white", relief=RIDGE, text="Current Department")
        current_department.place(x=5, y=100, width=650, height=150)

        departmentLabel = Label(current_department, text="Department", font=("times new roman", 12, "bold"), bg="white")
        departmentLabel.grid(row=0, column=0, padx=10, sticky=W)

        departmentCombo = ttk.Combobox(current_department, font=("times new roman", 12, "bold"), state="readonly",
                                       textvariable=self.var_dep)
        departmentCombo["values"] = ("Select Department", "Engineering", "Hotel Management", "Architecture", "Business")
        departmentCombo.current(0)
        departmentCombo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course Labels
        courseLabel = Label(current_department, text="Course", font=("times new roman", 12, "bold"), bg="white")
        courseLabel.grid(row=0, column=2, padx=10, sticky=W)

        courseCombo = ttk.Combobox(current_department, font=("times new roman", 12, "bold"), state="readonly",
                                   textvariable=self.var_course)
        courseCombo["values"] = ("Select Course", "BTech", "BCA", "BArhc", "Bsc", "BBA", "MBA")
        courseCombo.current(0)
        courseCombo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year Labels
        yearLabel = Label(current_department, text="Year", font=("times new roman", 12, "bold"), bg="white")
        yearLabel.grid(row=1, column=0, padx=20, sticky=W)

        yearCombo = ttk.Combobox(current_department, font=("times new roman", 12, "bold"), state="readonly",
                                 textvariable=self.var_year)
        yearCombo["values"] = ("Select Year", "1", "2", "3", "4")
        yearCombo.current(0)
        yearCombo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester Labels
        semLabel = Label(current_department, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semLabel.grid(row=1, column=2, padx=10, sticky=W)

        semCombo = ttk.Combobox(current_department, font=("times new roman", 12, "bold"), state="readonly",
                                textvariable=self.var_semester)
        semCombo["values"] = ("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8")
        semCombo.current(0)
        semCombo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Information
        studentInformation = LabelFrame(leftFrame, bd=2, bg="white", relief=RIDGE, text="Information")
        studentInformation.place(x=5, y=250, width=650, height=320)

        studentID = Label(studentInformation, text="ID:", font=("times new roman", 12, "bold"), bg="white")
        studentID.grid(row=0, column=0, padx=10, sticky=W)

        idEntry = ttk.Entry(studentInformation, width=20, font=('times now roman', 13, "bold"),
                            textvariable=self.var_ID)
        idEntry.grid(row=0, column=1, padx=10, sticky=W)

        studentName = Label(studentInformation, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        studentName.grid(row=0, column=2, padx=10, sticky=W)

        nameEntry = ttk.Entry(studentInformation, width=20, font=('times now roman', 13, "bold"),
                              textvariable=self.var_Name)
        nameEntry.grid(row=0, column=3, padx=10, sticky=W)

        classFloor = Label(studentInformation, text="Building Floor:", font=("times new roman", 12, "bold"), bg="white")
        classFloor.grid(row=1, column=0, pady=10, sticky=W)

        floorEntry = ttk.Entry(studentInformation, width=20, font=('times now roman', 13, "bold"),
                               textvariable=self.var_floor)
        floorEntry.grid(row=1, column=1, pady=20, padx=10, sticky=W)

        hodName = Label(studentInformation, text="HOD Name:", font=("times new roman", 12, "bold"), bg="white")
        hodName.grid(row=1, column=2, pady=10, sticky=W)

        hodEntry = ttk.Entry(studentInformation, width=20, font=('times now roman', 13, "bold"),
                             textvariable=self.var_hodName)
        hodEntry.grid(row=1, column=3, pady=20, padx=10, sticky=W)

        gender = Label(studentInformation, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender.grid(row=2, column=0, pady=10, sticky=W)

        genderEntry = ttk.Combobox(studentInformation, font=('times now roman', 12), state="readonly",
                                   textvariable=self.var_gender)
        genderEntry["values"] = ("Select Gender", "Male", "Female")
        genderEntry.current(0)
        genderEntry.grid(row=2, column=1, pady=10, padx=10, sticky=W)

        rollNo = Label(studentInformation, text="Roll NO:", font=("times new roman", 12, "bold"), bg="white")
        rollNo.grid(row=2, column=2)
        rollNoEntry = ttk.Entry(studentInformation, width=20, font=('times now roman', 13, "bold"),
                                textvariable=self.var_rollNO)
        rollNoEntry.grid(row=2, column=3, sticky=W)

        address = Label(studentInformation, text="Address:", font=("times new roman", 12, "bold"), bg="white")
        address.grid(row=3, column=0, pady=10, sticky=W)

        addEntry = ttk.Entry(studentInformation, width=20, font=('times now roman', 13, "bold"),
                             textvariable=self.var_address)
        addEntry.grid(row=3, column=1, pady=20, padx=10, sticky=W)

        phone = Label(studentInformation, text="PhoneNo:", font=("times new roman", 12, "bold"), bg="white")
        phone.grid(row=3, column=2, pady=10, sticky=W)

        phoneEntry = ttk.Entry(studentInformation, width=20, font=('times now roman', 13, "bold"),
                               textvariable=self.var_phone)
        phoneEntry.grid(row=3, column=3, pady=20, padx=10, sticky=W)

        radioButton1 = ttk.Radiobutton(studentInformation, text="Take photo sample", value="Yes",
                                       variable=self.var_radio)
        radioButton1.grid(row=4, column=0)

        radioButton2 = ttk.Radiobutton(studentInformation, text="No photo sample", value="No", variable=self.var_radio)
        radioButton2.grid(row=4, column=1)

        btnFrame = Frame(studentInformation, bd=2, relief=RIDGE, bg="white")
        btnFrame.place(x=0, y=230, width=645, height=35)

        saveButton = Button(btnFrame, text="Save", width=15, font=('times now roman', 13, "bold"), bg="blue",
                            fg="white", command=self.addData)
        saveButton.grid(row=0, column=1)

        delButton = Button(btnFrame, text="Delete", width=15, font=('times now roman', 13, "bold"), bg="blue",
                           fg="white", command=self.deleteDetails)
        delButton.grid(row=0, column=2)

        updateButton = Button(btnFrame, text="Update", width=15, font=('times now roman', 13, "bold"), bg="blue",
                              fg="white", command=self.updateDetails)
        updateButton.grid(row=0, column=3)

        resetButton = Button(btnFrame, text="Reset", width=15, font=('times now roman', 13, "bold"), bg="blue",
                             fg="white", command=self.resetDetails)
        resetButton.grid(row=0, column=4)

        btnFrame1 = Frame(studentInformation, bd=2, relief=RIDGE, bg="white")
        btnFrame1.place(x=0, y=265, width=645, height=35)

        takePhotoButton = Button(btnFrame1, text="Take Photo", width=32, font=('times now roman', 13, "bold"),
                                 bg="blue",
                                 fg="white", command=self.generateData)
        takePhotoButton.grid(row=0, column=0)

        updatePhotoButton = Button(btnFrame1, text="Update Photo", width=32, font=('times now roman', 13, "bold"),
                                   bg="blue",
                                   fg="white")
        updatePhotoButton.grid(row=0, column=1)
        # RHS
        rightFrame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        rightFrame.place(x=800, y=30, width=660, height=580)

        # searching query
        searchFrame = LabelFrame(rightFrame, bd=2, relief=RIDGE, text="Search Query",
                                 font=("times new roman", 12, "bold"), bg="white")
        searchFrame.place(x=5, y=150, width=650, height=70)

        searchLabel = Label(searchFrame, text="Search By:", font=("times new roman", 15, "bold"), bg="green",
                            fg="white")
        searchLabel.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        searchCombo = ttk.Combobox(searchFrame, font=("times new roman", 12), state="readonly", width=15)
        searchCombo["values"] = ("Select", "ID", "PhoneNo")
        searchCombo.current(0)
        searchCombo.grid(row=0, column=1)

        searchEntry = ttk.Entry(searchFrame, width=15, font=("times now roman", 12))
        searchEntry.grid(row=0, column=2, padx=10)

        searchButton = Button(searchFrame, width=12, text="Search", bd=2, bg="red", fg="white", relief=RIDGE,
                              cursor="hand2")
        searchButton.grid(row=0, column=3)

        searchAllButton = Button(searchFrame, width=12, text="Search ALl", bd=2, relief=RIDGE, bg="red", fg="white",
                                 cursor="hand2")
        searchAllButton.grid(row=0, column=4)

        # Database Entry table

        tableFrame = Frame(rightFrame, bd=2, relief=RIDGE, bg="white")
        tableFrame.place(x=2, y=250, width=650, height=300)

        scrollBarX = ttk.Scrollbar(tableFrame, orient=HORIZONTAL)
        scrollBarY = ttk.Scrollbar(tableFrame, orient=VERTICAL)

        self.studentDetailsTable = ttk.Treeview(tableFrame, columns=("stId", "roll_no",
                                                                     "dep", "course", "year", "sem", "name", "floor",
                                                                     "hod", "phone",
                                                                     "add", "gender", "photo"),
                                                xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)
        scrollBarX.pack(side=BOTTOM, fill=X)
        scrollBarY.pack(side=RIGHT, fill=Y)
        scrollBarX.config(command=self.studentDetailsTable.xview)
        scrollBarY.config(command=self.studentDetailsTable.yview)

        self.studentDetailsTable.heading("stId", text="id")
        self.studentDetailsTable.heading("roll_no", text="Roll no")
        self.studentDetailsTable.heading("dep", text="Department")
        self.studentDetailsTable.heading("course", text="Course")
        self.studentDetailsTable.heading("year", text="Year")
        self.studentDetailsTable.heading("sem", text="Semester")
        self.studentDetailsTable.heading("name", text="Name")
        self.studentDetailsTable.heading("floor", text="Floor")
        self.studentDetailsTable.heading("hod", text="HOD Name")
        self.studentDetailsTable.heading("phone", text="Phone")
        self.studentDetailsTable.heading("add", text="Address")
        self.studentDetailsTable.heading("gender", text="Gender")
        self.studentDetailsTable.heading("photo", text="Photo")
        self.studentDetailsTable["show"] = "headings"

        self.studentDetailsTable.column("stId", width=40)
        self.studentDetailsTable.column('roll_no', width=100)
        self.studentDetailsTable.column('dep', width=100)
        self.studentDetailsTable.column('course', width=80)
        self.studentDetailsTable.column('year', width=50)
        self.studentDetailsTable.column('sem', width=80)
        self.studentDetailsTable.column('name', width=100)
        self.studentDetailsTable.column('floor', width=70)
        self.studentDetailsTable.column('gender', width=70)
        self.studentDetailsTable.column('hod', width=100)
        self.studentDetailsTable.column('phone', width=80)
        self.studentDetailsTable.column('add', width=100)
        self.studentDetailsTable.column('photo', width=50)
        self.studentDetailsTable.pack(fill=BOTH, expand=1)

        self.studentDetailsTable.bind("<ButtonRelease>", self.getCursor)
        self.fetchData()

    def addData(self):
        if self.var_dep.get() == "Select Department" or self.var_Name.get() == "" or self.var_rollNO == "" or self.var_phone == "" or self.var_gender.get() == "Select Gender" or self.var_hodName == "" or self.var_address == "" or self.var_floor == "" or self.var_semester == "" or self.var_course == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="vishu",
                                               database="face_recognisation", auth_plugin='mysql_native_password')
                myCursor = conn.cursor()
                myCursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ID.get(),
                    self.var_rollNO.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_Name.get(),
                    self.var_floor.get(),
                    self.var_hodName.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_gender.get(),
                    self.var_radio.get()
                ))
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("success", "Student details added successfully", parent=self.root)
            except Exception as error:
                messagebox.showerror("Error", f"Due to {str(error)} something went wrong")

    def fetchData(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="vishu", database="face_recognisation",
                                       auth_plugin='mysql_native_password')
        myCursor = conn.cursor()
        sql = "select * from student"
        myCursor.execute(sql)
        data = myCursor.fetchall()
        if len(data) != 0:
            self.studentDetailsTable.delete(*self.studentDetailsTable.get_children())
            for i in data:
                self.studentDetailsTable.insert('', END, values=i)
            conn.commit()
            conn.close()

    def getCursor(self, event=""):
        cursorFocus = self.studentDetailsTable.focus()
        content = self.studentDetailsTable.item(cursorFocus)
        data = content["values"]

        self.var_ID.set(data[0]),
        self.var_rollNO.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_course.set(data[3]),
        self.var_year.set(data[4]),
        self.var_semester.set(data[5]),
        self.var_Name.set(data[6]),
        self.var_floor.set(data[7]),
        self.var_hodName.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_address.set(data[10]),
        self.var_gender.set(data[11]),
        self.var_radio.set(data[12])

    def updateDetails(self):
        if self.var_dep.get() == "Select Department" or self.var_Name.get() == "" or self.var_ID.get() == "" or self.var_ID.get() == "" or self.var_phone == "" or self.var_gender.get() == "Select Gender" or self.var_hodName == "" or self.var_address == "" or self.var_floor == "" or self.var_semester == "" or self.var_course == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you really want to update this data", parent=self.root)
                if Update > 0:

                    conn = mysql.connector.connect(host="localhost", user="root", password="vishu",
                                                   database="face_recognisation",
                                                   auth_plugin='mysql_native_password')
                    myCursor = conn.cursor()
                    myCursor.execute(
                        "update student set  roll_no=%s, dep=%s, course=%s, year=%s, sem=%s, name=%s, floor=%s, hod=%s, phone=%s, address=%s, gender=%s, photo=%s where stID=%s",
                        (
                            self.var_rollNO.get(),
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_Name.get(),
                            self.var_floor.get(),
                            self.var_hodName.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_gender.get(),
                            self.var_radio.get(),
                            self.var_ID.get()

                        ))
                    conn.commit()
                    self.fetchData()
                    conn.close()
                else:
                    if not Update:
                        return
                messagebox.showinfo("success", "Student Details got Updated!!!", parent=self.root)
            except Exception as error:
                messagebox.showerror("Error", str(error), parent=self.root)

    def deleteDetails(self):
        if self.var_ID.get() == "":
            messagebox.showerror("Error", "Atleast one student id is required")
        else:
            try:
                delete = messagebox.askyesno("Delete Student Details", "Are you sure you want to delete this student",
                                             parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="vishu",
                                                   database="face_recognisation",
                                                   auth_plugin='mysql_native_password')
                    myCursor = conn.cursor()
                    sql = "delete from student where stId=%s"
                    val = (self.var_ID.get(),)
                    myCursor.execute(sql, val)
                    conn.commit()
                    self.fetchData()
                    conn.close()
                    messagebox.showinfo("success", "Student Details got deleted!!!", parent=self.root)
                else:
                    if not delete:
                        return
            except Exception as error:
                messagebox.showerror("Error", str(error), parent=self.root)

    def resetDetails(self):
        self.var_ID.set("")
        self.var_rollNO.set("")
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_Name.set("")
        self.var_floor.set("")
        self.var_hodName.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_gender.set("")

    def generateData(self):
        self.recordingOn()
        userId = self.var_ID.get()
        if self.var_dep.get() == "Select Department" or self.var_Name.get() == "" or self.var_ID.get() == "" or self.var_ID.get() == "" or self.var_phone == "" or self.var_gender.get() == "Select Gender" or self.var_hodName == "" or self.var_address == "" or self.var_floor == "" or self.var_semester == "" or self.var_course == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="vishu",
                                               database="face_recognisation",
                                               auth_plugin='mysql_native_password')
                myCursor = conn.cursor()
                myCursor.execute("select * from student")
                result = myCursor.fetchall()
                id = 0
                for x in result:
                    id = id + 1
                self.var_ID.set(id)
                myCursor.execute(
                    "update student set  roll_no=%s, dep=%s, course=%s, year=%s, sem=%s, name=%s, floor=%s, hod=%s, phone=%s, address=%s, gender=%s, photo=%s where stID=%s",
                    (
                        self.var_rollNO.get(),
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_Name.get(),
                        self.var_floor.get(),
                        self.var_hodName.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_gender.get(),
                        self.var_radio.get(),
                        self.var_ID.get() == id + 1
                    ))
                conn.commit()
                self.fetchData()
                self.resetDetails()
                conn.close()

                faceClassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                def faceCropped(img):
                    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = faceClassifier.detectMultiScale(grey, 1.3, 5)

                    for (x, y, w, h) in faces:
                        faceCropped = img[y:y + h, x:x + w]
                        return faceCropped

                cap = cv2.VideoCapture(0)
                imgId = 0
                while True:
                    ret, frame = cap.read()
                    if faceCropped(frame) is not None:
                        imgId += 1
                        face = cv2.resize(faceCropped(frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        fileName = "data/user." + userId + "." + str(imgId) + ".jpg"
                        cv2.imwrite(fileName, face)
                        cv2.putText(face, str(imgId), (100, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(imgId) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!!", parent=self.root)
                self.recordingOff()



            except Exception as error:
                messagebox.showerror("Error", str(error), parent=self.root)

    def openImages(self):
        os.startfile("data")

    def recordingOn(self):
        recordingOn = pyttsx3.init()
        recordingOn.say("Now Your Face is Analyzing Please Be still")
        recordingOn.runAndWait()
    def recordingOff(self):
        recordingOff = pyttsx3.init()
        recordingOff.say("Face has been Analyzed Thankyou for using me..")
        recordingOff.runAndWait()

if __name__ == "__main__":
    root = Tk()
    obj = studentDetails(root)
    root.withdraw()
    root.mainloop()
